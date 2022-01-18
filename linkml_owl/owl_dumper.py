from collections import defaultdict
from typing import Optional, List, Set, Any, Union, Dict, Tuple
from dataclasses import dataclass, field
import logging

import click
from funowl.converters.functional_converter import to_python
from jinja2 import Template
from linkml.generators.pythongen import PythonGenerator
from linkml.utils import datautils
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import meta
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.compile_python import compile_python

from rdflib import URIRef

from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition, Definition, \
    ClassDefinitionName
from linkml_runtime.utils.formatutils import underscore, camelcase
from linkml_runtime.linkml_model.types import Uri, Uriorcurie

from funowl import OntologyDocument, Ontology, IRI, ObjectSomeValuesFrom, \
    Literal, \
    ObjectUnionOf, SubClassOf, ClassAssertion, \
    Class, Individual, \
    AnnotationAssertion, ObjectPropertyAssertion, \
    Prefix, AnonymousIndividual, ObjectAllValuesFrom, EquivalentClasses, ObjectIntersectionOf, ClassExpression, Axiom, \
    ObjectProperty, Declaration, ObjectInverseOf, InverseObjectProperties, ObjectPropertyDomain, ObjectPropertyRange, \
    SubObjectPropertyOf, TransitiveObjectProperty, SymmetricObjectProperty, AsymmetricObjectProperty, \
    ReflexiveObjectProperty, IrreflexiveObjectProperty

from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.yamlutils import YAMLRoot

from linkml_owl.util.loader_wrapper import load_structured_file

INTERPRETATION = str
AXIOM_TYPE_NAME = str
OPERAND = str  ## e.g IntersectionOf, UnionOf

LEVEL = int
OP_KEY = Tuple[LEVEL, OPERAND, AXIOM_TYPE_NAME]


