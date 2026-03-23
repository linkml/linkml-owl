# -*- coding: utf-8 -*-
import logging
import os

import pyhornedowl
import yaml
import unittest

from copy import deepcopy
from dataclasses import dataclass
from typing import List, Optional, Union

from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.index.object_index import ObjectIndex
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.schema_as_dict import schema_as_dict
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import RDFS, URIRef
from rdflib.namespace import Namespace, SKOS, DCTERMS
from linkml_owl.dumpers.owl_dumper import OWLDumper, Axiom
from pyhornedowl.model import AnnotationAssertion, Literal, SubClassOf, ObjectSomeValuesFrom, \
    ObjectAllValuesFrom, ObjectUnionOf, EquivalentClasses, ObjectIntersectionOf, Annotation, SimpleLiteral, \
    AnnotationProperty, IRI, AnnotatedComponent, ObjectProperty

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
                s.alias = None
                s.domain_of = None
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

        This also generates the file ./tests/output/owl_dumper_test.md
        """
        X = Namespace("http://example.org/")
        BFO = Namespace("http://purl.obolibrary.org/obo/BFO_")
        IAO = Namespace("http://purl.obolibrary.org/obo/IAO_")
        RO = Namespace("http://purl.obolibrary.org/obo/RO_")
        SCHEMA = Namespace("http://schema.org/")
        dumper = OWLDumper()
        sv = SchemaView(SCHEMA_IN)
        schema = sv.schema
        py_str = PythonGenerator(SCHEMA_IN).serialize()
        # print(py_str)
        py_mod = compile_python(py_str)

        ont = pyhornedowl.PyIndexedOntology()
        for ns in [X, BFO, IAO, RO, SCHEMA]:
            ont.add_prefix_mapping(ns.prefix, str(ns))

        md = "# linkml-owl Test Cases\n\n"
        md += 'These examples are generated automatically from test_owl_dumper\n\n'
        md += 'For the complete schema, see [owl_dumper_test.yaml](https://github.com/linkml/linkml-owl/blob/main/tests/inputs/owl_dumper_test.yaml)\n\n'

        checks = []
        def add_check(*args, **kwargs):
            ch = Check(*args, **kwargs)
            ch.set_schema_section(sv)
            checks.append(ch)

        def ann(prop: URIRef, value: Union[SimpleLiteral, IRI]) -> Annotation:
            ap = AnnotationProperty(ont.iri(str(prop)))
            return Annotation(ap, value)

        x_a = ont.iri(X.a)
        assert str(x_a) == "http://example.org/a"
        assert isinstance(x_a, IRI)
        #assert x_a == IRI.parse("http://example.org/a")
        x_b = ont.iri(X.b)
        x_c = ont.iri(X.c)
        x_new = ont.iri(X.NewClass)
        x_src = ont.iri(X.src)
        x_src1 = ont.iri(X.src1)
        x_src2 = ont.iri(X.src2)
        part_of = ObjectProperty(ont.iri(BFO['0000050']))
        x_a_cls = ont.clazz(str(x_a))
        x_b_cls = ont.clazz(str(x_b))
        x_c_cls = ont.clazz(str(x_c))
        x_genus_cls = ont.clazz(str(ont.iri(X.genus)))
        x_new_cls = ont.clazz(str(ont.iri(X.NewClass)))
        x_in_cls = ont.clazz(str(ont.iri(X.IN)))
        x_h_cls = ont.clazz(str(ont.iri(X.H)))

        # Disease-related IRIs
        disease_location = ObjectProperty(ont.iri(RO['0004026']))
        has_phenotype = ObjectProperty(ont.iri(RO['0002200']))
        x_cancer_cls = ont.clazz(str(ont.iri(X.Cancer)))
        x_lung_cancer_cls = ont.clazz(str(ont.iri(X.LungCancer)))
        x_lung_cls = ont.clazz(str(ont.iri(X.Lung)))
        x_disease_cls = ont.clazz(str(ont.iri(X.Disease)))
        x_brain_disease_cls = ont.clazz(str(ont.iri(X.BrainDisease)))
        x_brain_cls = ont.clazz(str(ont.iri(X.Brain)))
        x_tremor_cls = ont.clazz(str(ont.iri(X.Tremor)))
        x_parkinsonism_cls = ont.clazz(str(ont.iri(X.Parkinsonism)))
        x_nsd_cls = ont.clazz(str(ont.iri(X.NervousSystemDisorder)))
        x_brain_neuropathy_cls = ont.clazz(str(ont.iri(X.BrainNeuropathy)))
        x_neuropathy_cls = ont.clazz(str(ont.iri(X.Neuropathy)))

        add_check("Annotation using literals",
                  [py_mod.NamedThing('x:a', label='foo')],
                  [AnnotationAssertion(x_a, ann(RDFS.label, SimpleLiteral("foo")))],
                  """Default is to use an annotation assertion,
                  and if the range is a string then this is literal""")
        add_check("Annotation using IRIs",
                  [py_mod.NamedThingWithMatches('x:a', exactMatch='x:b')],
                  [AnnotationAssertion(x_a, ann(SKOS.exactMatch, x_b))],
                  "As above, but if the range is an instance of a LinkML class then use a literal")
        add_check("Annotation using forced literals",
                  [py_mod.NamedThingWithMatchesAsLiterals('x:a', exactMatch='x:b')],
                  [AnnotationAssertion(x_a, ann(SKOS.exactMatch, SimpleLiteral("x:b")))],
                  "We can force a literal by imposing a range")
        add_check("Axiom annotation with Literal value on annotation axiom",
                  [py_mod.DefinitionWithAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                        definition_source=['Me'])],
                  [AnnotatedComponent(AnnotationAssertion(x_a, ann(IAO['0000115'], SimpleLiteral("a foo is a foo"))),
                                      {ann(DCTERMS.source, SimpleLiteral("Me"))})],
                  """Axiom annotations (literals) can be driven by a separate slot""")
        add_check("Axiom annotation with IRI val on annotation axiom",
                  [py_mod.DefinitionWithIRIAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                           definition_source=['x:src'])],
                  [AnnotatedComponent(AnnotationAssertion(x_a, ann(IAO['0000115'], SimpleLiteral("a foo is a foo"))),
                                      {ann(DCTERMS.source, x_src)})],
                  """Axiom annotations (IRIs) can be driven by a separate slot""")
        add_check("Axiom annotations with IRI val on annotation axiom",
                  [py_mod.DefinitionWithIRIAxiomAnnotation('x:a', label='foo', definition='a foo is a foo',
                                                           definition_source=['x:src1', 'x:src2'])],
                    [AnnotatedComponent(AnnotationAssertion(x_a, ann(IAO['0000115'], SimpleLiteral("a foo is a foo"))),
                                        {ann(DCTERMS.source, x_src1),
                                         ann(DCTERMS.source, x_src2)})],
                  """Multiple axiom annotations""")
        add_check("Basic SubClassOf between named classes",
                  [py_mod.Child('x:a', subclass_of='x:b')],
                  [SubClassOf(x_a_cls, x_b_cls)],
                  """Adding SubClassOf annotation to the linkml class forces a SubClass axiom""")
        add_check("basic direct equivalence between named classes",
                  [py_mod.DirectEquivalent('x:a', equivalent_to='x:b')],
                  [EquivalentClasses([x_a_cls, x_b_cls])],
                  "Adding EquivalentTo annotation to the linkml class forces an EquivalentClass axiom")
        #add_check("n-ary equivalence between named classes",
        #           [py_mod.DirectEquivalent('x:a', equivalent_to=['x:b', 'x:c'])],
        #          [EquivalentClasses(X.a, X.b, X.c)],
        #          "n-ary equivalence between named classes")
        add_check("SubClassOf SomeValuesFrom",
                  [py_mod.Part('x:a', part_of='x:b')],
                  [SubClassOf(x_a_cls, ObjectSomeValuesFrom(part_of, x_b_cls))],
                  """A SubClassOf annotation makes the annotation type be subclass,
                  a SomeValuesFrom annotation makes the slot interpreted as an existential""")
        add_check("SubClassOf AllValuesFrom",
                  [py_mod.PartOnly('x:a', part_of='x:b')],
                  [SubClassOf(x_a_cls, ObjectAllValuesFrom(part_of, x_b_cls))],
                  "As above, but with universal restrictions")
        add_check("SubClassOf DataHasValue",
                  [py_mod.HasName('x:a', has_name='Violet')],
                  #[SubClassOf(X.a, DataHasValue(SCHEMA['has_name'], Literal('Violet')))],
                  [],
                  "SubClassOf DataHasValue")
        add_check("SubClassOf SomeValuesFrom plus label",
                  [py_mod.Part('x:a', label='foo', part_of='x:b')],
                  [AnnotationAssertion(x_a, ann(RDFS.label, SimpleLiteral("foo"))),
                   SubClassOf(x_a_cls, ObjectSomeValuesFrom(part_of, x_b_cls))],
                  """Demonstrates a mix of slots, some annotation, some logical""")
        #anon_part_of = py_mod.AnonPartOf(part_of='x:b')
        #o = py_mod.ChildOfAnon('x:a', subclass_of_anon=[anon_part_of])
        #add_check("SubClassOf SomeValuesFrom nested",
        #          [o],
        #          [SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.b))],
        #          "")
        #          #[SubClassOf(X.a, ObjectSomeValuesFrom(BFO['0000050'], X.b))],
        #          [],
        #          "create a subClassOf-partOf-some using a nested structure")
        # NOTE: assumes order-preserving
        add_check("SubClassOf Union",
                  [py_mod.ChildOfUnion('x:a', subclass_of=['x:b', 'x:c'])],
                  [SubClassOf(x_a_cls, ObjectUnionOf([x_b_cls, x_c_cls]))],
                  """The slot is interpreted as a parent class,
                  and all slot values with a UnionOf annotation are collected to make a UnionOf expression""")
        add_check("EquivalentTo Union",
                  [py_mod.EquivUnion('x:a', operands=['x:b', 'x:c'])],
                  [EquivalentClasses([x_a_cls, ObjectUnionOf([x_b_cls, x_c_cls])])],
                  "As above, but with equivalence")
        #add_check("DisjointUnion",
        #          [py_mod.DisjointUnion('x:a', operands=['x:b', 'x:c'])],
        #          [DisjointUnion(X.a, X.b, X.c)],
        #          "As above, combining equivalence and disjointness into a single axiom")
        add_check("EquivalentTo IntersectionOf",
                  [py_mod.EquivIntersection('x:a', operands=['x:b', 'x:c'])],
                  [EquivalentClasses([x_a_cls, ObjectIntersectionOf([x_b_cls, x_c_cls])])],
                  """The slot is interpreted as a parent class,
                  and all slot values with a IntersectionOf annotation are collected to make a IntersectionOf expression""")
        add_check("EquivalentTo Genus and SomeValuesFrom",
                  [py_mod.EquivGenusAndPartOf('x:a',
                                              subclass_of=['X:genus'],
                                              part_of=['x:b', 'x:c'])],
                  [EquivalentClasses([x_a_cls, ObjectIntersectionOf([x_genus_cls,
                                                                     ObjectSomeValuesFrom(part_of, x_b_cls),
                                                                     ObjectSomeValuesFrom(part_of, x_c_cls)])])],
                  """All slot value interpretations are collected into a single IntersectionOf""")
        add_check("EquivalentTo Genus and SomeValuesFrom with AutoLabel",
                  [py_mod.EquivGenusAndPartOfWithAutoLabel('x:NewClass',
                                                           part='x:IN',
                                                           whole='x:H'),
                   py_mod.NamedThing('x:IN', label='interneuron'),
                   py_mod.NamedThing('x:H', label='hippocampus')],
                  [AnnotationAssertion(x_new, ann(RDFS.label, SimpleLiteral('interneuron of hippocampus'))),
                   EquivalentClasses([x_new_cls, ObjectIntersectionOf([x_in_cls,
                                                                       ObjectSomeValuesFrom(part_of, x_h_cls)])])],
                  """Label auto-added using string_serialization""")
        add_check("EquivalentTo IntersectionOf with axiom annotation",
                  [py_mod.EquivIntersectionWithAxiomAnnotation('x:a', operands=['x:b', 'x:c'],
                                                               logical_definition_source=["Me"])],
                  [AnnotatedComponent(EquivalentClasses([x_a_cls, ObjectIntersectionOf([x_b_cls, x_c_cls])]),
                                {ann(DCTERMS.source, SimpleLiteral("Me"))})],
                  """as above, with axiom annotation""")
        #add_check("EquivalentTo with Singleton IntersectionOf",
        #          [py_mod.EquivGenusAndPartOf('x:a',
        #                                      subclass_of=['X:genus'],
        #                                      part_of=[])],
        #          [EquivalentClasses(X.a, X.genus)],
        #          """An IntersectionOf with one element is converted to a singleton""")
        add_check("Hidden GCI",
                  [py_mod.EquivGenusAndPartOf('x:a',
                                              subclass_of=['X:genus'],
                                              part_of=['x:b'],
                                              other_part_ofs=['x:c'])],
                  [EquivalentClasses([x_a_cls, ObjectIntersectionOf([x_genus_cls,
                                                                     ObjectSomeValuesFrom(part_of, x_b_cls)])]),
                   SubClassOf(x_a_cls, ObjectSomeValuesFrom(part_of, x_c_cls))],
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
        p1 = py_mod.PartWithCounts2(unit='x:p1', count=2, state='ACTIVATED')
        p2 = py_mod.PartWithCounts2(unit='x:p2', count=3, state='ACTIVATED')
        add_check("Parts collection with counts v2",
                  [py_mod.CollectionOfPartsWithCounts2('x:collection',
                                                       has_part=[p1,
                                                                 p2,
                                                                 ])],
                  [],
                  """Demonstrates tr function
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
        add_check("Disease SubClassOf hierarchy",
                  [py_mod.DiseaseClass('x:LungCancer', label='lung cancer', subclass_of='x:Cancer'),
                   py_mod.NamedThing('x:Cancer', label='cancer')],
                  [SubClassOf(x_lung_cancer_cls, x_cancer_cls),
                   AnnotationAssertion(ont.iri(X.LungCancer), ann(RDFS.label, SimpleLiteral("lung cancer")))],
                  """A simple disease hierarchy using named SubClassOf parents,
                     e.g. 'lung cancer SubClassOf cancer'""")
        add_check("Disease defined by anatomical location",
                  [py_mod.DiseaseByLocation('x:BrainDisease',
                                            label='brain disease',
                                            subclass_of='x:NervousSystemDisorder',
                                            disease_location='x:Brain')],
                  [EquivalentClasses([x_brain_disease_cls,
                                      ObjectIntersectionOf([x_nsd_cls,
                                                            ObjectSomeValuesFrom(disease_location, x_brain_cls)])])],
                  """A disease defined by genus (nervous system disorder) and
                     anatomical location differentia (brain), following the
                     Mondo disease_by_location design pattern""")
        add_check("Disease defined by phenotype",
                  [py_mod.DiseaseByPhenotype('x:Parkinsonism',
                                             label='parkinsonism',
                                             subclass_of='x:Disease',
                                             has_phenotype='x:Tremor')],
                  [EquivalentClasses([x_parkinsonism_cls,
                                      ObjectIntersectionOf([x_disease_cls,
                                                            ObjectSomeValuesFrom(has_phenotype, x_tremor_cls)])])],
                  """A disease defined by an associated phenotype,
                     e.g. 'parkinsonism EquivalentTo disease AND has-phenotype some tremor'""")
        add_check("Disease defined by location and phenotype",
                  [py_mod.DefinedDisease('x:BrainNeuropathy',
                                          label='brain neuropathy',
                                          subclass_of='x:Neuropathy',
                                          disease_location='x:Brain',
                                          has_phenotype='x:Tremor')],
                  [EquivalentClasses([x_brain_neuropathy_cls,
                                      ObjectIntersectionOf([x_neuropathy_cls,
                                                            ObjectSomeValuesFrom(disease_location, x_brain_cls),
                                                            ObjectSomeValuesFrom(has_phenotype, x_tremor_cls)])])],
                  """A disease defined by both location and phenotype in a single intersection,
                     illustrating multiple differentiae in one EquivalentClasses axiom""")
        for check in checks:
            #print(f'** CHECK: {check.title}')
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
            container = py_mod.Container(entities=check.records)
            dumper.object_index = ObjectIndex(container, schemaview=sv)
            dumper.autofill = True
            # print(f"RECORDS = {check.records}")
            doc = dumper.to_ontology_document(check.records, schema)
            doc.save_to_file("/tmp/tmp.owl", "ofn")
            ontology_str = doc.save_to_string("ofn")
            md += '\n__Generated axioms__:\n\n'
            md += f'```\n{ontology_str}\n```\n\n'
            for axiom in doc.get_axioms():
                logging.info(f'GENERATED: {axiom}')

            ontology_str_trimmed = ontology_str.replace('\n', '')
            generated_axioms = doc.get_axioms()
            for axiom in doc.get_axioms():
                if isinstance(axiom, AnnotatedComponent):
                    if len(axiom.ann) == 0:
                        generated_axioms.append(axiom.component)
            for axiom in check.axioms:
                # print(f'TESTING FOR: {axiom}')
                if not isinstance(axiom, str):
                    s = ""
                    if axiom not in generated_axioms:
                        logging.error(f'COULD NOT FIND: {axiom}')
                        for a in generated_axioms:
                            logging.error(f'   HAS: {a}')
                            s += f'{a}\n'
                    self.assertIn(axiom, generated_axioms, f"Could not find among {len(generated_axioms)} axioms // {s}")
                else:
                    # print(f'  LOOKING IN: {ontology_str_trimmed}')
                    assert axiom.replace(' ', '') in ontology_str_trimmed.replace(' ', '')
        with open(MD_OUT, 'w') as stream:
            stream.write(md)

