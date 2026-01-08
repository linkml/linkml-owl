# -*- coding: utf-8 -*-
import os
import unittest

import pyhornedowl
from tests.model.chromschema import *
from linkml_owl.dumpers.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator

from linkml_runtime.loaders import yaml_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

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
        dumper = OWLDumper()
        ofn_str = dumper.dumps(collection, schema=schema, output_type="ofn")
        axioms = dumper.ontology.get_axioms()
        print(len(axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(ofn_str)
        doc2 = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        print(len(doc2.get_axioms()))
        assert len(axioms) == len(doc2.get_axioms())
