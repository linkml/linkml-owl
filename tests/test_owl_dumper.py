# -*- coding: utf-8 -*-
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Optional

import yaml
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.schema_as_dict import schema_as_dict
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import Graph, RDFS
from rdflib.namespace import Namespace, SKOS
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
import json
from funowl.converters.functional_converter import to_python
from funowl import OntologyDocument, Ontology, Axiom, AnnotationAssertion, Literal, SubClassOf, ObjectSomeValuesFrom, \
    ObjectAllValuesFrom, ObjectUnionOf, EquivalentClasses, ObjectIntersectionOf, AnnotationValue

from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader

import os
from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

import unittest

SCHEMA_IN = os.path.join(MODEL_DIR, 'owl_dumper_test.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'owl_dumper_test.owl.ofn')
MD_OUT = os.path.join(OUTPUT_DIR, 'owl_dumper_test.md')

SCHEMA = """
id: https://w3id.org/linkml/owl/tests
name: OwlTest
description: |-
  OWL Tests
imports:
  - linkml:types
prefixes:
  linkml: https://w3id.org/linkml/
  biolink: https://w3id.org/biolink/vocab/
  chromoschema: https://w3id.org/biodatamodels/chromoschema/
  gff: https://w3id.org/biodatamodels/gff/
  faldo: http://biohackathon.org/resource/faldo#
  CHR: http://purl.obolibrary.org/obo/CHR_
  SO: http://purl.obolibrary.org/obo/SO_
  GO: http://purl.obolibrary.org/obo/GO_
  BFO: http://purl.obolibrary.org/obo/BFO_
  RO: http://purl.obolibrary.org/obo/RO_
  NCBITaxon: http://purl.obolibrary.org/obo/NCBITaxon_
  edam: http://edamontology.org/
  refseq: http://identifiers.org/refseq/
  insdc: http://identifiers.org/insdc/
  ensembl: http://identifiers.org/ensembl/
  OIO: http://www.geneontology.org/formats/oboInOwl#
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  x: http://example.org/

default_prefix: chromoschema
default_curi_maps:
  - semweb_context
  
slots:
  id:
    identifier: true
  label:
    slot_uri: rdfs:label
  definition:
    slot_uri: IAO:0000115
  exactMatch:
    slot_uri: skos:exactMatch
    range: NamedThing
  equivalent_to:
    slot_uri: owl:equivalentClasses
    range: NamedThing
    multivalued: true
  subclass_of:
    slot_uri: rdfs:subclass_of
    range: NamedThing
    multivalued: true
  operands:
    range: NamedThing
    multivalued: true
  part_of:
    slot_uri: BFO:0000050
    range: NamedThing
    multivalued: true
    
classes:
  Thing:
  NamedThing:
    is_a: Thing
    slots:
      - id
      - label
  Anonymous:
    is_a: Thing
    annotations:
      owl: Class
  ExactMatch:
    is_a: NamedThing
    slots:
      - exactMatch
    slot_usage:
      exactMatch:
        required: true
  ExactMatchAsLiteral:
    is_a: NamedThing
    slots:
      - exactMatch
    slot_usage:
      exactMatch:
        range: string
        required: true
  Child:
    is_a: NamedThing
    slots:
      - subclass_of
    slot_usage:
      subclass_of:
        required: true
        annotations:
          owl: SubClassOf
  ChildOfAnon:
    is_a: NamedThing
    slots:
      - subclass_of
    slot_usage:
      subclass_of:
        range: AnonPartOf
        annotations:
          owl: SubClassOf
  DirectEquivalent:
    is_a: NamedThing
    slots:
      - equivalent_to
    slot_usage:
      equivalent_to:
        required: true
        annotations:
          owl: EquivalentClasses
  ChildOfUnion:
    is_a: NamedThing
    slots:
      - subclass_of
    slot_usage:
      subclass_of:
        required: true
        annotations:
          owl: SubClassOf, UnionOf
  EquivUnion:
    is_a: NamedThing
    slots:
      - operands
    slot_usage:
      operands:
        required: true
        annotations:
          owl: EquivalentClasses, UnionOf
  EquivIntersection:
    is_a: NamedThing
    slots:
      - operands
    slot_usage:
      operands:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
  Part:
    is_a: NamedThing
    slots:
      - part_of
    slot_usage:
      part_of:
        required: true
        annotations:
          owl: ObjectSomeValuesFrom
  PartOnly:
    is_a: NamedThing
    slots:
      - part_of
    slot_usage:
      part_of:
        required: true
        annotations:
          owl: ObjectAllValuesFrom
  AnonPartOf:
    is_a: Anonymous
    slots:
      - part_of
    slot_usage:
      part_of:
        required: true
        annotations:
          owl: ObjectSomeValuesFrom
    annotations:
      owl: Class
  EquivGenusAndPartOf:
    is_a: NamedThing
    slots:
      - subclass_of
      - part_of
    slot_usage:
      subclass_of:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
      part_of:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
    
"""

# TODO: move to schema_as_dict
def trim_yaml(obj):
    if isinstance(obj, dict):
        if 'owl' in obj:
            obj['owl'] = obj['owl']['value']
        for k in ['from_schema', 'owner']:
            if k in obj:
                del obj[k]
        for k, v in obj.items():
            trim_yaml(v)
    elif isinstance(obj, list):
        for v in obj:
            trim_yaml(v)

@dataclass
class Check:
    title: str
    records: List[YAMLRoot] = None
    axioms: List[Axiom] = None
    description: Optional[str] = None
    schema_section: str = None

    def set_schema_section(self, sv: SchemaView):
        """
        Used primarily for generating documentation
        """
        classes = set()
        for record in self.records:
            classes.add(type(record).__name__)
            #for k, v in vars(record).items():
        n = self.title.replace(' ', '-')
        schema = SchemaDefinition(id=f'http//example.org/{n}')
        for cn in classes:
            c = deepcopy(sv.get_class(cn))
            for s in sv.class_induced_slots(cn):
                c.attributes[s.name] = s
            schema.classes[c.name] = c
            c.slots = []
            c.slot_usage = {}
        obj = schema_as_dict(schema)
        trim_yaml(obj)
        del obj['name']
        del obj['default_prefix']
        del obj['prefixes']
        self.schema_section = yaml.dump(obj, default_flow_style=False, sort_keys=False)




class TestOwlDumper(unittest.TestCase):
    """A test case for create tests."""

    def test_owl_dumper(self):
        """
        Test OWLDumper
        """
        X = Namespace("http://example.org/")
        BFO = Namespace("http://purl.obolibrary.org/obo/BFO_")
        dumper = OWLDumper()
        sv = SchemaView(SCHEMA)
        schema = sv.schema
        py_str = PythonGenerator(SCHEMA).serialize()
        py_mod = compile_python(py_str)

        md = "# linkml-owl Test Cases\n\n"
        md += 'These examples are generated automatically from test_owl_dumper\n\n'


        checks = []
        def add_check(*args, **kwargs):
            ch = Check(*args, **kwargs)
            ch.set_schema_section(sv)
            checks.append(ch)
        add_check("Annotation using literals",
                  [py_mod.NamedThing('x:a', label='foo')],
                  [AnnotationAssertion(RDFS.label, X.a, Literal("foo"))],
                  """Default is to use an annotation assertion,
                  and if the range is a string then this is literal""")
        add_check("Annotation using IRIs",
                  [py_mod.ExactMatch('x:a', exactMatch='x:b')],
                  [AnnotationAssertion(SKOS.exactMatch, X.a, X.b)],
                  "As above, but if the range is an instance of a LinkML class then use a literal")
        add_check("Annotation using forced literals",
                  [py_mod.ExactMatchAsLiteral('x:a', exactMatch='x:b')],
                  [AnnotationAssertion(SKOS.exactMatch, X.a, Literal("x:b"))],
                  "We can force a literal by imposing a range")
        add_check("Basic SubClassOf between named classes",
                  [py_mod.Child('x:a', subclass_of='x:b')],
                  [SubClassOf(X.a, X.b)],
                  """Adding SubClassOf annotation to the linkml class forces a SubClass axiom
                  """)
        add_check("basic direct equivalence between named classes",
                  [py_mod.DirectEquivalent('x:a', equivalent_to='x:b')],
                  [EquivalentClasses(X.a, X.b)],
                  "Adding EquivalentTo annotation to the linkml class forces a SubClass axiom")
        #add_check("n-ary equivalence between named classes",
        #           [py_mod.DirectEquivalent('x:a', equivalent_to=['x:b', 'x:c'])],
        #          [EquivalentClasses(X.a, X.b, X.c)],
        #          "n-ary equivalence between named classes")
        add_check("SubClassOf SomeValuesFrom",
                  [py_mod.Part('x:a', part_of='x:b')],
                  [SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.b))],
                  """A SubClassOf annotation makes the annotation type be subclass,
                  a SomeValuesFrom annotation makes the slot interpreted as an existential""")
        add_check("SubClassOf AllValuesFrom",
                  [py_mod.PartOnly('x:a', part_of='x:b')],
                  [SubClassOf(X.a, ObjectAllValuesFrom(BFO['0000050'], X.b))],
                  "As above, but with universal restrictions")
        add_check("SubClassOf SomeValuesFrom plus label",
                  [py_mod.Part('x:a', label='foo', part_of='x:b')],
                  [AnnotationAssertion(RDFS.label, X.a, Literal("foo")),
                   SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.b))],
                  """Demonstrates a mix of slots, some annotation, some logical""")
        #add_check("SubClassOf SomeValuesFrom, nested",
        #          [py_mod.ChildOfAnon('x:a', subclass_of=py_mod.AnonPartOf(part_of='x:b'))],
        #          [SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.b))],
        #          "create a subClassOf-partOf-some using a nested structure")
        # NOTE: assumes order-preserving
        add_check("SubClassOf Union",
                  [py_mod.ChildOfUnion('x:a', subclass_of=['x:b', 'x:c'])],
                  [SubClassOf(X.a, ObjectUnionOf(X.b, X.c))],
                  """The slot is interpreted as a parent class,
                  and all slot values with a UnionOf annotation are collected to make a UnionOf expression""")
        add_check("EquivalentTo Union",
                  [py_mod.EquivUnion('x:a', operands=['x:b', 'x:c'])],
                  [EquivalentClasses(X.a, ObjectUnionOf(X.b, X.c))],
                  "As above, but with equivalence")
        add_check("EquivalentTo IntersectionOf",
                  [py_mod.EquivIntersection('x:a', operands=['x:b', 'x:c'])],
                  [EquivalentClasses(X.a, ObjectIntersectionOf(X.b, X.c))],
                  """The slot is interpreted as a parent class,
                  and all slot values with a IntersectionOf annotation are collected to make a IntersectionOf expression""")
        add_check("EquivalentTo Genus and SomeValuesFrom",
                  [py_mod.EquivGenusAndPartOf('x:a',
                                              subclass_of=['X:genus'],
                                              part_of=['x:b', 'x:c'])],
                  [EquivalentClasses(X.a, ObjectIntersectionOf(X.genus,
                                                               ObjectSomeValuesFrom(BFO['0000050'],X.b),
                                                               ObjectSomeValuesFrom(BFO['0000050'],X.c)))],
                  """All slot value interpretations are collected into a single IntersectionOf""")
        for check in checks:
            print(f'** CHECK: {check.title}')
            md += f'## {check.title}\n\n'
            md += f'\n__Description__: _{check.description}_\n\n'
            md += f'\n__Schema__:\n\n```yaml\n{check.schema_section}\n```\n\n'

            md += '\n__Input__:\n\n'
            for record in check.records:
                md += f'* {record}\n'
            doc = dumper.to_ontology_document(check.records, schema)
            md += '\n__Generated axioms__:\n\n'
            md += f'```\n{str(doc)}\n```\n\n'
            for axiom in doc.ontology.axioms:
                print(f'GENERATED: {axiom}')
                #md += f'* {to_python(axiom)}\n'

            for axiom in check.axioms:
                print(f'TESTING FOR: {axiom}')
                assert axiom in doc.ontology.axioms
        with open(MD_OUT, 'w') as stream:
            stream.write(md)

