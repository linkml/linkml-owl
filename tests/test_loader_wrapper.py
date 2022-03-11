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


from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper, rdflib_dumper
from linkml_runtime.loaders import yaml_loader

from tests import MODEL_DIR, INPUT_DIR, OUTPUT_DIR

"""Test the module can be imported."""

SCHEMA_IN = os.path.join(INPUT_DIR, 'ro-metamodel-v2.yaml')
DATA_IN = os.path.join(INPUT_DIR, 'ro-data-v2.yaml')
META_ONT_OUT = os.path.join(OUTPUT_DIR, 'ro-meta-ont.ttl')




class TestLoaderWrapper(unittest.TestCase):
    """Tests the loader wrapper."""

    def test_loader_wrapper(self):
        sv = SchemaView(SCHEMA_IN)
        python_module = PythonGenerator(SCHEMA_IN).compile_module()
        objs = load_structured_file(DATA_IN, schemaview=sv, python_module=python_module)
        full_graph = Graph()
        for obj in objs:
            d = rdflib_dumper.dumps(obj, schemaview=sv)
            g = rdflib_dumper.as_rdf_graph(obj, schemaview=sv)
            full_graph += g
            #print(d)
        gen = OwlSchemaGenerator(SCHEMA_IN, metaclasses=False, type_objects=False, format='turtle')
        ttl_str = gen.serialize()
        full_graph.parse(data=ttl_str, format='turtle')
        full_graph.serialize(destination=META_ONT_OUT, format='ttl')
