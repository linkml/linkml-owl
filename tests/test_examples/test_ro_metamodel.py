# -*- coding: utf-8 -*-
import logging
import os
import unittest
from typing import List

from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper
from funowl.converters.functional_converter import to_python

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

    doc = dumper.to_ontology_document(data, schema=sv.schema)
    with open(OWL_OUT, 'w') as stream:
        stream.write(str(doc))
    doc_rt = to_python(str(doc))
    axioms = doc_rt.ontology.axioms
    logging.info(f'AXIOMS={len(axioms)}')
    assert len(axioms) > 5
    # compare with expected output
    doc_expected = to_python(str(EXPECTED))
    assert len(axioms) == len(doc_expected.ontology.axioms)
    assert str_sorted(axioms) == str_sorted(doc_expected.ontology.axioms)

