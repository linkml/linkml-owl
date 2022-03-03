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
from linkml_runtime.loaders import yaml_loader, json_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'allen-brain.yaml')
#DATA_IN = os.path.join(INPUT_DIR, 'allen-brain-hba.json')
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
        print('Enums:')
        print(python_module.Laterality.IN_LEFT_SIDE_OF.meaning)
        print(python_module.Laterality["IN_LEFT_SIDE_OF"].meaning)
        print(python_module.Hemisphere["3"].text)
        region = python_module.BrainRegion(id=1, hemisphere_id="3")
        print(region)
        region = python_module.BrainRegion(id=1, hemisphere_id=3)
        #print(region)
        atlas = json_loader.loads(DATA_IN, target_class=python_module.Atlas)
        dumper = OWLDumper()
        doc = dumper.to_ontology_document(atlas, sv.schema)
        #print(len(doc.ontology.axioms))
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))