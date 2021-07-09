import json
from typing import Optional, List, Set, Any
from dataclasses import dataclass
import logging

from rdflib import URIRef

from hbreader import hbread
from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition
from linkml_runtime.utils.formatutils import underscore, camelcase

from funowl import OntologyDocument, Ontology, IRI, ObjectSomeValuesFrom,\
    ObjectUnionOf, SubClassOf,\
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

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition, iri=None):
        o = Ontology(schema.id)
        self.ontology = o
        self.schema = schema
        #o.annotation(RDFS.label, name)
        doc = OntologyDocument(iri, o)
        self.transform(element, schema)
        return str(doc)

    def transform(self, element: YAMLRoot, schema: SchemaDefinition, is_element_an_object=True) -> Any:
        if element is None:
            logging.error('NONE')
            return None
        if not self._instance_of_linkml_class(element):
            #print(f'Atomic: {element}')
            # TODO: better way of detecting atoms
            if is_element_an_object:
                # foreign key
                return self._get_IRI_str(element)
            else:
                # literal
                return element
        o = self.ontology
        python_type = type(element)
        #print(f'E={element }PT={python_type}')
        linkml_class_name = python_type.class_name
        c = schema.classes[linkml_class_name]
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
            if slot is None:
                logging.error(f'No slot for {k}')
                continue
            if slot.identifier:
                continue
            slot_uri = self._get_IRI_str(slot.slot_uri)
            print(f'in {subj} {k} = {v} (URI={slot.slot_uri}) // slot = {slot.name}')
            interps = self._get_interpretations(slot)
            #print(f'Interps = {interps}')
            is_disjunction = 'UnionOf' in interps
            is_object_ref = slot.range in self.schema.classes

            # TODO: abstract this
            if isinstance(v, list):
                tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in v]
            elif isinstance(v, dict):
                tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in v.values()]
            else:
                tr_vals = [self.transform(v, schema, is_element_an_object=is_object_ref)]

            #print(f'Vals={tr_vals}')
            axiomType = SubClassOf
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
                    #o.subClassOf(subj, parent)
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

    def _get_interpretations(self, slot: SlotDefinition) -> Set[INTERPRETATION]:
        interps = set()
        OWL_MARKER = 'OWL>>'
        for c in slot.comments:
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





