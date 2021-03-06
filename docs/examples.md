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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "foo" )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( skos:exactMatch x:a x:b )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( skos:exactMatch x:a "x:b" )
)
```

## Axiom annotation with Literal value on annotation axiom


__Description__: _Axiom annotations (literals) can be driven by a separate slot_


__Schema__:

```yaml
id: http//example.org/Axiom-annotation-with-Literal-value-on-annotation-axiom
classes:
  DefinitionWithAxiomAnnotation:
    is_a: NamedThing
    attributes:
      definition_source:
        slot_uri: dcterms:source
        multivalued: true
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  definition: a foo is a foo
  definition_source:
  - Me
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "foo" )
    AnnotationAssertion(
        Annotation( dcterms:source "Me" )
        <http://purl.obolibrary.org/obo/IAO_0000115> x:a "a foo is a foo"
    )
)
```

## Axiom annotation with IRI val on annotation axiom


__Description__: _Axiom annotations (IRIs) can be driven by a separate slot_


__Schema__:

```yaml
id: http//example.org/Axiom-annotation-with-IRI-val-on-annotation-axiom
classes:
  DefinitionWithIRIAxiomAnnotation:
    is_a: NamedThing
    attributes:
      definition_source:
        slot_uri: dcterms:source
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
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  definition: a foo is a foo
  definition_source:
  - x:src
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "foo" )
    AnnotationAssertion(
        Annotation( dcterms:source x:src )
        <http://purl.obolibrary.org/obo/IAO_0000115> x:a "a foo is a foo"
    )
)
```

## Axiom annotations with IRI val on annotation axiom


__Description__: _Multiple axiom annotations_


__Schema__:

```yaml
id: http//example.org/Axiom-annotations-with-IRI-val-on-annotation-axiom
classes:
  DefinitionWithIRIAxiomAnnotation:
    is_a: NamedThing
    attributes:
      definition_source:
        slot_uri: dcterms:source
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
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  definition: a foo is a foo
  definition_source:
  - x:src1
  - x:src2
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "foo" )
    AnnotationAssertion(
        Annotation( dcterms:source x:src1 )
        Annotation( dcterms:source x:src2 )
        <http://purl.obolibrary.org/obo/IAO_0000115> x:a "a foo is a foo"
    )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a x:b )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:a
        x:b
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b ) )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a     ObjectAllValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b ) )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "foo" )
    SubClassOf( x:a     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b ) )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a     ObjectUnionOf(
        x:b
        x:c
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:a
            ObjectUnionOf(
        x:b
        x:c
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:a
            ObjectIntersectionOf(
        x:b
        x:c
    )
    )
)
```

## EquivalentTo IntersectionOf with axiom annotation


__Description__: _as above, with axiom annotation_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-IntersectionOf-with-axiom-annotation
classes:
  EquivIntersectionWithAxiomAnnotation:
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, IntersectionOf
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        multivalued: true
        range: NamedThing
        required: true
      logical_definition_source:
        slot_uri: dcterms:source
        multivalued: true
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
  logical_definition_source:
  - Me
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        Annotation( dcterms:source "Me" )
            x:a
                ObjectIntersectionOf(
        x:b
        x:c
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:a
            ObjectIntersectionOf(
        x:genus
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b )
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:c )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:c ) )
    EquivalentClasses(
        x:a
            ObjectIntersectionOf(
        x:genus
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b )
    )
    )
)
```

## Hidden GCI with axiom annotations


__Description__: _End-to-end example with hidden GCIs and different axiom annotations_


__Schema__:

```yaml
id: http//example.org/Hidden-GCI-with-axiom-annotations
classes:
  EquivGenusAndPartOfWithAxiomAnnotation:
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        slot_uri: rdfs:subclass_of
        multivalued: true
        range: NamedThing
        required: true
      part_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: true
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: axiom_source
        description: for hidden GCIs
        slot_uri: BFO:0000050
        multivalued: true
        range: NamedThing
        required: false
      definition_source:
        slot_uri: dcterms:source
        multivalued: true
      logical_definition_source:
        slot_uri: dcterms:source
        multivalued: true
      axiom_source:
        slot_uri: dcterms:source
        multivalued: true
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        slot_uri: rdfs:label
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        slot_uri: IAO:0000115

```


__Input__:

```yaml
-
  id: x:a
  label: a
  definition: A X:genus that part_of some x:b
  subclass_of:
  - X:genus
  part_of:
  - x:b
  other_part_ofs:
  - x:c
  definition_source:
  - Auto
  logical_definition_source:
  - Me
  axiom_source:
  - Auto
  
```

__Generated axioms__:

```
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    AnnotationAssertion( rdfs:label x:a "a" )
    AnnotationAssertion(
        Annotation( dcterms:source "Auto" )
        <http://purl.obolibrary.org/obo/IAO_0000115> x:a "A X:genus that part_of some x:b"
    )
    SubClassOf(
        Annotation( dcterms:source "Auto" )
        x:a     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:c )
    )
    EquivalentClasses(
        Annotation( dcterms:source "Me" )
            x:a
                ObjectIntersectionOf(
        x:genus
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:b )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:a x:b )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:collection     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051>     ObjectIntersectionOf(
        x:p1
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/RO_0000053> <http://purl.obolibrary.org/obo/PATO_0002354> )
            DataHasValue( <http://purl.obolibrary.org/obo/PATO_0001555> "2"^^xsd:integer )
    ) ) )
    SubClassOf( x:collection     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051>     ObjectIntersectionOf(
        x:p2
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/RO_0000053> <http://purl.obolibrary.org/obo/PATO_0002354> )
            DataHasValue( <http://purl.obolibrary.org/obo/PATO_0001555> "3"^^xsd:integer )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    SubClassOf( x:collection     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:p1 ) )
    SubClassOf( x:collection     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:p2 ) )
    DisjointClasses(
        Annotation( rdfs:label "all parts of x:collection are part-disjoint" )
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:p1 )     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050> x:p2 )
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
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( test: = <https://w3id.org/linkml/owl/tests/> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )
Prefix( RO: = <http://purl.obolibrary.org/obo/RO_> )
Prefix( PATO: = <http://purl.obolibrary.org/obo/PATO_> )
Prefix( skos: = <http://www.w3.org/2004/02/skos/core#> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )
Prefix( x: = <http://example.org/> )

Ontology( <https://w3id.org/linkml/owl/tests>
    EquivalentClasses(
        x:collection
            ObjectIntersectionOf(
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:dp1 )
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:dp2 )
            ObjectAllValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051>     ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000050>     ObjectUnionOf(
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:dp1 )
            ObjectSomeValuesFrom( <http://purl.obolibrary.org/obo/BFO_0000051> x:dp2 )
    ) ) )
    )
    )
)
```

