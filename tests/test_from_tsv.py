# -*- coding: utf-8 -*-
import os
import json
import unittest
import pytest

from rdflib import Graph

from linkml_owl.util.loader_wrapper import load_structured_file
from tests.model.chromschema import *
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
from funowl.converters.functional_converter import to_python
from funowl import OntologyDocument


from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

SCHEMA_IN = os.path.join(INPUT_DIR, 'owl_dumper_test.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'parts.csv')
OWL_OUT = os.path.join(OUTPUT_DIR, 'parts.owl.ofn')

class TestFromCSV(unittest.TestCase):
    """Test import from csv."""

    def test_from_csv(self):
        """
        Test creation of an OWL TBox

        Uses monochrom schema as guiding templates, and
        chrosomome data in yaml as source for classes
        """
        yd = YAMLGenerator(SCHEMA_IN)
        data = load_structured_file(DATA_IN, schema=SCHEMA_IN)
        dumper = OWLDumper()
        doc = dumper.to_ontology_document(data, schema)
