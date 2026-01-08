import pyhornedowl
import pytest
from pyhornedowl.model import ObjectIntersectionOf, SubClassOf, ObjectSomeValuesFrom, Class, IRI, DeclareClass, \
    Annotation, SimpleLiteral, AnnotatedComponent, ObjectUnionOf, ObjectComplementOf, InverseObjectProperty, \
    ObjectAllValuesFrom, SubObjectPropertyOf

from tests import OUTPUT_DIR


@pytest.mark.parametrize("ont,syntax,valid",
[
    ("Ontology()", "ofn", True),
    ("Ontology( Declaration(Class(<http://example.org>)) )", "ofn", True),
    ("foo", "ofn", False),
])
def test_parse(ont, syntax, valid):
    if not valid:
        try:
            _onto = pyhornedowl.open_ontology_from_string(ont, serialization=syntax)
            assert False, "Expected an error"
        except Exception as e:
            print(f"Got expected error: {e}")
        return
    onto = pyhornedowl.open_ontology_from_string(ont, serialization=syntax)

    print(f"Loaded ontology has {len(onto.get_classes())} classes.")
    print(f"Loaded ontology has {len(onto.get_axioms())} axioms.")

    for c in onto.get_classes():
        print(onto.get_axioms_for_iri(c))

def test_generate():
    o = pyhornedowl.PyIndexedOntology()
    ont_iri = o.iri("https://example.com/")
    assert isinstance(ont_iri, IRI)
    assert str(ont_iri) == "https://example.com/"
    #assert IRI.parse("https://example.com/") == "https://example.com/"
    print(ont_iri)
    print(repr(ont_iri))
    print(o.get_iri())
    o.add_prefix_mapping("", "https://example.com/")
    o.add_prefix_mapping("ex", "https://example.com/ex/")
    assert str(o.curie("ex:A")) == "https://example.com/ex/A"

    a = o.clazz(str(o.curie("ex:A")))
    b = o.clazz("http://example.com/B")
    p = o.object_property(str(o.curie("ex:p")))
    a_iri = IRI.parse("https://example.com/A")
    #a = Class(a_iri)
    ax = SubClassOf(a, ObjectSomeValuesFrom(p, b))
    print(repr(ax))
    o.add_axiom(ax)
    o.add_axiom(DeclareClass(a))
    o.add_axiom(DeclareClass(b))
    ap = o.annotation_property(str(o.curie("ex:ap")))
    ann = Annotation(ap, SimpleLiteral("foo"))
    o.add_axiom(ax, {ann})
    x = o.iri("https://example.com/")
    print(x)
    o.save_to_file("/tmp/foo.ofn", "ofn")
    o.save_to_file("/tmp/foo.owl", "owl")
    print(o.get_iri())
    print(o.curie("ex:[p]"))

def test_class_expressions():
    o = pyhornedowl.PyIndexedOntology()
    o.add_prefix_mapping("", "https://example.com/")

    A = o.clazz(":A")
    B = o.clazz(":B")
    C = o.clazz(":C")
    r = o.object_property("r")

    assert A & B == ObjectIntersectionOf([A, B])
    assert A | B == ObjectUnionOf([A, B])
    assert ~A == ObjectComplementOf(A)
    assert ~r == InverseObjectProperty(r)
    assert r.some(A) == ObjectSomeValuesFrom(r, A)
    assert r.only(A) == ObjectAllValuesFrom(r, A)
    assert r.some(A & B | (~r).only(C)) == ObjectSomeValuesFrom(r, ObjectUnionOf(
        [ObjectIntersectionOf([A, B]), ObjectAllValuesFrom(InverseObjectProperty(r), C)]))
    o.add_axiom(SubObjectPropertyOf(r, r))
    import os
    o.save_to_file(os.path.join(OUTPUT_DIR, "ce.owl"), "owl")