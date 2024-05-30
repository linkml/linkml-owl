"""Test the module can be imported."""
import logging
import os
import unittest

import pytest
import rdflib
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from rdflib import Graph, URIRef, Literal

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper
from funowl.converters.functional_converter import to_python

from tests import INPUT_DIR, OUTPUT_DIR

EX = rdflib.Namespace('http://example.org/enum-test/')


SCHEMA_IN = os.path.join(INPUT_DIR, 'enum_model.yaml')


@pytest.mark.parametrize("data_name,data,expected",[
    ("1", {"id": "ex:1", "job": "Welder"}, {"job": EX["Welder"]}),
    ("2", {"id": "ex:2", "job": "Bricklayer"}, {"job":  EX["JobEnum#Bricklayer"]}),
    ("3", {"id": "ex:3", "job": "Chimney Sweep"}, {"job": EX["JobEnum#Chimney+Sweep"]}),
    ("4", {"id": "ex:4", "job_str": "Welder"}, {"job_str": Literal("Welder")}),
    ("5", {"id": "ex:5", "job_str": "Bricklayer"}, {"job_str": Literal("Bricklayer")}),
    ("6", {"id": "ex:6", "job_str": "Chimney Sweep"}, {"job_str": Literal("Chimney Sweep")}),
])
def test_enums(data_name, data, expected):
    """
    Test mapping of permissible values in enums.

    If the enum slot is an object slot, then a URI is generated
    (using ``meaning`` if present, otherwise construct a URI by appending a hash url encoding
    of the PV to the enum)

    If the enum slot is a data slot, then a literal is created from the PV string
    """
    sv = SchemaView(SCHEMA_IN)
    python_module = PythonGenerator(SCHEMA_IN).compile_module()
    dumper = OWLDumper()
    dumper.schemaview = sv
    obj = python_module.Person(**data)
    doc = dumper.to_ontology_document(obj, schema=sv.schema)
    out_path = os.path.join(OUTPUT_DIR, f'enum-{data_name}.ofn')
    with open(out_path, 'w') as stream:
        stream.write(str(doc))
    doc_rt = to_python(str(doc))
    axioms = doc_rt.ontology.axioms
    logging.info(f'AXIOMS={len(axioms)}')
    g = Graph()
    doc.to_rdf(g)
    for p, v in expected.items():
        vals = []
        print(EX[p])
        print(f"CHECKING FOR {type(v)}  == {v}")
        for _s, __p, o in g.triples((None, EX[p], None)):
            vals.append(o)
            print(f" FOUND {o} {type(o)}")
        assert len(vals) == 1
        assert vals[0] == v

