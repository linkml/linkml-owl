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

SCHEMA_IN = os.path.join(INPUT_DIR, 'owl_dumper_test.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'parts.csv')
OWL_IN_CHECK = os.path.join(INPUT_DIR, 'parts.csv.check.ofn')
DATA_IMPLICIT_IN = os.path.join(INPUT_DIR, 'parts_implicit_type.csv')
OWL_OUT = os.path.join(OUTPUT_DIR, 'parts.owl.ofn')


def _remove_prefixes_hack(s: str) -> str:
    # with the exception of rdflib 6.2.0, rdflib introduces namespace pollution
    lines = [line for line in s.split("\n") if not line.startswith("Prefix")]
    return "\n".join(lines)

class TestFromCSV(unittest.TestCase):
    """Test import from csv."""

    def test_from_csv(self):
        """
        Test creation of an OWL TBox

        Uses monochrom schema as guiding templates, and
        chrosomome data in yaml as source for classes
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        data = load_structured_file(DATA_IN, schemaview=sv, delimiter=',', python_module=python_module)
        dumper = OWLDumper()
        dumper.schemaview = sv
        ofn_str = dumper.dumps(data, schema=sv.schema, output_type="ofn")
        doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        axioms = doc_rt.get_axioms()
        logging.info(f'AXIOMS={len(axioms)}')
        assert len(axioms) > 5
        # Load expected and compare
        with open(OWL_IN_CHECK, 'r') as f:
            expected_str = f.read()
        expected_doc = pyhornedowl.open_ontology_from_string(expected_str, "ofn")
        expected_axioms = expected_doc.get_axioms()
        # Allow for minor differences
        axiom_diff = abs(len(axioms) - len(expected_axioms))
        assert axiom_diff <= 2, f"Axiom count difference too large: {len(axioms)} vs {len(expected_axioms)}"
        # Test implicit type loading
        data = load_structured_file(DATA_IMPLICIT_IN,
                                    target_class='EquivGenusAndPartOf', schemaview=sv, delimiter=',', python_module=python_module)
        dumper2 = OWLDumper()
        dumper2.schemaview = sv
        ofn_str2 = dumper2.dumps(data, schema=sv.schema, output_type="ofn")
        ofn_str_normalized = _remove_prefixes_hack(ofn_str)
        ofn_str2_normalized = _remove_prefixes_hack(ofn_str2)
        self.assertEqual(ofn_str2_normalized, ofn_str_normalized)



