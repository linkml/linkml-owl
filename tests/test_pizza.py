# -*- coding: utf-8 -*-
import logging
import os
import json
import unittest
import pytest
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

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

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'pizza-model.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'pizza-data.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'pizza.ofn')
EXPECTED = os.path.join(INPUT_DIR, 'pizza.expected.ofn')




class TestPizza(unittest.TestCase):
    """Pizza Ontology test case."""

    def test_build_pizza_ontology(self):
        """
        Test creation of an OWL TBox
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        data = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
        dumper = OWLDumper()
        dumper.schemaview = sv

        doc = dumper.to_ontology_document(data, schema=sv.schema)
        for a in doc.ontology.axioms:
            print(f'AXIOM={a}')
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))
        doc_rt = to_python(str(doc))
        axioms = doc_rt.ontology.axioms
        logging.info(f'AXIOMS={len(axioms)}')
        #assert len(axioms) > 5
        # compare with expected output
        #doc_expected = to_python(str(EXPECTED))
        #assert len(axioms) == len(doc_expected.ontology.axioms)
        #self.assertCountEqual(axioms, doc_expected.ontology.axioms)

