# -*- coding: utf-8 -*-
import logging
import os
import unittest

import pyhornedowl
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper

from tests import INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'pizza-model.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'pizza-data.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'pizza.ofn')
EXPECTED = os.path.join(INPUT_DIR, 'pizza.expected.ofn')


class TestPizza(unittest.TestCase):
    """Pizza Ontology test case."""

    def test_build_pizza_ontology(self):
        """
        Test creation of an OWL TBox using the pizza ontology.
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        data = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
        dumper = OWLDumper()
        dumper.schemaview = sv

        ofn_str = dumper.dumps(data, schema=sv.schema, output_type="ofn")
        axioms = dumper.ontology.get_axioms()
        for a in axioms:
            print(f'AXIOM={a}')
        with open(OWL_OUT, 'w') as stream:
            stream.write(ofn_str)
        doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        rt_axioms = doc_rt.get_axioms()
        logging.info(f'AXIOMS={len(rt_axioms)}')