@dataclass
class EntityAxiomIndex:
    """
    For indexing axioms that involve an aggregate grouping (intersection, union)

    Any object can have any number of these axioms. They are grouped by:

    - Operator (e.g. AND/IntersectionOf, OR/Union)
    - AxiomType (e.g. SubClassOf, EquivalentClasses)
    - Level (default 0), allows for example multiple equivalence axioms using intersection
    """
    operand_list_index: Dict[OP_KEY, List[ClassExpression]] = field(default_factory=lambda: defaultdict(list))

    def add_operand(self, key: OP_KEY, op: ClassExpression):
        """

        :param key: combo of operator/axiomType/level
        :param op: operand - an element of the list used to construct the operator construct
        :return:
        """
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

    def to_ontology_document(self, element: Union[YAMLRoot, List[YAMLRoot]], schema: Union[SchemaDefinition, str], iri=None) -> str:
        """
        Convert a linkml instance tree as a function syntax OWL ontology string
        """
        o = Ontology(schema.id)
        self.ontology = o
        if isinstance(schema, SchemaDefinition):
            self.schema = schema
            self.schemaview = SchemaView(schema)
        else:
            self.schemaview = SchemaView(schema)
            self.schema = self.schemaview.schema
            schema = self.schema
        #o.annotation(RDFS.label, name)
        doc = OntologyDocument(iri, o)
        if isinstance(element, list):
            for e1 in element:
                self.transform(e1, schema)
        else:
            self.transform(element, schema)
        for pfx in schema.prefixes.values():
            doc.prefixDeclarations.append(Prefix(pfx.prefix_prefix, pfx.prefix_reference))
        return doc

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition = None, schemaview: SchemaView = None, iri=None) -> str:
        """
        Dump a linkml instance tree as a function syntax OWL ontology string

        :param element:
        :param schema:
        :param schemaview:
        :param iri:
        :return:
        """
        if schemaview:
            schema = schemaview.schema
        doc = self.to_ontology_document(element, schema, iri=iri)
        return str(doc)

    def transform(self, element: YAMLRoot, schema: SchemaDefinition, is_element_an_object=True,
                  is_element_an_owl_class=False) -> Any:
        """
        Recursively transform a LinkML element

        Each field is introspected, and translated to an OWL axiom.
        The field value is recursively transformed

        :param element:
        :param schema:
        :param is_element_an_object:
        :param is_element_an_owl_class:
        :return:
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
                return URIRef(self._get_IRI_str(element))
            elif isinstance(element, Uriorcurie):
                return URIRef(self._get_IRI_str(element))
            elif isinstance(element, Uri):
                return URIRef(element)
            else:
                # literal
                return Literal(element)
        o = self.ontology
        python_type = type(element)
        #logging.debug(f'E={element }PT={python_type}')
        linkml_class_name = python_type.class_name
        c = schema.classes[linkml_class_name]
        #if 'owl.fstring' in c.annotations:
        #    self.add_axioms_from_fstring(c.annotations['owl.fstring'], element)
        for fstr in self._get_inferred_class_annotations(c, 'owl.fstring'):
            self.add_axioms_from_fstring(fstr, element)
        for tmpl_str in self._get_inferred_class_annotations(c, 'owl.template'):
            self.add_axioms_from_template(tmpl_str, element)
        #if 'owl.template' in c.annotations:
        #    self.add_axioms_from_template(c.annotations['owl.template'], element)
        cls_interps = self._get_class_interpretations(c)
        #cls_interps = self._get_interpretations(c)
        if Class.__name__ in cls_interps:
            is_element_an_owl_class = True
        subj = None
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
        if ObjectProperty.__name__ in cls_interps:
            decl = Declaration(ObjectProperty(subj))
            o.axioms.append(decl)
        for k, v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            actual_slot = self._get_actual_slot(slot)
            owl_templates = self._get_inferred_slot_annotations(slot, 'owl.template', linkml_class_name)
            owl_fstrings = self._get_inferred_slot_annotations(slot, 'owl.fstring', linkml_class_name)
            boolean_form_of = self._get_inferred_slot_annotations(slot, 'boolean_form_of', linkml_class_name)
            for tmpl in owl_templates:
                self.add_axioms_from_template(tmpl, element)
            #if 'owl.template' in slot.annotations and v is not None:
            #    self.add_axioms_from_template(slot.annotations['owl.template'], element)
            if slot is None:
                logging.error(f'No slot for {k}')
                continue
            if slot.identifier:
                continue
            slot_uri = self._get_IRI_str(actual_slot.slot_uri)
            #slot_uri = slot.slot_uri
            logging.debug(f'in {subj} {k} = {v} (URI={actual_slot.slot_uri}) // slot = {slot.name}')
            #interps = self._get_interpretations(slot)
            interps = self._get_slot_interpretations(slot, linkml_class_name)
            logging.debug(f'INTERPS={interps}')
            #if len(interps) == 0:
            #    interps = self._get_interpretations(actual_slot)
            is_disjunction = 'UnionOf' in interps
            is_conjunction = 'IntersectionOf' in interps
            is_annotation = 'AnnotationProperty' in interps or 'Annotation' in interps
            is_object_ref = slot.range in self.schema.classes

            # normalize input_vals to a list, then transform
            if isinstance(v, list):
                input_vals = v
            elif isinstance(v, dict):
                input_vals = v.values()
            else:
                input_vals = [v]
            tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in input_vals]
            logging.debug(f'TR Vals={tr_vals}')
            parents = []
            is_class_logical_axiom = False
            for tr_val in tr_vals:
                logging.debug(f'  TR_VAL = {tr_val}')
                if tr_val is None:
                    continue
                if owl_fstrings:
                    for owl_fstring in owl_fstrings:
                        self.add_axioms_from_fstring(owl_fstring, element, tr_val)
                    continue
                #if 'owl.fstring' in slot.annotations and v is not None:
                #    self.add_axioms_from_fstring(slot.annotations['owl.fstring'], element, tr_val)
                #    continue
                if slot.range in self.schema.classes:
                    if isinstance(tr_val, str):
                        tr_val = self._get_IRI_str(tr_val)
                parent = tr_val
                if boolean_form_of:
                    if parent and parent == Literal(True):
                        for owl_uri in boolean_form_of:
                            if owl_uri == 'owl:TransitiveProperty':
                                o.axioms.append(TransitiveObjectProperty(subj))
                            elif owl_uri == 'owl:SymmetricProperty':
                                o.axioms.append(SymmetricObjectProperty(subj))
                            elif owl_uri == 'owl:AsymmetricProperty':
                                o.axioms.append(AsymmetricObjectProperty(subj))
                            elif owl_uri == 'owl:ReflexiveProperty':
                                o.axioms.append(ReflexiveObjectProperty(subj))
                            elif owl_uri == 'owl:IrreflexiveProperty':
                                o.axioms.append(IrreflexiveObjectProperty(subj))
                            else:
                                raise ValueError(f'Cannot interpret {owl_uri}')
                # transform parents if an expression type is specified
                if ObjectSomeValuesFrom.__name__ in interps:
                    parent = ObjectSomeValuesFrom(slot_uri, tr_val)
                    is_class_logical_axiom = True
                elif ObjectAllValuesFrom.__name__ in interps:
                    parent = ObjectAllValuesFrom(slot_uri, tr_val)
                    is_class_logical_axiom = True
                elif SubClassOf.__name__ in interps:
                    is_class_logical_axiom = True
                elif EquivalentClasses.__name__ in interps:
                    is_class_logical_axiom = True
                parents.append(parent)
            axiom_type = None
            # TODO: make this more generic / less repetitive
            if SubClassOf.__name__ in interps:
                axiom_type = SubClassOf
            elif SubObjectPropertyOf.__name__ in interps:
                axiom_type = SubObjectPropertyOf
            elif EquivalentClasses.__name__ in interps:
                axiom_type = EquivalentClasses
            elif InverseObjectProperties.__name__ in interps:
                axiom_type = InverseObjectProperties
            elif ObjectPropertyDomain.__name__ in interps:
                axiom_type = ObjectPropertyDomain
            elif ObjectPropertyRange.__name__ in interps:
                axiom_type = ObjectPropertyRange
            elif AnnotationAssertion.__name__ in interps:
                axiom_type = AnnotationAssertion
            if axiom_type is None:
                if is_class_logical_axiom:
                    if is_annotation:
                        raise ValueError(f'{slot.name} cannot be both logical and an annotation')
                    axiom_type = SubClassOf
                else:
                    if is_annotation:
                        axiom_type = AnnotationAssertion
                    else:
                        axiom_type = None
            logging.debug(f'AXIOM TYPE = {axiom_type}')
            if not axiom_type:
                continue
            if is_disjunction:
                # translate the filler list to a single entry that is a disjunction
                # TODO: allow for different groupings; for now default to 0
                level = 0
                eai.add_operands((level, axiom_type.__name__, ObjectUnionOf.__name__), parents)
                parents = []
            if is_conjunction:
                # translate the filler list to a single entry that is a conjunction
                # TODO: allow for different groupings; for now default to 0
                level = 0
                eai.add_operands((level, axiom_type.__name__, ObjectIntersectionOf.__name__), parents)
                parents = []
            for parent in parents:
                # TODO: make this more generic
                if axiom_type == SubClassOf:
                    logging.debug(f'type(subj) = {type(subj)} // {subj}')
                    if isinstance(subj, AnonymousIndividual):
                        axiom = None
                    else:
                        axiom = SubClassOf(subj, parent)
                elif axiom_type == SubObjectPropertyOf:
                    axiom = SubObjectPropertyOf(subj, parent)
                elif axiom_type == EquivalentClasses:
                    axiom = EquivalentClasses(subj, parent)
                elif axiom_type == ClassAssertion:
                    axiom = ClassAssertion(parent, subj)
                elif axiom_type == ObjectPropertyAssertion:
                    axiom = ObjectPropertyAssertion(slot_uri, subj, parent)
                elif axiom_type == InverseObjectProperties:
                    axiom = InverseObjectProperties(subj, parent)
                elif axiom_type == ObjectPropertyDomain:
                    axiom = ObjectPropertyDomain(subj, parent)
                elif axiom_type == ObjectPropertyRange:
                    axiom = ObjectPropertyRange(subj, parent)
                elif axiom_type == AnnotationAssertion:
                    axiom = AnnotationAssertion(slot_uri, subj, parent)
                else:
                    raise Exception(f'Unknown: {axiom_type}')
                if axiom is not None:
                    o.axioms.append(axiom)
        for op_key, operands in eai.operand_list_index.items():
            _, interp, operator = op_key
            logging.debug(f'EAI {subj}: {interp} => {operator} over {operands}')
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
            if type(v).class_name:
                return True
        except Exception:
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

    def _get_inferred_slot_annotations(self, slot: SlotDefinition, ann_key: str,
                                       class_name: ClassDefinitionName) -> List[str]:
        vals = set()
        anc_slots = [slot]
        sv = self.schemaview
        for anc_c in sv.class_ancestors(class_name, reflexive=True):
            induced_slot = sv.induced_slot(slot.name, anc_c)
            anc_slots.append(induced_slot)
        for a in sv.slot_ancestors(slot.name, reflexive=True):
            anc_slots.append(sv.get_slot(a))
        for s in anc_slots:
            if ann_key == 'owl':
                # inject inferred annotations
                slot_uri = s.slot_uri
                if slot_uri == 'owl:inverseOf':
                    vals.add(InverseObjectProperties.__name__)
                if slot_uri == 'rdfs:domain':
                    vals.add(ObjectPropertyDomain.__name__)
                if slot_uri == 'rdfs:range':
                    vals.add(ObjectPropertyRange.__name__)
            if ann_key in s.annotations:
                if ann_key == 'owl':
                    vals.update([v.strip() for v in s.annotations[ann_key].value.split(',')])
                else:
                    vals.add(s.annotations[ann_key].value)
        return list(vals)

    def _get_inferred_class_annotations(self, cls: ClassDefinition, ann_key: str) -> List[str]:
        vals = set()
        anc_classes = [cls]
        sv = self.schemaview
        for anc_c in sv.class_ancestors(cls.name, reflexive=True):
            anc_classes.append(sv.get_class(anc_c))
        for s in anc_classes:
            if ann_key in s.annotations:
                if ann_key == 'owl':
                    vals.update([v.strip() for v in s.annotations[ann_key].value.split(',')])
                else:
                    vals.add(s.annotations[ann_key].value)
        return list(vals)

    def _get_class_interpretations(self, cls: ClassDefinition) -> Set[INTERPRETATION]:
        return set(self._get_inferred_class_annotations(cls, 'owl'))

    def _get_slot_interpretations(self, slot: SlotDefinition, class_name: ClassDefinitionName) -> Set[INTERPRETATION]:
        return set(self._get_inferred_slot_annotations(slot, 'owl', class_name))

    def _get_interpretations(self, x: Definition) -> Set[INTERPRETATION]:

        if isinstance(x, SlotDefinition):
            anc_names = self.schemaview.slot_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_slot(a) for a in anc_names] + [x]
        elif isinstance(x, ClassDefinition):
            anc_names = self.schemaview.class_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_class(a) for a in anc_names] + [x]
        else:
            raise ValueError(f'Not supported: {type(x)}')
        interps = set()
        #OWL_MARKER = 'OWL>>'
        for x in ancs:
            #for c in x.comments:
            #    logging.warning('Use of OWL>> is deprecated - replace with an annotation')
            #    # TODO: deprecated comment-based way of doing this
            #    if c.startswith(OWL_MARKER) and False:
            #        n = c.replace(OWL_MARKER, '').strip()
            #        interps.add(n)
            if 'owl' in x.annotations:
                interps.update([s.strip() for s in x.annotations['owl'].value.split(',')])
            # TODO: make this more declarative/generic; use a mapping of URIs => OWL types
            if isinstance(x, SlotDefinition):
                slot_uri = x.slot_uri
                if slot_uri == 'owl:inverseOf':
                    interps.add(InverseObjectProperties.__name__)
                if slot_uri == 'rdfs:domain':
                    interps.add(ObjectPropertyDomain.__name__)
                if slot_uri == 'rdfs:range':
                    interps.add(ObjectPropertyRange.__name__)
        return interps


    def OLD_get_interpretations(self, x: Definition) -> Set[INTERPRETATION]:
        if isinstance(x, SlotDefinition):
            anc_names = self.schemaview.slot_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_slot(a) for a in anc_names] + [x]
        elif isinstance(x, ClassDefinition):
            anc_names = self.schemaview.class_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_class(a) for a in anc_names] + [x]
        else:
            raise ValueError(f'Not supported: {type(x)}')
        interps = set()
        #OWL_MARKER = 'OWL>>'
        for x in ancs:
            #for c in x.comments:
            #    logging.warning('Use of OWL>> is deprecated - replace with an annotation')
            #    # TODO: deprecated comment-based way of doing this
            #    if c.startswith(OWL_MARKER) and False:
            #        n = c.replace(OWL_MARKER, '').strip()
            #        interps.add(n)
            if 'owl' in x.annotations:
                interps.update([s.strip() for s in x.annotations['owl'].value.split(',')])
            # TODO: make this more declarative/generic; use a mapping of URIs => OWL types
            if isinstance(x, SlotDefinition):
                slot_uri = x.slot_uri
                if slot_uri == 'owl:inverseOf':
                    interps.add(InverseObjectProperties.__name__)
                if slot_uri == 'rdfs:domain':
                    interps.add(ObjectPropertyDomain.__name__)
                if slot_uri == 'rdfs:range':
                    interps.add(ObjectPropertyRange.__name__)
        return interps

    def _get_IRI_str(self, id: str) -> str:
        uri = self.schemaview.expand_curie(id)
        if uri:
            return uri

    # TODO: deprecate this
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

    def parse_axioms_string(self, owl_str: str, schemaview: SchemaView = None) -> OntologyDocument:
        if schemaview is None:
            schemaview = self.schemaview
        prefix_lines = []
        for prefix, url in schemaview.namespaces().items():
            prefix_lines.append(f'Prefix( {prefix}: = <{url}> )')
        header = "\n".join(prefix_lines)
        owl_str = f'{header}\nOntology(\n{owl_str}\n)'
        logging.debug(owl_str)
        try:
            doc = to_python(owl_str)
        except Exception as e:
            logging.error(f'Error parsing generated OWL: {owl_str}')
            raise e
        from funowl.writers.FunctionalWriter import FunctionalWriter
        from rdflib import Graph
        g = Graph()
        for p in doc.prefixDeclarations:
            g.namespace_manager.bind(p.prefixName, p.fullIRI)
        fw = FunctionalWriter(g=g)
        owl_str_roundtrip = doc.to_functional(fw)
        #logging.debug(f'ROUNDTRIP = {owl_str_roundtrip}')
        return doc

    def _element_to_template_dict(self, element: YAMLRoot, val: Any = None):
        d = {'this': element, 'V': val}
        for k, v in vars(element).items():
            d[k] = v
        return d

    def add_axioms_from_fstring(self, fstring: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None):
        if isinstance(fstring, meta.Annotation):
            fstring = fstring.value
        d = self._element_to_template_dict(element, val)
        owl_str = fstring.format(**d)
        logging.debug(f'FSTRING = {owl_str}')
        axioms = self.parse_axioms_string(owl_str).ontology.axioms
        logging.debug(f'AXIOMS >> = {axioms}')
        self.ontology.axioms += axioms

    def add_axioms_from_template(self, template_ann: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None):
        # TODO: simplify, change arg to str
        d = self._element_to_template_dict(element, val)
        if isinstance(template_ann, str):
            tstr = template_ann
        else:
            tstr = template_ann.value
        jt = Template(tstr)
        owl_str = jt.render(**d)
        axioms = self.parse_axioms_string(owl_str).ontology.axioms
        self.ontology.axioms += axioms


@click.command()
@click.option('-s', '--schema', required=True,
              help="Path to LinkML schema")
@click.option("--target-class", "-C",
              help="name of class in datamodel that the root node instantiates")
@click.option("--module", "-m",
              help="Path to python datamodel module")
@click.option("--format", "-f",
              help="Input format (will be inferred from file suffix if not specified)")
@click.option('-o', '--output', required=True,
              help="Path to OWL functional syntax output")
@click.argument('inputfile')
def cli(inputfile: str, schema: str, target_class, module, output, format, **args):
    """
    Dump LinkML instance data as OWL

    Examples:

    Convert a CSV to OWL

        linkml-data2owl -s tests/inputs/owl_dumper_test.yaml tests/inputs/parts.csv -o parts.ofn

        Note in this example, there must be a class type designator column `@type` in the CSV

    Convert a CSV to OWL, homogeneous classes:

        linkml-data2owl -C EquivGenusAndPartOf -s tests/inputs/owl_dumper_test.yaml \
            tests/inputs/parts_implicit_type.csv -o parts.ofn

    Convert YAML or JSON to OWL:

        linkml-data2owl -s tests/inputs/owl_dumper_test.yaml tests/inputs/owl_dumper_test_data.yaml -o ont.ofn

    """
    if module is None:
        if schema is None:
            raise Exception('must pass one of module OR schema')
        else:
            python_module = PythonGenerator(schema).compile_module()
    else:
        python_module = compile_python(module)
    sv = SchemaView(schema)
    element = load_structured_file(inputfile, target_class=target_class, python_module=python_module, schemaview=sv, fmt=format)
    dumper = OWLDumper()
    doc = dumper.dumps(element, schemaview=sv)
    with open(output, 'w') as stream:
        stream.write(str(doc))


if __name__ == '__main__':
    cli()