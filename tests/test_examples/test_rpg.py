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

SCHEMA_IN = os.path.join(INPUT_DIR, 'monsters_and_magic.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'monsters_and_magic.data.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'monsters_and_magic.ofn')
EXPECTED = os.path.join(INPUT_DIR, 'monsters_and_magic.expected.ofn')


class TestRolePlayGameExample(unittest.TestCase):
    """Test case using a fantasy RPG example.

    Note: the example data here is also an experiment in co-pilot assisted
    knowledge base generation; the majority of the content was created by
    LLM-autocomplete.
    """

    def test_build_rpg(self):
        """
        Test creation of an OWL TBox using RPG template.
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        data = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
        dumper = OWLDumper()
        dumper.schemaview = sv
        ofn_str = dumper.dumps(data, schema=sv.schema, output_type="ofn")
        with open(OWL_OUT, 'w') as stream:
            stream.write(ofn_str)
        doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        axioms = doc_rt.get_axioms()
        logging.info(f'AXIOMS={len(axioms)}')
        assert len(axioms) > 5
        # compare with expected output
        with open(EXPECTED, 'r') as f:
            expected_str = f.read()
        doc_expected = pyhornedowl.open_ontology_from_string(expected_str, "ofn")
        expected_axioms = doc_expected.get_axioms()
        # Allow for minor differences between funowl and py-horned-owl
        axiom_diff = abs(len(axioms) - len(expected_axioms))
        assert axiom_diff <= 2, f"Axiom count difference too large: {len(axioms)} vs {len(expected_axioms)}"

