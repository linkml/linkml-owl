# -*- coding: utf-8 -*-
from rdflib import Graph
from tests.model.chromschema import *
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
import json
from funowl.converters.functional_converter import to_python
from funowl import OntologyDocument


from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader

import os
from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

import unittest

SCHEMA_IN = os.path.join(MODEL_DIR, 'chromo.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'hg38_mini.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'hg38_mini.owl.ofn')
OWLSCHEMA_OUT = os.path.join(OUTPUT_DIR, 'chromo.schema.owl.ttl')

class TestCreate(unittest.TestCase):
    """A test case for create tests."""

    def test_create_ontology(self):
        """
        Test creation of an OWL TBox

        Uses monochrom schema as guiding templates, and
        chrosomome data in yaml as source for classes
        """
        yd = YAMLGenerator(SCHEMA_IN)
        schema = yd.schema
        with open(OWLSCHEMA_OUT, 'w') as stream:
            stream.write(OwlSchemaGenerator(SCHEMA_IN).serialize())
        collection = yaml_loader.load(DATA_IN, ChromosomePartCollection)
        #collection = ChromosomePartCollection()
        #c1 = ChromosomePart(id='chr1')
        #collection.has = [c1]
        dumper = OWLDumper()
        doc = dumper.to_ontology_document(collection, schema)
        print(len(doc.ontology.axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))
        doc2: OntologyDocument
        doc2 = to_python(OWL_OUT)
        print(len(doc2.ontology.axioms))
        assert len(doc.ontology.axioms) == len(doc2.ontology.axioms)
