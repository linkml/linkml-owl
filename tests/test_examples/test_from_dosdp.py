# -*- coding: utf-8 -*-
import os
import unittest

import pyhornedowl
from linkml_runtime.utils.schemaview import SchemaView

from linkml_owl.util.csv_converter import csv_to_objects
from tests.model.mondo_dps import *
from linkml_owl.dumpers.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""


SCHEMA_IN = os.path.join(MODEL_DIR, 'mondo_dps.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'vectorBorneDisease.tsv')
OWL_OUT = os.path.join(OUTPUT_DIR, 'vectorBorneDisease.owl.ofn')
OWLSCHEMA_OUT = os.path.join(OUTPUT_DIR, 'mondo_dps.owl.ttl')

class TestFromDosdp(unittest.TestCase):
    """A test case for create tests."""

    def test_as_owl(self):
        """
        Test creation of OWL metamodel
        """
        yd = YAMLGenerator(SCHEMA_IN)
        # schema = yd.schema
        with open(OWLSCHEMA_OUT, 'w') as stream:
            stream.write(OwlSchemaGenerator(SCHEMA_IN).serialize())

    def test_from_dosdp(self):
        """
        Test creation of an OWL TBox from Mondo DOSDP templates, converted to LinkML
        """
        sv = SchemaView(SCHEMA_IN)
        collection = csv_to_objects(DATA_IN, target_class=VectorBorneDiseaseTemplate, schemaview=sv)
        for obj in collection:
            print(obj)
        dumper = OWLDumper()
        dumper.schemaview = sv
        ofn_str = dumper.dumps(collection, schema=sv.schema, output_type="ofn")
        axioms = dumper.ontology.get_axioms()
        print(len(axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(ofn_str)
        # Verify roundtrip
        doc2 = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        print(len(doc2.get_axioms()))
        assert len(axioms) == len(doc2.get_axioms())