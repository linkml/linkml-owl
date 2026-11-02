"""
Check that OWLDumper's per-schema memos do not leak between dumps.

OWLDumper caches slot lookups and inferred slot annotations keyed by slot
and class *name*. Those memos must be dropped whenever the dumper is pointed
at a new schema, otherwise reusing one dumper instance across schemas that
share class and slot names would silently emit axioms from the wrong schema.
"""
from copy import deepcopy
from dataclasses import dataclass

import pytest
from linkml_runtime.linkml_model import ClassDefinition, Prefix, SchemaDefinition, SlotDefinition
from linkml_runtime.linkml_model.meta import Annotation
from linkml_runtime.utils.yamlutils import YAMLRoot
from pyhornedowl.model import AnnotationAssertion, SubClassOf

from linkml_owl.dumpers.owl_dumper import OWLDumper


@dataclass
class Thing(YAMLRoot):
    class_name = "Thing"
    id: str = None
    parent: str = None


def _make_schema(parent_fstring: str) -> SchemaDefinition:
    schema = SchemaDefinition(
        id="http://example.org/cache-test",
        name="cache_test",
        default_prefix="X",
        prefixes={
            "X": Prefix("X", "http://example.org/"),
            "rdfs": Prefix("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
        },
    )
    schema.slots["id"] = SlotDefinition("id", identifier=True, range="uriorcurie")
    schema.slots["parent"] = SlotDefinition("parent", range="Thing")
    schema.slots["parent"].annotations["owl.fstring"] = Annotation("owl.fstring", parent_fstring)
    schema.classes["Thing"] = ClassDefinition("Thing", slots=["id", "parent"])
    return schema


SCHEMA_A = _make_schema("SubClassOf({id} {V})")
SCHEMA_B = _make_schema("AnnotationAssertion(rdfs:seeAlso {id} {V})")


def _axiom_types(dumper: OWLDumper, schema: SchemaDefinition) -> set:
    element = Thing(id="X:1", parent="X:2")
    doc = dumper.to_ontology_document(element, deepcopy(schema))
    return {type(c.component) for c in doc.get_components()}


@pytest.mark.parametrize("first,second,expected_second", [
    (SCHEMA_A, SCHEMA_B, AnnotationAssertion),
    (SCHEMA_B, SCHEMA_A, SubClassOf),
])
def test_memos_reset_between_schemas(first, second, expected_second):
    """Dumping twice through one dumper must honour the second schema's annotations."""
    dumper = OWLDumper()
    _axiom_types(dumper, first)
    assert expected_second in _axiom_types(dumper, second)


def test_memos_reused_within_a_dump():
    """Within one dump the memo is populated and hit, not bypassed."""
    dumper = OWLDumper()
    _axiom_types(dumper, SCHEMA_A)
    cache = dumper._cache("inferred_slot_annotations")
    assert ("parent", "owl.fstring", "Thing") in cache
    assert cache[("parent", "owl.fstring", "Thing")] == ["SubClassOf({id} {V})"]
