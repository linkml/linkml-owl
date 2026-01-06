import logging
from typing import Type, Union, List, Any, Collection

from linkml_runtime.linkml_model.types import Uri, Uriorcurie
from pyhornedowl.model import *
from pyhornedowl.pyhornedowl import PyIndexedOntology

# Aliasing Axiom for isomorphism to OWL2 specification
# See also: https://github.com/ontology-tools/py-horned-owl/issues/30
Axiom = Component

# Aliasing Ontology for isomorphism to OWL2 specification
Ontology = PyIndexedOntology

logger = logging.getLogger(__name__)


def _is_uri_like(obj: Any) -> bool:
    """Check if an object is URI-like (string, IRI, or linkml-runtime URI type)."""
    return isinstance(obj, (str, IRI, Uri, Uriorcurie))


def render_object(obj: Any) -> str:
    """
    Render an object to a string.

    :param obj:
    :return:
    """
    if isinstance(obj, IRI):
        return str(obj)
    if isinstance(obj, str):
        return obj
    if isinstance(obj, (DeclareClass, DeclareObjectProperty, DeclareDataProperty, DeclareAnnotationProperty, DeclareNamedIndividual, DeclareDatatype)):
        return type(obj).__name__ + "(" + render_object(obj.first) + ")"
    if isinstance(obj, ClassExpression):
        return str(obj)
    return repr(obj)

def add_axiom(ontology: PyIndexedOntology, axiom: Union[Component, AnnotatedComponent]) -> None:
    """
    Add an axiom to an ontology.

    Example:

        >>> ontology = PyIndexedOntology()
        >>> a = ontology.clazz("http://example.com/A")
        >>> b = ontology.clazz("http://example.com/B")
        >>> sc = SubClassOf(a, b)
        >>> add_axiom(ontology, sc)
        >>> len(ontology.get_axioms())
        1
        >>> axiom = ontology.get_axioms()[0]
        >>> assert axiom.component == sc
        >>> ap = ontology.annotation_property("http://example.com/label")
        >>> ann = Annotation(ap, SimpleLiteral("foo"))
        >>> asc = AnnotatedComponent(sc, {ann})
        >>> add_axiom(ontology, asc)
        >>> len(ontology.get_axioms())
        2

    :param ontology:
    :param axiom:
    :return:
    """
    if isinstance(axiom, AnnotatedComponent):
        ontology.add_axiom(axiom.component, set(axiom.ann))
    elif isinstance(axiom, Axiom):
        ontology.add_axiom(axiom, set())
    else:
        raise ValueError(f"Cannot add axiom {axiom}")


def as_class_expression(ontology: PyIndexedOntology, x: Union[ClassExpression, IRI, str]) -> ClassExpression:
    """
    Cast an object to a class expression.

    If the object is a string, it is converted to a class.

        >>> ontology = PyIndexedOntology()
        >>> cls = as_class_expression(ontology, "http://example.com/A")
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'

    If the object is an IRI, it is converted to a class.

        >>> iri = ontology.iri("http://example.com/A")
        >>> cls = as_class_expression(ontology, iri)
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'

    If the object is a CURIE, it is converted to a class.

        >>> ontology.add_prefix_mapping("ex", "http://example.com/ex/")
        >>> ontology.add_prefix_mapping("", "http://example.com/")
        >>> curie = ontology.curie("ex:A")
        >>> cls = as_class_expression(ontology, curie)
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/ex/A'
        >>> curie = ontology.curie(":A")
        >>> cls = as_class_expression(ontology, curie)
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'
        >>> curie = ontology.curie("A")
        >>> cls = as_class_expression(ontology, curie)
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'
        >>> cls = as_class_expression(ontology, "ex:A")
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/ex/A'
        >>> cls = as_class_expression(ontology, ":A")
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'
        >>> cls = as_class_expression(ontology, "A")
        >>> assert isinstance(cls, Class)
        >>> str(cls)
        'http://example.com/A'

    If the object is a class expression, it is returned as is.

        >>> cls = ontology.clazz("http://example.com/A")
        >>> cls2 = as_class_expression(ontology, cls)
        >>> assert cls is cls2

    If the object is a compound class expression, it is returned as is.

        >>> cls = ObjectIntersectionOf([ontology.clazz("http://example.com/A"), ontology.clazz("http://example.com/B")])
        >>> cls2 = as_class_expression(ontology, cls)
        >>> assert cls is cls2

    If the object is of a different type, an error is raised.

        >>> try:
        ...     as_class_expression(ontology, 1)
        ... except ValueError as e:
        ...     print(e)
        Cannot convert 1 to class expression

    :param ontology:
    :param x:
    :return:
    """
    if isinstance(x, ClassExpression):
        return x
    if isinstance(x, IRI):
        x = str(x)
    if not isinstance(x, str):
        raise ValueError(f"Cannot convert {x} to class expression")
    return ontology.clazz(x)


