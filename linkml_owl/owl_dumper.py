import json
from collections import defaultdict
from typing import Optional, List, Set, Any, Union, Dict, Tuple
from dataclasses import dataclass, field
import logging
import click
from linkml_runtime import SchemaView

from rdflib import URIRef

from hbreader import hbread
from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition, Definition
from linkml_runtime.utils.formatutils import underscore, camelcase
from linkml_runtime.linkml_model.types import Uri, Uriorcurie

from funowl import OntologyDocument, Ontology, IRI, ObjectSomeValuesFrom, \
    Literal, \
    ObjectUnionOf, SubClassOf, ClassAssertion, \
    Class, Individual, \
    AnnotationAssertion, ObjectPropertyAssertion, \
    Prefix, AnonymousIndividual, ObjectAllValuesFrom, EquivalentClasses, ObjectIntersectionOf, ClassExpression
from pyld.jsonld import expand
from rdflib import Graph, BNode
from rdflib.namespace import RDF, RDFS, OWL
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from linkml_runtime.dumpers.rdf_dumper import RDFDumper
from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.context_utils import CONTEXTS_PARAM_TYPE, CONTEXT_TYPE
from linkml_runtime.utils.yamlutils import YAMLRoot

INTERPRETATION = str
AXIOM_TYPE_NAME = str
OPERAND = str  ## e.g IntersectionOf, UnionOf

LEVEL = int
OP_KEY = Tuple[LEVEL, OPERAND, AXIOM_TYPE_NAME]


@dataclass
class EntityAxiomIndex:
    operand_list_index: Dict[OP_KEY, List[ClassExpression]] = field(default_factory=lambda: defaultdict(list))

    def add_operand(self, key: OP_KEY, op: ClassExpression):
        if key not in self.operand_list_index:
            self.operand_list_index[key] = []
        self.operand_list_index[key].append(op)

    def add_operands(self, key: OP_KEY, ops: List[ClassExpression]):
        for op in ops:
            self.add_operand(key, op)


