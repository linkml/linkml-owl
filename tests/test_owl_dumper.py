# -*- coding: utf-8 -*-
import logging
import os
import yaml
import pytest
import unittest

from copy import deepcopy
from dataclasses import dataclass
from typing import List, Optional

from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.schema_as_dict import schema_as_dict
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import RDFS
from rdflib.namespace import Namespace, SKOS, DCTERMS
from linkml_owl.owl_dumper import OWLDumper
from funowl import Axiom, AnnotationAssertion, Literal, SubClassOf, ObjectSomeValuesFrom, \
    ObjectAllValuesFrom, ObjectUnionOf, EquivalentClasses, ObjectIntersectionOf, Annotation

from linkml_owl.util.trim_yaml import trim_yaml
from tests import INPUT_DIR, OUTPUT_DIR


SCHEMA_IN = os.path.join(INPUT_DIR, 'owl_dumper_test.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'owl_dumper_test.owl.ofn')
MD_OUT = os.path.join(OUTPUT_DIR, 'owl_dumper_test.md')

@dataclass
class Check:
    """
    A check for a particular OWL mapping construct
    """
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
    """Tests full functionality of OWL dumper"""

    def test_get_interpretations(self):
        dumper = OWLDumper()
        sv = SchemaView(SCHEMA_IN)
        schema = sv.schema
        #dumper._get_inferred_slot_annotations()


    def test_owl_dumper(self):
        """
        Test OWLDumper
        """
        X = Namespace("http://example.org/")
        BFO = Namespace("http://purl.obolibrary.org/obo/BFO_")
        IAO = Namespace("http://purl.obolibrary.org/obo/IAO_")
        dumper = OWLDumper()
        sv = SchemaView(SCHEMA_IN)
        schema = sv.schema
        py_str = PythonGenerator(SCHEMA_IN).serialize()
        #print(py_str)
        py_mod = compile_python(py_str)

        md = "# linkml-owl Test Cases\n\n"
        md += 'These examples are generated automatically from test_owl_dumper\n\n'
        md += 'For the complete schema, see tests/input/owl_dumper_test.yaml\n\n'


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
        add_check("Axiom annotation with Literal value on annotation axiom",
                  [py_mod.DefinitionWithAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                        definition_source=['Me'])],
                  [AnnotationAssertion(IAO['0000115'], X.a, Literal("a foo is a foo"), [
                      Annotation(DCTERMS.source, Literal("Me"))
                  ])],
                  """Axiom annotations (literals) can be driven by a separate slot""")
        add_check("Axiom annotation with IRI val on annotation axiom",
                  [py_mod.DefinitionWithIRIAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                           definition_source=['x:src'])],
                  [AnnotationAssertion(IAO['0000115'], X.a, Literal("a foo is a foo"), [
                      Annotation(DCTERMS.source, X.src)
                  ])],
                  """Axiom annotations (IRIs) can be driven by a separate slot""")
        add_check("Axiom annotations with IRI val on annotation axiom",
                  [py_mod.DefinitionWithIRIAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                           definition_source=['x:src1', 'x:src2'])],
                  [AnnotationAssertion(IAO['0000115'], X.a, Literal("a foo is a foo"), [
                      Annotation(DCTERMS.source, X.src1),
                      Annotation(DCTERMS.source, X.src2)
                  ])],
                  """Multiple axiom annotations""")
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
        add_check("EquivalentTo IntersectionOf with axiom annotation",
                  [py_mod.EquivIntersectionWithAxiomAnnotation('x:a', operands=['x:b', 'x:c'], logical_definition_source=["Me"])],
                  [EquivalentClasses(X.a, ObjectIntersectionOf(X.b, X.c),
                                     annotations=[Annotation(DCTERMS.source, Literal("Me"))])],
                  """as above, with axiom annotation""")
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
        add_check("Hidden GCI with axiom annotations",
                  [py_mod.EquivGenusAndPartOfWithAxiomAnnotation('x:a',
                                              label='a',
                                              definition='A X:genus that part_of some x:b',
                                              definition_source=['Auto'],
                                              subclass_of=['X:genus'],
                                              part_of=['x:b'],
                                              logical_definition_source=['Me'],
                                              other_part_ofs=['x:c'],
                                              axiom_source=['Auto'])],
                  [],  # TODO
                  """End-to-end example with hidden GCIs and different axiom annotations""")
        add_check("slot-value level fstring template",
                  [py_mod.ClassTemplateExample1('x:a', subclass_of='x:b')],
                  #[SubClassOf(X.a, X.b)],
                  ["SubClassOf( x:a x:b )"],
                  """Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)""")
        add_check("slot-value level jinja template",
                  [py_mod.ClassTemplateExample2('x:a', subclass_of='x:b')],
                  ["SubClassOf( x:a x:b )"],
                  #[SubClassOf(X.a, X.b)],
                  """Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)""")
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
        for check in checks:
            print(f'** CHECK: {check.title}')
            md += f'## {check.title}\n\n'
            md += f'\n__Description__: _{check.description}_\n\n'
            md += f'\n__Schema__:\n\n```yaml\n{check.schema_section}\n```\n\n'

            md += '\n__Input__:\n\n```yaml\n'
            for record in check.records:
                md += f'-\n'
                yaml_str = yaml_dumper.dumps(record)
                for line in yaml_str.split('\n'):
                    md += f'  {line}\n'
            md += '```\n'
            doc = dumper.to_ontology_document(check.records, schema)
            md += '\n__Generated axioms__:\n\n'
            md += f'```\n{str(doc)}\n```\n\n'
            for axiom in doc.ontology.axioms:
                logging.info(f'GENERATED: {axiom}')
                #md += f'* {to_python(axiom)}\n'

            ontology_str_trimmed = str(doc).replace('\n', '')
            for axiom in check.axioms:
                print(f'TESTING FOR: {axiom}')
                if not isinstance(axiom, str):
                    if axiom not in doc.ontology.axioms:
                        logging.error(f'COULD NOT FIND: {axiom}')
                        for a in doc.ontology.axioms:
                            logging.error(f'   HAS: {a}')
                    assert axiom in doc.ontology.axioms
                else:
                    print(f'  LOOKING IN: {ontology_str_trimmed}')
                    assert axiom.replace(' ', '') in ontology_str_trimmed.replace(' ', '')
        with open(MD_OUT, 'w') as stream:
            stream.write(md)

