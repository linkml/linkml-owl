# -*- coding: utf-8 -*-
import logging
import os
import unittest
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper
from funowl.converters.functional_converter import to_python

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
        doc = dumper.to_ontology_document(data, schema=sv.schema)
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))
        doc_rt = to_python(str(doc))
        axioms = doc_rt.ontology.axioms
        logging.info(f'AXIOMS={len(axioms)}')
        assert len(axioms) > 5
        # compare with expected output
        doc_expected = to_python(str(EXPECTED))
        self.assertEquals(len(axioms), len(doc_expected.ontology.axioms))
        self.assertCountEqual(axioms, doc_expected.ontology.axioms)

