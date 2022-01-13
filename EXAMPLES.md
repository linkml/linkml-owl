# linkml-owl Test Cases

## Annotation using literals


__Description__: _Default is to use an annotation assertion,
                  and if the range is a string then this is literal_


__Schema__:

```yaml
id: http//example.org/Annotation-using-literals
classes:
  NamedThing:
    is_a: Thing
    attributes:
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* NamedThing(id='x:a', label='foo')

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label <http://example.org/a> "foo" )
)
```

## Annotation using IRIs


__Description__: _As above, but if the range is an instance of a LinkML class then use a literal_


__Schema__:

```yaml
id: http//example.org/Annotation-using-IRIs
classes:
  ExactMatch:
    is_a: NamedThing
    attributes:
      exactMatch:
        slot_uri: skos:exactMatch
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* ExactMatch(id='x:a', label=None, exactMatch='x:b')

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( <http://www.w3.org/2004/02/skos/core#exactMatch> <http://example.org/a> <http://example.org/b> )
)
```

## Annotation using forced literals


__Description__: _We can force a literal by imposing a range_


__Schema__:

```yaml
id: http//example.org/Annotation-using-forced-literals
classes:
  ExactMatchAsLiteral:
    is_a: NamedThing
    attributes:
      exactMatch:
        slot_uri: skos:exactMatch
        range: string
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* ExactMatchAsLiteral(id='x:a', label=None, exactMatch='x:b')

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( <http://www.w3.org/2004/02/skos/core#exactMatch> <http://example.org/a> "x:b" )
)
```

## Basic SubClassOf between named classes


__Description__: _Adding SubClassOf annotation to the linkml class forces a SubClass axiom
                  _


__Schema__:

```yaml
id: http//example.org/Basic-SubClassOf-between-named-classes
classes:
  Child:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: SubClassOf
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* Child(id='x:a', label=None, subclass_of=['x:b'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( <http://example.org/a> <http://example.org/b> )
)
```

## basic direct equivalence between named classes


__Description__: _Adding EquivalentTo annotation to the linkml class forces a SubClass axiom_


__Schema__:

```yaml
id: http//example.org/basic-direct-equivalence-between-named-classes
classes:
  DirectEquivalent:
    is_a: NamedThing
    attributes:
      equivalent_to:
        annotations:
          owl: EquivalentClasses
        slot_uri: owl:equivalentClasses
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* DirectEquivalent(id='x:a', label=None, equivalent_to=['x:b'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        <http://example.org/a>
        <http://example.org/b>
    )
)
```

## SubClassOf SomeValuesFrom


__Description__: _A SubClassOf annotation makes the annotation type be subclass,
                  a SomeValuesFrom annotation makes the slot interpreted as an existential_


__Schema__:

```yaml
id: http//example.org/SubClassOf-SomeValuesFrom
classes:
  Part:
    is_a: NamedThing
    attributes:
      part_of:
        annotations:
          owl: ObjectSomeValuesFrom
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* Part(id='x:a', label=None, part_of=['x:b'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( <http://example.org/a>     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/b> ) )
)
```

## SubClassOf AllValuesFrom


__Description__: _As above, but with universal restrictions_


__Schema__:

```yaml
id: http//example.org/SubClassOf-AllValuesFrom
classes:
  PartOnly:
    is_a: NamedThing
    attributes:
      part_of:
        annotations:
          owl: ObjectAllValuesFrom
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* PartOnly(id='x:a', label=None, part_of=['x:b'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( <http://example.org/a>     ObjectAllValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/b> ) )
)
```

## SubClassOf Union


__Description__: _The slot is interpreted as a parent class,
                  and all slot values with a UnionOf annotation are collected to make a UnionOf expression_


__Schema__:

```yaml
id: http//example.org/SubClassOf-Union
classes:
  ChildOfUnion:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: SubClassOf, UnionOf
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* ChildOfUnion(id='x:a', label=None, subclass_of=['x:b', 'x:c'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( <http://example.org/a>     ObjectUnionOf(
        <http://example.org/b>
        <http://example.org/c>
    ) )
)
```

## EquivalentTo Union


__Description__: _As above, but with equivalence_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-Union
classes:
  EquivUnion:
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, UnionOf
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* EquivUnion(id='x:a', label=None, operands=['x:b', 'x:c'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        <http://example.org/a>
            ObjectUnionOf(
        <http://example.org/b>
        <http://example.org/c>
    )
    )
)
```

## EquivalentTo IntersectionOf


__Description__: _The slot is interpreted as a parent class,
                  and all slot values with a IntersectionOf annotation are collected to make a IntersectionOf expression_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-IntersectionOf
classes:
  EquivIntersection:
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* EquivIntersection(id='x:a', label=None, operands=['x:b', 'x:c'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        <http://example.org/a>
            ObjectIntersectionOf(
        <http://example.org/b>
        <http://example.org/c>
    )
    )
)
```

## EquivalentTo Genus and SomeValuesFrom


__Description__: _All slot value interpretations are collected into a single IntersectionOf_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-Genus-and-SomeValuesFrom
classes:
  EquivGenusAndPartOf:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
        required: true
      part_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: true
      id:
        identifier: true
      label:
        slot_uri: rdfs:label

```


__Input__:

* EquivGenusAndPartOf(id='x:a', label=None, subclass_of=['X:genus'], part_of=['x:b', 'x:c'])

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        <http://example.org/a>
            ObjectIntersectionOf(
        <http://example.org/genus>
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/b> )
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/c> )
    )
    )
)
```

