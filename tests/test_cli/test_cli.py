import os
import unittest

from click.testing import CliRunner
from funowl.converters.functional_converter import to_python

from linkml_owl.dumpers import owl_dumper
from tests import INPUT_DIR, OUTPUT_DIR


class CliTestSuite(unittest.TestCase):
    """
    Tests command line interface.
    """

    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
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
        doc_rt = to_python(owl_out)
        axioms = doc_rt.ontology.axioms
        doc_expected = to_python(str(os.path.join(INPUT_DIR, 'monsters_and_magic.expected.ofn')))
        assert len(axioms) == len(doc_expected.ontology.axioms)
        self.assertCountEqual(axioms, doc_expected.ontology.axioms)


