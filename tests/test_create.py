# -*- coding: utf-8 -*-
from rdflib import Graph
from model.chromschema import *
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
import json

from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader

import os
from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

import unittest

SCHEMA_IN = os.path.join(MODEL_DIR, 'chromo.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'hg38_mini.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'hg38_mini.owl.ofn')

class TestCreate(unittest.TestCase):
    """A test case for create tests."""

    def test_create(self):
        yd = YAMLGenerator(SCHEMA_IN)
        schema = yd.schema
        collection = yaml_loader.load(DATA_IN, ChromosomePartCollection)
        #collection = ChromosomePartCollection()
        #c1 = ChromosomePart(id='chr1')
        #collection.has = [c1]
        dumper = OWLDumper()
        ont = dumper.dumps(collection, schema)
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(ont))