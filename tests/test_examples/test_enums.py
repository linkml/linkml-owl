"""Test the module can be imported."""
import logging
import os
import unittest

import pyhornedowl
import pytest
import rdflib
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from rdflib import Graph, URIRef, Literal

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.dumpers.owl_dumper import OWLDumper

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
    # Use dumps() to get properly fixed OFN string
    ofn_str = dumper.dumps(obj, schema=sv.schema, output_type="ofn")
    out_path = os.path.join(OUTPUT_DIR, f'enum-{data_name}.ofn')
    with open(out_path, 'w') as stream:
        stream.write(ofn_str)
    # Parse back to verify
    doc_rt = pyhornedowl.open_ontology_from_string(ofn_str, "ofn")
    axioms = doc_rt.get_axioms()
    logging.info(f'AXIOMS={len(axioms)}')
    # Get RDF graph for testing - need the ontology document for this
    doc = dumper.ontology  # Get the ontology created during dumps()
    rdf_str = doc.save_to_string("owl")
    g = Graph()
    g.parse(data=rdf_str, format='xml')
    for p, v in expected.items():
        vals = []
        print(EX[p])
        print(f"CHECKING FOR {type(v)}  == {v}")
        for _s, __p, o in g.triples((None, EX[p], None)):
            vals.append(o)
            print(f" FOUND {o} {type(o)}")
        assert len(vals) == 1
        # For literals, compare string values since py-horned-owl may add xsd:string datatype
        if isinstance(v, Literal):
            assert str(vals[0]) == str(v)
        else:
            assert vals[0] == v

