# -*- coding: utf-8 -*-
import logging
import os
import unittest
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.loaders import yaml_loader

from linkml_owl.crossproducts.cross_product_generator import CrossProductGenerator
from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper
from funowl.converters.functional_converter import to_python

from tests import INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'laterality_model.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'laterality_data.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'laterality.ofn')
#EXPECTED = os.path.join(INPUT_DIR, 'pizza.expected.ofn')


class TestCrossProducts(unittest.TestCase):
    """XP test case."""

    def test_cross_products(self):
        """
        Test materialization of cross-products
        """
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        #lth = python_module.TaxonSpecificStructure(id='LeftThumbHomoSapiens', taxon_specific_forms={}, in_taxon='HomoSapiens', parent='LeftThumb')
        #obj = {'parent': 'Thumb', 'in_taxon': 'HomoSapiens', 'id': 'ThumbHomoSapiens', 'lateralized_forms': {'LeftThumbHomoSapiens': lth}}
        #python_module.TaxonSpecificStructure(**obj)


        data = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
        xpgen = CrossProductGenerator(schemaview=sv, python_model=python_module)
        nne = xpgen.materialize(data)
        print(f"Generated {nne} new elements")
        self.assertGreater(nne, 0)
        nne = xpgen.materialize(data)
        print(f"2nd iter Generated {nne} new elements")
        self.assertEqual(nne, 0)
        data_yaml = yaml_dumper.dumps(data)
        print(data_yaml)
        #data = yaml_loader.loads(data_yaml, target_class=python_module.Ontology)
        forelimb = data.structures["ForeLimb"]
        left_forelimb = forelimb.lateralized_forms["LeftForeLimb"]
        print(yaml_dumper.dumps(left_forelimb))
        left_hand = left_forelimb.parts["LeftHand"]
        left_pinky = left_hand.parts["LeftPinky"]
        self.assertEqual(left_pinky.parent, "Pinky")
        self.assertEqual(left_pinky.has_laterality, "Left")
        cat_forelimb = forelimb.taxon_specific_forms["ForeLimbFelisCatus"]
        cat_hand = cat_forelimb.parts["HandFelisCatus"]
        self.assertEqual(cat_hand.parent, "Hand")
        self.assertEqual(cat_hand.in_taxon, "FelisCatus")
        dumper = OWLDumper()
        dumper.schemaview = sv

        doc = dumper.to_ontology_document(data, schema=sv.schema)
        #for a in doc.ontology.axioms:
        #    print(f'AXIOM={a}')
        with open(OWL_OUT, 'w') as stream:
            stream.write(str(doc))

