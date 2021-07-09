import json
from typing import Optional, List, Set, Any
from dataclasses import dataclass
import logging

from rdflib import URIRef

from hbreader import hbread
from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition, Definition
from linkml_runtime.utils.formatutils import underscore, camelcase
from linkml_runtime.linkml_model.types import Uri, Uriorcurie

from funowl import OntologyDocument, Ontology, IRI, ObjectSomeValuesFrom,\
    Literal,\
    ObjectUnionOf, SubClassOf, ClassAssertion,\
    Class, Individual,\
    AnnotationAssertion, ObjectPropertyAssertion,\
    Prefix, AnonymousIndividual
from pyld.jsonld import expand
from rdflib import Graph, BNode
from rdflib.namespace import RDF, RDFS, OWL
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from linkml_runtime.dumpers.rdf_dumper import RDFDumper
from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.context_utils import CONTEXTS_PARAM_TYPE, CONTEXT_TYPE
from linkml_runtime.utils.yamlutils import YAMLRoot

INTERPRETATION = str

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

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition, iri=None) -> str:
        """
        Dump a linkml instance tree as a function syntax OWL ontology string
        """
        o = Ontology(schema.id)
        self.ontology = o
        self.schema = schema
        #o.annotation(RDFS.label, name)
        doc = OntologyDocument(iri, o)
        self.transform(element, schema)
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
        for k,v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
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
            if len(interps) == 0:
                interps = self._get_interpretations(actual_slot)
            #print(f'Interps = {interps}')
            is_disjunction = 'UnionOf' in interps
            is_object_ref = slot.range in self.schema.classes

            if isinstance(v, list):
                input_vals = v
            elif isinstance(v, dict):
                input_vals = v.values()
            else:
                input_vals = [v]
            tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in input_vals]
            #print(f'Vals={tr_vals}')
            if is_element_an_owl_class:
                axiomType = SubClassOf
            else:
                axiomType = ClassAssertion
            parents = []
            for tr_val in tr_vals:
                if tr_val is None:
                    continue
                if slot.range in self.schema.classes:
                    if isinstance(tr_val, str):
                        tr_val = self._get_IRI_str(tr_val)
                parent = tr_val
                if ObjectSomeValuesFrom.__name__ in interps:
                    parent = ObjectSomeValuesFrom(slot_uri, tr_val)
                    axiomType = SubClassOf
                elif SubClassOf.__name__ in interps:
                    axiomType = SubClassOf
                else:
                    axiomType = AnnotationAssertion
                parents.append(parent)
            if is_disjunction:
                # translate the filler list to a single entry that is a disjunction
                disj = ObjectUnionOf(parents)
                parents = [disj]
            for parent in parents:
                if axiomType == SubClassOf:
                    axiom = SubClassOf(subj, parent)
                elif axiomType == ClassAssertion:
                    axiom = ClassAssertion(parent, subj)
                elif axiomType == ObjectPropertyAssertion:
                    axiom = ObjectPropertyAssertion(slot_uri, subj, parent)
                elif axiomType == AnnotationAssertion:
                    axiom = AnnotationAssertion(slot_uri, subj, parent)
                else:
                    raise Exception(f'Unknown: {axiomType}')
                o.axioms.append(axiom)
        return subj

    def _instance_of_linkml_class(self, v) -> bool:
        try:
            type(v).class_name
            return True
        except:
            return False

    def _lookup_slot(self, cls: ClassDefinition, field: str):
        for sn in cls.slots:
            s: SlotDefinition
            s = self.schema.slots[sn]
            if underscore(s.name) == field:
                return s
            if s.alias and underscore(s.alias) == field:
                return s
        logging.error(f'Did not find {field} in {cls.name} slots =  {cls.slots}')

    def _get_interpretations(self, x: Definition) -> Set[INTERPRETATION]:
        interps = set()
        OWL_MARKER = 'OWL>>'
        for c in x.comments:
            if c.startswith(OWL_MARKER):
                n = c.replace(OWL_MARKER, '').strip()
                interps.add(n)
        return interps

    def _get_IRI_str(self, id: str) -> str:
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