class OWLDumper(Dumper):
    """
    Translate LinkML instances to OWL

    This differs from rdf_dumper in that each edge in the linkml instance graph
    may have a more complex OWL interpretation; for example:

     - lists may be treat as unions, rather than conjunctions of triples
     - linkml instances may be OWL classes
        - edges from these instances may be treated as axiom types such as SubClassOf R some Y

    Note that currently the OWL interpretation is "smuggled" into a model by way of special-syntax
    comments. In future we will either have a formal mapping file or extend the mapping syntax

    For context, see:
    https://github.com/linkml/linkml/issues/267
    """

    def to_ontology_document(self, element: Union[YAMLRoot, List[YAMLRoot]], schema: SchemaDefinition, iri=None) -> str:
        """
        Dump a linkml instance tree as a function syntax OWL ontology string
        """
        o = Ontology(schema.id)
        self.ontology = o
        self.schema = schema
        self.schemaview = SchemaView(schema)
        #o.annotation(RDFS.label, name)
        doc = OntologyDocument(iri, o)
        if isinstance(element, list):
            for e1 in element:
                self.transform(e1, schema)
        else:
            self.transform(element, schema)
        return doc

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition, iri=None) -> str:
        """
        Dump a linkml instance tree as a function syntax OWL ontology string
        """
        doc = to_ontology_document(element, schema, iri=iri)
        return str(doc)

    def transform(self, element: YAMLRoot, schema: SchemaDefinition, is_element_an_object=True,
                  is_element_an_owl_class=False) -> Any:
        """
        Recursively transform a LinkML element

        Each field is introspected, and translated to an OWL axiom.
        The field value is recursively transformed
        """
        if element is None:
            return None
        try:
            meaning = element.meaning
            return self._get_IRI_str(meaning)
        except:
            None
        if not self._instance_of_linkml_class(element):
            # TODO: better way of detecting atoms
            if is_element_an_object:
                # foreign key
                return self._get_IRI_str(element)
            elif isinstance(element, Uriorcurie):
                return self._get_IRI_str(element)
            elif isinstance(element, Uri):
                return URIRef(element)
            else:
                # literal
                return Literal(element)
        o = self.ontology
        python_type = type(element)
        #print(f'E={element }PT={python_type}')
        linkml_class_name = python_type.class_name
        c = schema.classes[linkml_class_name]
        cls_interps = self._get_interpretations(c)
        if Class.__name__ in cls_interps:
            is_element_an_owl_class = True
        subj = None
        conjunction_groups = []
        disjunction_groups = []
        eai = EntityAxiomIndex()
        for k, v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            if slot is None:
                raise ValueError(f'Lookup slot in {c.name} failed for {k}')
            if slot.identifier:
                subj = URIRef(self._get_IRI_str(v))
        if subj is None:
            subj = AnonymousIndividual()
        for k, v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            actual_slot = self._get_actual_slot(slot)
            if slot is None:
                logging.error(f'No slot for {k}')
                continue
            if slot.identifier or actual_slot.identifier:
                continue
            slot_uri = self._get_IRI_str(actual_slot.slot_uri)
            print(f'in {subj} {k} = {v} (URI={actual_slot.slot_uri}) // slot = {slot.name}')
            interps = self._get_interpretations(slot)
            print(f'INTERPS={interps}')
            if len(interps) == 0:
                interps = self._get_interpretations(actual_slot)
            is_disjunction = 'UnionOf' in interps
            is_conjunction = 'IntersectionOf' in interps
            is_equiv = 'EquivalentTo' in interps  ## TODO: used?
            is_object_ref = slot.range in self.schema.classes

            if isinstance(v, list):
                input_vals = v
            elif isinstance(v, dict):
                input_vals = v.values()
            else:
                input_vals = [v]
            tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in input_vals]
            print(f'TR Vals={tr_vals}')
            if is_element_an_owl_class:
                # TODO: is this used?
                if is_equiv:
                    axiomType = EquivalentClasses
                else:
                    axiomType = SubClassOf
            else:
                axiomType = None
            parents = []
            axiomType = SubClassOf
            is_class_logical_axiom = False
            for tr_val in tr_vals:
                print(f'  TR_VAL = {tr_val}')
                if tr_val is None:
                    continue
                if slot.range in self.schema.classes:
                    if isinstance(tr_val, str):
                        tr_val = self._get_IRI_str(tr_val)
                parent = tr_val
                if ObjectSomeValuesFrom.__name__ in interps:
                    parent = ObjectSomeValuesFrom(slot_uri, tr_val)
                    is_class_logical_axiom = True
                    #axiomType = SubClassOf
                elif ObjectAllValuesFrom.__name__ in interps:
                    parent = ObjectAllValuesFrom(slot_uri, tr_val)
                    is_class_logical_axiom = True
                    #axiomType = SubClassOf
                elif SubClassOf.__name__ in interps:
                    axiomType = SubClassOf
                elif EquivalentClasses.__name__ in interps:
                    axiomType = EquivalentClasses
                else:
                    axiomType = AnnotationAssertion
                parents.append(parent)
            axiomType = None
            if SubClassOf.__name__ in interps:
                axiomType = SubClassOf
            elif EquivalentClasses.__name__ in interps:
                axiomType = EquivalentClasses
            if axiomType is None:
                if is_class_logical_axiom:
                    axiomType = SubClassOf
                else:
                    axiomType = AnnotationAssertion
            print(f'AXIOM TYPE = {axiomType}')
            # TODO: delay conj/disj
            if is_disjunction:
                # translate the filler list to a single entry that is a disjunction
                disj = ObjectUnionOf(*parents)
                #parents = [disj]
                if len(disjunction_groups) == 0:
                    disjunction_groups = [[]]
                disjunction_groups[0] += parents
                level = 0
                eai.add_operands((level, axiomType.__name__, ObjectUnionOf.__name__), parents)
                parents = []
            if is_conjunction:
                # translate the filler list to a single entry that is a conjunction
                conj = ObjectIntersectionOf(*parents)
                #parents = [conj]
                if len(conjunction_groups) == 0:
                    conjunction_groups = [[]]
                conjunction_groups[0] += parents
                level = 0
                eai.add_operands((level, axiomType.__name__, ObjectIntersectionOf.__name__), parents)
                parents = []
            for parent in parents:
                if axiomType == SubClassOf:
                    print(f'type(subj) = {type(subj)} // {subj}')
                    if isinstance(subj, AnonymousIndividual):
                        axiom = None
                    else:
                        axiom = SubClassOf(subj, parent)
                elif axiomType == EquivalentClasses:
                    axiom = EquivalentClasses(subj, parent)
                elif axiomType == ClassAssertion:
                    axiom = ClassAssertion(parent, subj)
                elif axiomType == ObjectPropertyAssertion:
                    axiom = ObjectPropertyAssertion(slot_uri, subj, parent)
                elif axiomType == AnnotationAssertion:
                    axiom = AnnotationAssertion(slot_uri, subj, parent)
                else:
                    raise Exception(f'Unknown: {axiomType}')
                if axiom is not None:
                    o.axioms.append(axiom)
        #for operands in conjunction_groups:
        #    o.axioms.append(EquivalentClasses(subj, *operands))
        #for operands in disjunction_groups:
        #    o.axioms.append(ObjectUnionOf(subj, *operands))
        for op_key, operands in eai.operand_list_index.items():
            _, interp, operator = op_key
            print(f'EAI {subj}: {interp} => {operator} over {operands}')
            if operator == ObjectUnionOf.__name__:
                expr = ObjectUnionOf(*operands)
            elif operator == ObjectIntersectionOf.__name__:
                expr = ObjectIntersectionOf(*operands)
            else:
                raise ValueError(f'Cannot handle: {operator}')
            if interp == EquivalentClasses.__name__:
                axiom = EquivalentClasses(subj, expr)
            elif interp == SubClassOf.__name__:
                axiom = SubClassOf(subj, expr)
            else:
                raise ValueError(f'Not handled: {interp}')
            o.axioms.append(axiom)
        #if isinstance(subj, AnonymousIndividual):
        #  TODO: nesting
        return subj

    def _instance_of_linkml_class(self, v) -> bool:
        try:
            type(v).class_name
            return True
        except:
            return False

    def _lookup_slot(self, cls: ClassDefinition, field: str) -> SlotDefinition:
        matching_slot = None
        for s in self.schemaview.class_induced_slots(cls.name):
            if underscore(s.name) == field:
                matching_slot = s
                break
            if s.alias and underscore(s.alias) == field:
                matching_slot = s
                break
        if matching_slot:
            if not matching_slot.slot_uri:
                uri = self.schemaview.get_uri(matching_slot)
                matching_slot.slot_uri = uri
            return matching_slot
        else:
            logging.error(f'Did not find {field} in {cls.name} slots =  {cls.slots}')

    def _get_interpretations(self, x: Definition) -> Set[INTERPRETATION]:
        interps = set()
        OWL_MARKER = 'OWL>>'
        for c in x.comments:
            if c.startswith(OWL_MARKER):
                n = c.replace(OWL_MARKER, '').strip()
                interps.add(n)
        if 'owl' in x.annotations:
            interps.update([s.strip() for s in x.annotations['owl'].value.split(',')])
        return interps

    def _get_IRI_str(self, id: str) -> str:
        uri = self.schemaview.expand_curie(id)
        if uri:
            return uri
        # CHECK IF WE NEED LEGACY CODE BELOW; TODO
        if id.startswith('http'):
            return id
        parts = id.split(':')
        if len(parts) == 2:
            [pfx, local] = parts
            if pfx in self.schema.prefixes:
                return f'{self.schema.prefixes[pfx].prefix_reference}{local}'
            else:
                logging.error(f'Undeclared: {pfx} -- just using {id}')
        return id

    def _get_actual_slot(self, slot: SlotDefinition) -> SlotDefinition:
        """
        See
        https://github.com/linkml/linkml/issues/270
        for context
        """
        alias = slot.alias
        if alias in self.schema.slots:
            actual_slot = self.schema.slots[alias]
        else:
            actual_slot = slot
        if actual_slot.name != slot.name:
            logging.warning(f'Using actual slot uri: {actual_slot.name} >> {slot.name}')
        return actual_slot

@click.option('-s', '--schema-file', required=True, help="""
Path to LinkML schema
""")
@click.command()
def cli(inputfile: str, schema_file: str, raw: bool, **args):
    """
    Dump LinkML instance data as OWL
    """
    schema = YAMLGenerator(schema_file).schema
    element = yaml_loader.load(inputfile)
    dumper = OWLDumper()
    ont = dumper.dumps(collection, schema)
    with open(OWL_OUT, 'w') as stream:
        stream.write(str(ont))


if __name__ == '__main__':
    cli()