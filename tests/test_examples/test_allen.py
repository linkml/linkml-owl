"""Test the module can be imported."""
import os
import unittest
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

from linkml_owl.dumpers.owl_dumper import OWLDumper

from linkml_runtime.loaders import json_loader

from tests import INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'allen-brain.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'allen-brain-hba-truncated.json')
OWL_OUT = os.path.join(OUTPUT_DIR, 'allen-brain-hba.ofn')

class TestAllenBrain(unittest.TestCase):
    """
    Allen Brain Ontology test case.

    https://github.com/obophenotype/ABA_Uberon/issues/9
    """

    def test_brain_atlas_ontology(self):
        """
        Test creation of an OWL TBox
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        self.assertEqual("http://purl.obolibrary.org/obo/BSPO_0000120", python_module.Laterality.IN_LEFT_SIDE_OF.meaning)
        self.assertEqual("http://purl.obolibrary.org/obo/BSPO_0000120", python_module.Laterality["IN_LEFT_SIDE_OF"].meaning)
        self.assertEqual("3", python_module.Hemisphere["3"].text)
        region = python_module.BrainRegion(id=1, hemisphere_id="3")
        self.assertEqual("1", region.id)
        self.assertEqual(3, region.hemisphere_id)
        region = python_module.BrainRegion(id=1, hemisphere_id=3)
        self.assertEqual("1", region.id)
        self.assertEqual(3, region.hemisphere_id)
        atlas = json_loader.loads(DATA_IN, target_class=python_module.Atlas)
        dumper = OWLDumper()
        doc = dumper.to_ontology_document(atlas, sv.schema)
        #print(len(doc.ontology.axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))