def as_class_expression_list(ontology: PyIndexedOntology, *x: Union[ClassExpression, IRI, str]) -> List[ClassExpression]:
    """
    Convert a list of objects to a list of class expressions.

    Example:

        >>> ontology = PyIndexedOntology()
        >>> cls_list = as_class_expression_list(ontology, "http://example.com/A", "http://example.com/B")
        >>> assert len(cls_list) == 2
        >>> assert all(isinstance(cls, Class) for cls in cls_list)

    :param ontology:
    :param x:
    :return:
    """
    return [as_class_expression(ontology, y) for y in x]

def get_declarations(ontology: PyIndexedOntology, subj: Any, interpretations: Collection[str]):
    """
    Get declarations for a subject.

    Example:

        >>> ontology = PyIndexedOntology()
        >>> decls = get_declarations(ontology, "http://example.com/A", ["Class"])
        >>> assert len(decls) == 1
        >>> decl = decls[0]
        >>> assert isinstance(decl, DeclareClass)
        >>> str(decl.first)
        'http://example.com/A'

    :param ontology:
    :param subj:
    :param interpretations:
    :return:
    """
    declarations = []
    # Store the original string representation for use in each iteration
    # (avoid mutating subj in the loop)
    subj_str = str(subj) if subj else None
    for model_class, declaration_class, create_method in [
        (ObjectProperty, DeclareObjectProperty, ontology.object_property),
        (DataProperty, DeclareDataProperty, ontology.data_property),
        (AnnotationProperty, DeclareAnnotationProperty, ontology.annotation_property),
        (NamedIndividual, DeclareNamedIndividual, ontology.named_individual),
        (Class, DeclareClass, ontology.clazz),
        (Datatype, DeclareDatatype, None),
    ]:
        if model_class.__name__ in interpretations:
            if not subj_str:
                raise ValueError(f"Cannot create {declaration_class} without an identifier")
            # Create the entity using the appropriate factory method
            entity = create_method(subj_str) if create_method else None
            if entity is None:
                # Datatype doesn't have a factory method, skip for now
                continue
            decl = declaration_class(entity)
            declarations.append(decl)
            logger.debug(f"Inferred {decl} based on {model_class.__name__} in {interpretations}")
    return declarations

def instantiate_restriction(typ: Type[ClassExpression], prop: str, value: str, ontology: PyIndexedOntology) -> ClassExpression:
    """
    Instantiate a restriction.

    OneOf:
    ObjectSomeValuesFrom, DataSomeValuesFrom, ObjectHasValue, DataHasValue, ObjectAllValuesFrom, DataAllValuesFrom

    """
    if typ in [ObjectSomeValuesFrom, ObjectAllValuesFrom, ObjectHasValue]:
        op = ontology.object_property(prop)
        if typ in [ObjectSomeValuesFrom, ObjectAllValuesFrom]:
            value = as_class_expression(ontology, value)
        else:
            # ObjectHasValue - value is an individual
            value = ontology.named_individual(str(value))
        return typ(op, value)
    dp = ontology.data_property(prop)
    if typ in [DataSomeValuesFrom, DataAllValuesFrom]:
        value = ontology.datatype(str(value))
    else:
        #value = SimpleLiteral(value)
        value = value
    return typ(dp, value)