# linkml-owl Test Cases

These examples are generated automatically from test_owl_dumper

For the complete schema, see tests/input/owl_dumper_test.yaml

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  
```

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
        annotations:
          owl: AnnotationAssertion
        slot_uri: skos:exactMatch
        range: NamedThing
        required: true
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  exactMatch: x:b
  
```

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
        annotations:
          owl: AnnotationAssertion
        slot_uri: skos:exactMatch
        range: string
        required: true
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  exactMatch: x:b
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - x:b
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  equivalent_to:
  - x:b
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  part_of:
  - x:b
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  part_of:
  - x:b
  
```

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

## SubClassOf SomeValuesFrom plus label


__Description__: _Demonstrates a mix of slots, some annotation, some logical_


__Schema__:

```yaml
id: http//example.org/SubClassOf-SomeValuesFrom-plus-label
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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  part_of:
  - x:b
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label <http://example.org/a> "foo" )
    SubClassOf( <http://example.org/a>     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/b> ) )
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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - x:b
  - x:c
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  operands:
  - x:b
  - x:c
  
```

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
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  operands:
  - x:b
  - x:c
  
```

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
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
        description: for hidden GCIs
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: false
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - X:genus
  part_of:
  - x:b
  - x:c
  
```

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

## Hidden GCI


__Description__: _Demonstrates a case where some slots contribute to a logical definition (equiv axiom),
                     and other contribute to additional axioms (so called hidden GCIs)_


__Schema__:

```yaml
id: http//example.org/Hidden-GCI
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
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
        description: for hidden GCIs
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: false
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - X:genus
  part_of:
  - x:b
  other_part_ofs:
  - x:c
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( <http://example.org/a>     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/c> ) )
    EquivalentClasses(
        <http://example.org/a>
            ObjectIntersectionOf(
        <http://example.org/genus>
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> <http://example.org/b> )
    )
    )
)
```

## slot-value level fstring template


__Description__: _Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)_


__Schema__:

```yaml
id: http//example.org/slot-value-level-fstring-template
classes:
  ClassTemplateExample1:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl.fstring:
            tag: owl.fstring
            value: SubClassOf({id} {V})
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
      part_of:
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
      other_part_ofs:
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - x:b
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a <http://example.org/b> )
)
```

## slot-value level jinja template


__Description__: _Axiom generation per slot-value assignment.
                     (Note that currently non-identifier fields have their URIs expanded,
                      but the OWL is the same)_


__Schema__:

```yaml
id: http//example.org/slot-value-level-jinja-template
classes:
  ClassTemplateExample2:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl.template:
            tag: owl.template
            value: '{% for p in subclass_of %}SubClassOf({{id}} {{p}}){% endfor %}'
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
      part_of:
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
      other_part_ofs:
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  subclass_of:
  - x:b
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a x:b )
)
```

## Parts collection with counts


__Description__: _Demonstrates nesting
                  _


__Schema__:

```yaml
id: http//example.org/Parts-collection-with-counts
classes:
  CollectionOfPartsWithCounts:
    annotations:
      owl.template:
        tag: owl.template
        value: "{% for p in has_part %}\nSubClassOf( {{id}}\n            ObjectSomeValuesFrom(\
          \ BFO:0000051\n                                  ObjectIntersectionOf( {{p.unit\
          \ }}\n                                                        ObjectSomeValuesFrom(RO:0000053\
          \ {{p.state.meaning}})\n                                               \
          \         {% if p.count %}\n                                           \
          \             DataHasValue(PATO:0001555 \"{{p.count}}\"^^xsd:integer )\n\
          \                                                        {% endif %}\n \
          \                                                     )\n\n            \
          \                     )\n          )\n{% endfor %}"
    is_a: NamedThing
    attributes:
      has_part:
        slot_uri: BFO:0000051
        multivalued: true
        inlined: true
        inverse: part_of
        range: PartWithCounts
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:collection
  has_part:
  - unit: x:p1
    count: 2
    state: ACTIVATED
  - unit: x:p2
    count: 3
    state: ACTIVATED
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:collection     ObjectSomeValuesFrom( BFO:0000051     ObjectIntersectionOf(
        x:p1
            ObjectSomeValuesFrom( RO:0000053 <http://purl.obolibrary.org/obo/PATO_0002354> )
            DataHasValue( PATO:0001555 "2"^^xsd:integer )
    ) ) )
    SubClassOf( x:collection     ObjectSomeValuesFrom( BFO:0000051     ObjectIntersectionOf(
        x:p2
            ObjectSomeValuesFrom( RO:0000053 <http://purl.obolibrary.org/obo/PATO_0002354> )
            DataHasValue( PATO:0001555 "3"^^xsd:integer )
    ) ) )
)
```

## Parts collection


__Description__: _Things that are made of an arbitrary list of parts
                  _


__Schema__:

```yaml
id: http//example.org/Parts-collection
classes:
  CollectionOfParts:
    annotations:
      owl.template:
        tag: owl.template
        value: "{% for p in has_part %}\nSubClassOf( {{id}} ObjectSomeValuesFrom(\
          \ BFO:0000051 {{p}} ) )\n{% endfor %}\nDisjointClasses(\n   Annotation(\
          \ rdfs:label \"all parts of {{id}} are part-disjoint\")\n  {% for p in has_part\
          \ %}\n  ObjectSomeValuesFrom( BFO:0000050 {{p}} )\n  {% endfor %}\n)"
    is_a: NamedThing
    attributes:
      has_part:
        slot_uri: BFO:0000051
        multivalued: true
        inverse: part_of
        range: NamedThing
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:collection
  has_part:
  - x:p1
  - x:p2
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:collection     ObjectSomeValuesFrom( BFO:0000051 x:p1 ) )
    SubClassOf( x:collection     ObjectSomeValuesFrom( BFO:0000051 x:p2 ) )
    DisjointClasses(
        Annotation( rdfs:label "all parts of x:collection are part-disjoint" )
            ObjectSomeValuesFrom( BFO:0000050 x:p1 )     ObjectSomeValuesFrom( BFO:0000050 x:p2 )
    )
)
```

## Defined parts collection


__Description__: _Things that are defined exhaustively by an arbitrary list of parts
                  _


__Schema__:

```yaml
id: http//example.org/Defined-parts-collection
classes:
  DefinedCollectionOfParts:
    annotations:
      owl.template:
        tag: owl.template
        value: "EquivalentClasses( {{id}}\n                   ObjectIntersectionOf(\n\
          \                     {% for p in has_part %}\n                       ObjectSomeValuesFrom(\
          \ BFO:0000051 {{p}} )\n                     {% endfor %}\n             \
          \        ObjectAllValuesFrom( BFO:0000051\n                            \
          \              ObjectSomeValuesFrom( BFO:0000050\n                     \
          \                       ObjectUnionOf(\n                               \
          \             {% for p in has_part %}\n                                \
          \              ObjectSomeValuesFrom( BFO:0000051 {{p}} )\n             \
          \                               {% endfor %} )\n                       \
          \                   )\n                                        )\n     \
          \              )\n                 )"
    is_a: NamedThing
    attributes:
      has_part:
        slot_uri: BFO:0000051
        multivalued: true
        inverse: part_of
        range: NamedThing
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:collection
  has_part:
  - x:dp1
  - x:dp2
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:collection
            ObjectIntersectionOf(
            ObjectSomeValuesFrom( BFO:0000051 x:dp1 )
            ObjectSomeValuesFrom( BFO:0000051 x:dp2 )
            ObjectAllValuesFrom( BFO:0000051     ObjectSomeValuesFrom( BFO:0000050     ObjectUnionOf(
            ObjectSomeValuesFrom( BFO:0000051 x:dp1 )
            ObjectSomeValuesFrom( BFO:0000051 x:dp2 )
    ) ) )
    )
    )
)
```

