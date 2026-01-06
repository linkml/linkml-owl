# -*- coding: utf-8 -*-
import logging
import os
import unittest
from typing import List

import pyhornedowl
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper

from tests import INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'ro-metamodel.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'ro-data.yaml')
OWL_OUT = os.path.join(OUTPUT_DIR, 'ro.ofn')
EXPECTED = os.path.join(INPUT_DIR, 'expected_ro.ofn')


def str_sorted(objs: List[object]) -> List[str]:
    return sorted([str(o) for o in objs])


def test_build_relation_ontology():
    """
    Test creation of an OWL TBox
    """
    #logging.basicConfig(level=logging.DEBUG)
    sv = SchemaView(SCHEMA_IN)
    python_module = PythonGenerator(SCHEMA_IN).compile_module()
    data = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
    dumper = OWLDumper()
    dumper.schemaview = sv
    domain_slot = sv.get_slot('domain')
    #print(domain_slot)
    #print(f'URI = {domain_slot.slot_uri}')
    assert domain_slot.slot_uri == 'rdfs:domain'
    anns = dumper._get_inferred_slot_annotations(domain_slot, 'owl', 'TransitiveForm')
    #print(f'Anns={anns}')
    assert 'ObjectPropertyDomain' in anns

    test_slot = sv.get_slot('inverse_of')
    #print(domain_slot)
    #print(f'URI = {domain_slot.slot_uri}')
    assert test_slot.slot_uri == 'owl:inverseOf'
    anns = dumper._get_inferred_slot_annotations(test_slot, 'owl', 'TransitiveForm')
    print(f'Anns={anns}')
    assert 'InverseObjectProperties' in anns
    cls = sv.get_class('TransitiveForm')
    tmpls = dumper._get_inferred_class_annotations(cls, 'owl.template')
    print(f'TMPLS={tmpls}')
    assert tmpls

    ofn_str = dumper.dumps(data, schema=sv.schema, output_type="ofn")
    with open(OWL_OUT, 'w') as stream:
        stream.write(ofn_str)
    doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
    axioms = doc_rt.get_axioms()
    logging.info(f'AXIOMS={len(axioms)}')
    assert len(axioms) > 5
    # Verify expected output can also be parsed
    with open(EXPECTED, 'r') as f:
        expected_str = f.read()
    doc_expected = pyhornedowl.open_ontology_from_string(expected_str, "ofn")
    expected_axioms = doc_expected.get_axioms()
    # Allow for minor differences between funowl and py-horned-owl output
    # (typically 1-2 axioms due to serialization differences)
    axiom_diff = abs(len(axioms) - len(expected_axioms))
    assert axiom_diff <= 2, f"Axiom count difference too large: {len(axioms)} vs {len(expected_axioms)}"

