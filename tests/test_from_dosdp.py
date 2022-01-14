# -*- coding: utf-8 -*-
import os
import json
import pytest
import unittest

from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph

from linkml_owl.util.csv_converter import csv_to_objects
from tests.model.mondo_dps import *
from linkml_owl.owl_dumper import OWLDumper
from linkml.generators.yamlgen import YAMLGenerator
from linkml.generators.owlgen import OwlSchemaGenerator
from funowl.converters.functional_converter import to_python
from funowl import OntologyDocument


from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper
from linkml_runtime.loaders import csv_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""


SCHEMA_IN = os.path.join(MODEL_DIR, 'mondo_dps.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'vectorBorneDisease.tsv')
OWL_OUT = os.path.join(OUTPUT_DIR, 'vectorBorneDisease.owl.ofn')
OWLSCHEMA_OUT = os.path.join(OUTPUT_DIR, 'mondo_dps.owl.ttl')

class TestFromDosdp(unittest.TestCase):
    """A test case for create tests."""

    @pytest.mark.skip
    def test_as_owl(self):
        """
        Test creation of OWL metamodel
        """
        yd = YAMLGenerator(SCHEMA_IN)
        schema = yd.schema
        with open(OWLSCHEMA_OUT, 'w') as stream:
            stream.write(OwlSchemaGenerator(SCHEMA_IN).serialize())

    @pytest.mark.skip
    def test_from_dosdp(self):
        """
        Test creation of an OWL TBox from Mondo DOSDP templates, converted to LinkML
        """
        sv = SchemaView(SCHEMA_IN)
        collection = csv_to_objects(DATA_IN, target_class=VectorBorneDiseaseTemplate, schemaview=sv)
        for obj in collection:
            print(obj)
        #collection = csv_loader.load(DATA_IN, target_class=VectorBorneDiseaseTemplate, schema=schema)
        dumper = OWLDumper()
        doc = dumper.to_ontology_document(collection, sv.schema)
        print(len(doc.ontology.axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))
        doc2: OntologyDocument
        doc2 = to_python(OWL_OUT)
        print(len(doc2.ontology.axioms))
        assert len(doc.ontology.axioms) == len(doc2.ontology.axioms)