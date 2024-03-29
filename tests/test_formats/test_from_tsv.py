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
        doc = dumper.to_ontology_document(data, schema=sv.schema)
        doc_rt = to_python(str(doc))
        axioms = doc_rt.ontology.axioms
        logging.info(f'AXIOMS={len(axioms)}')
        assert len(axioms) > 5
        expected_doc = to_python(str(OWL_IN_CHECK))
        self.assertCountEqual(expected_doc.ontology.axioms, axioms)
        data = load_structured_file(DATA_IMPLICIT_IN,
                                    target_class='EquivGenusAndPartOf', schemaview=sv, delimiter=',', python_module=python_module)
        dumper = OWLDumper()
        doc2 = dumper.to_ontology_document(data, schema=sv.schema)
        doc = _remove_prefixes_hack(str(doc))
        doc2 = _remove_prefixes_hack(str(doc2))
        self.assertEquals(doc2, doc)



