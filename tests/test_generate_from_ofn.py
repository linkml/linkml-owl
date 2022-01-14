# -*- coding: utf-8 -*-
import os
import json
import pytest
import unittest

from linkml_runtime import SchemaView
from rdflib import Graph
from tests.model.chromschema import *
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
from funowl.converters.functional_converter import to_python
from funowl import OntologyDocument, Axiom, SubClassOf, Class
from rdflib.namespace import Namespace, SKOS

from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""


SCHEMA_IN = os.path.join(MODEL_DIR, 'chromo.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'hg38_mini.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'hg38_mini.owl.ofn')
OWLSCHEMA_OUT = os.path.join(OUTPUT_DIR, 'chromo.schema.owl.ttl')

class TestGen(unittest.TestCase):

    @pytest.mark.skip
    def test_gen(self):
        """
        Test creation of an OWL TBox

        Note that this test is largely redundant with test_owl_dumper, but the
        intent here is to provide a more unified example

        Uses monochrom schema as guiding templates, and
        chrosomome data in yaml as source for classes
        """
        sv = SchemaView(SCHEMA_IN)
        schema = sv.schema
        dumper = OWLDumper()
        X = Namespace('http://example.org/')

        def t(owl_str: str, expected: List[Axiom]):
            doc = dumper.parse_axioms_string(owl_str, schemaview=sv)
            #g = Graph()
            #doc.to_rdf(g)

            axioms = doc.ontology.axioms
            print(f'Axioms={axioms}')
            #self.assertCountEqual(axioms, expected)
        t("", [])
        t("SubClassOf( X:a X:b )", [SubClassOf(X.a, X.b)])
        t("SubClassOf( owl:Nothing owl:Thing )", [SubClassOf(X.a, X.b)])
        doc = dumper.parse_axioms_string("SubClassOf( X:a X:b )", sv)
        ax: SubClassOf = doc.ontology.axioms[0]
        su = ax.subClassExpression
        if isinstance(su, Class):
            print(f'SUB={su}')


