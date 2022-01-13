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
from funowl import Axiom, AnnotationAssertion, Literal, SubClassOf, ObjectSomeValuesFrom, \
    ObjectAllValuesFrom, ObjectUnionOf, EquivalentClasses, ObjectIntersectionOf, AnnotationValue

import os
from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

import unittest

SCHEMA_IN = os.path.join(INPUT_DIR, 'owl_dumper_test.yaml')
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
  PATO: http://purl.obolibrary.org/obo/PATO_
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
  
enums:
  ActivationStateEnum:
    permissible_values:
      ACTIVATED:
        meaning: PATO:0002354
      INACTIVATED:
        meaning: PATO:0002355
slots:
  id:
    identifier: true
    range: uriorcurie
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  definition:
    slot_uri: IAO:0000115
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  exactMatch:
    slot_uri: skos:exactMatch
    range: NamedThing
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
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
    #transitive: true
    range: NamedThing
    multivalued: true
  other_part_ofs:
    slot_uri: BFO:0000050
    range: NamedThing
    multivalued: true
  has_part:
    slot_uri: BFO:0000051
    range: NamedThing
    multivalued: true
    inverse: part_of
    
  subphenotype:
    range: Phenotype
  increased:
    is_a: subphenotype
  decreased:
    is_a: subphenotype
  abnormal:
    is_a: subphenotype
    
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
        annotations:
          owl: AnnotationAssertion
  ExactMatchAsLiteral:
    is_a: NamedThing
    slots:
      - exactMatch
    slot_usage:
      exactMatch:
        range: string
        required: true
        annotations:
          owl: AnnotationAssertion
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
      - other_part_ofs
    slot_usage:
      subclass_of:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
      part_of:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
      other_part_ofs:
        required: false
        description: for hidden GCIs
        annotations:
          owl: ObjectSomeValuesFrom
  ClassTemplateExample1:
    is_a: NamedThing
    slots:
      - subclass_of
      - part_of
      - other_part_ofs
    slot_usage:
      subclass_of:
        annotations:
          owl.fstring: SubClassOf({id} {V})
          
  ClassTemplateExample2:
    is_a: NamedThing
    slots:
      - subclass_of
      - part_of
      - other_part_ofs
    slot_usage:
      subclass_of:
        annotations:
          owl.template: |-
            {% for p in subclass_of %}SubClassOf({{id}} {{p}}){% endfor %} 
            
  CollectionOfParts:
    is_a: NamedThing
    slots:
      - has_part
    annotations:
      owl.template: |-
        {% for p in has_part %}
        SubClassOf( {{id}} ObjectSomeValuesFrom( BFO:0000051 {{p}} ) )
        {% endfor %}
        DisjointClasses(
           Annotation( rdfs:label "all parts of {{id}} are part-disjoint")
          {% for p in has_part %}
          ObjectSomeValuesFrom( BFO:0000050 {{p}} )
          {% endfor %}
        )
        
  DefinedCollectionOfParts:
    is_a: NamedThing
    slots:
      - has_part
    annotations:
      owl.template: |-
        EquivalentClasses( {{id}} 
                           ObjectIntersectionOf( 
                             {% for p in has_part %}
                               ObjectSomeValuesFrom( BFO:0000051 {{p}} )
                             {% endfor %}                           
                             ObjectAllValuesFrom( BFO:0000051
                                                  ObjectSomeValuesFrom( BFO:0000050
                                                    ObjectUnionOf( 
                                                    {% for p in has_part %}
                                                      ObjectSomeValuesFrom( BFO:0000051 {{p}} )
                                                    {% endfor %} )
                                                  )
                                                )
                           )
                         )
      
  PartWithCounts:
    is_a: Anonymous
    attributes:
      unit:
        range: NamedThing
        multivalued: false
        annotations:
          owl: SomeValuesFrom
      count:
        range: integer
        minimum_value: 1
        annotations:
          owl: HasValue
      state:
        range: ActivationStateEnum
        annotations:
          owl: SomeValuesFrom
      
  CollectionOfPartsWithCounts:
    is_a: NamedThing
    slots:
      - has_part
    slot_usage:
      has_part:
        range: PartWithCounts
        inlined: true
    annotations:
      owl.template: |-
        {% for p in has_part %}
        SubClassOf( {{id}} 
                    ObjectSomeValuesFrom( BFO:0000051 
                                          ObjectIntersectionOf( {{p.unit }}
                                                    ObjectSomeValuesFrom(RO:0000053 {{p.state.meaning}})
                                                    {% if p.count %}
                                                    DataHasValue(PATO:0001555 {{p.count}})
                                                    {% endif %}
                                                               ) 
                                                               
                                         ) 
                  )
        {% endfor %}
    
    
  Phenotype:
    is_a: NamedThing
    
  SizeTriad:
    slots:
      - increased
      - decreased
      - abnormal
    annotations:
      owl.template: |-
        {{increased.id}}
    
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
        sv = SchemaView(SCHEMA_IN)
        schema = sv.schema
        py_str = PythonGenerator(SCHEMA_IN).serialize()
        #print(py_str)
        py_mod = compile_python(py_str)

        md = "# linkml-owl Test Cases\n\n"
        md += 'These examples are generated automatically from test_owl_dumper\n\n'


        checks = []
        def add_check(*args, **kwargs):
            ch = Check(*args, **kwargs)
            ch.set_schema_section(sv)
            checks.append(ch)
        p1 = py_mod.PartWithCounts(unit='x:p1', count=2, state='ACTIVATED')
        p2 = py_mod.PartWithCounts(unit='x:p2', count=3, state='ACTIVATED')
        add_check("Parts collection with counts",
                  [py_mod.CollectionOfPartsWithCounts('x:collection',
                                                      has_part=[p1,
                                                                p2,
                                                                ])],
                  [],
                  """Demonstrates nesting
                  """)
        add_check("Parts collection",
                  [py_mod.CollectionOfParts('x:collection', has_part=['x:p1', 'x:p2'])],
                  [],
                  """Things that are made of an arbitrary list of parts
                  """)
        add_check("Defined parts collection",
                  [py_mod.DefinedCollectionOfParts('x:collection', has_part=['x:dp1', 'x:dp2'])],
                  [],
                  """Things that are defined exhaustively by an arbitrary list of parts
                  """)
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
        add_check("Hidden GCI",
                  [py_mod.EquivGenusAndPartOf('x:a',
                                              subclass_of=['X:genus'],
                                              part_of=['x:b'],
                                              other_part_ofs=['x:c'])],
                  [EquivalentClasses(X.a, ObjectIntersectionOf(X.genus,
                                                               ObjectSomeValuesFrom(BFO['0000050'],X.b))),
                   SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.c))],
                  """Demonstrates a case where some slots contribute to a logical definition (equiv axiom),
                     and other contribute to additional axioms (so called hidden GCIs)""")
        add_check("slot-value level fstring template",
                  [py_mod.ClassTemplateExample1('x:a', subclass_of='x:b')],
                  ["SubClassOf( x:a <http://example.org/b> )"],
                  """Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)""")
        add_check("slot-value level jinja template",
                  [py_mod.ClassTemplateExample2('x:a', subclass_of='x:b')],
                  ["SubClassOf( x:a x:b )"],
                  """Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)""")
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

            ontology_str_trimmed = str(doc).replace('\n', '')
            for axiom in check.axioms:
                print(f'TESTING FOR: {axiom}')
                if not isinstance(axiom, str):
                    assert axiom in doc.ontology.axioms
                else:
                    print(f'  LOOKING IN: {ontology_str_trimmed}')
                    assert axiom.replace(' ', '') in ontology_str_trimmed.replace(' ', '')
        with open(MD_OUT, 'w') as stream:
            stream.write(md)

