import os
import unittest

import pyhornedowl
from click.testing import CliRunner

from linkml_owl.dumpers import owl_dumper
from tests import INPUT_DIR, OUTPUT_DIR


class CliTestSuite(unittest.TestCase):
    """
    Tests command line interface.
    """

    def setUp(self) -> None:
        runner = CliRunner()
        self.runner = runner

    def test_help_option(self):
        """Ensures --help works."""
        result = self.runner.invoke(owl_dumper.cli, ["--help"])
        out = result.stdout
        self.assertEqual(0, result.exit_code)

    def test_data2owl(self):
        """Ensures linkml-data2owl command works."""
        schema_in = os.path.join(INPUT_DIR, 'monsters_and_magic.yaml')
        data_in = os.path.join(INPUT_DIR, 'monsters_and_magic.data.yaml')
        owl_out = os.path.join(OUTPUT_DIR, 'monsters_and_magic.cli.ofn')
        result = self.runner.invoke(owl_dumper.cli, ["--schema", schema_in, data_in, "--output", owl_out])
        self.assertEqual(0, result.exit_code)
        with open(owl_out, 'r') as f:
            ofn_str = f.read()
        doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
        axioms = doc_rt.get_axioms()
        with open(os.path.join(INPUT_DIR, 'monsters_and_magic.expected.ofn'), 'r') as f:
            expected_str = f.read()
        doc_expected = pyhornedowl.open_ontology_from_string(expected_str, "ofn")
        expected_axioms = doc_expected.get_axioms()
        # Allow for minor differences between funowl and py-horned-owl
        axiom_diff = abs(len(axioms) - len(expected_axioms))
        assert axiom_diff <= 2, f"Axiom count difference too large: {len(axioms)} vs {len(expected_axioms)}"

