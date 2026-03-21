# linkml-owl Test Cases

These examples are generated automatically from test_owl_dumper

For the complete schema, see [owl_dumper_test.yaml](https://github.com/linkml/linkml-owl/blob/main/tests/inputs/owl_dumper_test.yaml)

## Annotation using literals


__Description__: _Default is to use an annotation assertion,
                  and if the range is a string then this is literal_


__Schema__:

```yaml
id: http//example.org/Annotation-using-literals
classes:
  NamedThing:
    description: generic grouping for classes, relations, individuals, and other named
      entities
    is_a: Thing
    abstract: true
    attributes:
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:a
  label: foo
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "foo")
)

```

## Annotation using IRIs


__Description__: _As above, but if the range is an instance of a LinkML class then use a literal_


__Schema__:

```yaml
id: http//example.org/Annotation-using-IRIs
classes:
  NamedThingWithMatches:
    description: test metaclass illustrating generation of skos annotation axioms
    is_a: NamedThing
    attributes:
      exactMatch:
        annotations:
          owl: AnnotationAssertion
        description: a concept that is the object of a match triple
        slot_uri: skos:exactMatch
        range: NamedThing
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:a
  exactMatch: x:b
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(skos:exactMatch x:a x:b)
)

```

## Annotation using forced literals


__Description__: _We can force a literal by imposing a range_


__Schema__:

```yaml
id: http//example.org/Annotation-using-forced-literals
classes:
  NamedThingWithMatchesAsLiterals:
    description: test metaclass illustrating generation of skos annotation axioms,
      forcing use of literals
    is_a: NamedThing
    attributes:
      exactMatch:
        annotations:
          owl: AnnotationAssertion
        description: we override the range to be a string
        slot_uri: skos:exactMatch
        range: string
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:a
  exactMatch: x:b
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(skos:exactMatch x:a "x:b")
)

```

## Axiom annotation with Literal value on annotation axiom


__Description__: _Axiom annotations (literals) can be driven by a separate slot_


__Schema__:

```yaml
id: http//example.org/Axiom-annotation-with-Literal-value-on-annotation-axiom
classes:
  DefinitionWithAxiomAnnotation:
    description: test metaclass illustrating how a text definition can be adorned
      with annotation axioms, where values are literals
    is_a: NamedThing
    attributes:
      definition_source:
        description: origin of textual definition
        slot_uri: dcterms:source
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(Annotation(dcterms:source "Me") IAO:0000115 x:a "a foo is a foo")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "foo")
)

```

## Axiom annotation with IRI val on annotation axiom


__Description__: _Axiom annotations (IRIs) can be driven by a separate slot_


__Schema__:

```yaml
id: http//example.org/Axiom-annotation-with-IRI-val-on-annotation-axiom
classes:
  DefinitionWithIRIAxiomAnnotation:
    description: test metaclass illustrating how a text definition can be adorned
      with annotation axioms, where the values are IRIs
    is_a: NamedThing
    attributes:
      definition_source:
        description: origin of textual definition
        slot_uri: dcterms:source
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(Annotation(dcterms:source x:src) IAO:0000115 x:a "a foo is a foo")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "foo")
)

```

## Axiom annotations with IRI val on annotation axiom


__Description__: _Multiple axiom annotations_


__Schema__:

```yaml
id: http//example.org/Axiom-annotations-with-IRI-val-on-annotation-axiom
classes:
  DefinitionWithIRIAxiomAnnotation:
    description: test metaclass illustrating how a text definition can be adorned
      with annotation axioms, where the values are IRIs
    is_a: NamedThing
    attributes:
      definition_source:
        description: origin of textual definition
        slot_uri: dcterms:source
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    AnnotationAssertion(Annotation(dcterms:source x:src1) Annotation(dcterms:source x:src2) IAO:0000115 x:a "a foo is a foo")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "foo")
)

```

## Basic SubClassOf between named classes


__Description__: _Adding SubClassOf annotation to the linkml class forces a SubClass axiom_


__Schema__:

```yaml
id: http//example.org/Basic-SubClassOf-between-named-classes
classes:
  Child:
    description: test metaclass illustrating classes with basic superclass parents
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: SubClassOf
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a x:b)
)

```

## basic direct equivalence between named classes


__Description__: _Adding EquivalentTo annotation to the linkml class forces an EquivalentClass axiom_


__Schema__:

```yaml
id: http//example.org/basic-direct-equivalence-between-named-classes
classes:
  DirectEquivalent:
    description: test metaclass illustrating simple equivalence between two named
      classes
    is_a: NamedThing
    attributes:
      equivalent_to:
        annotations:
          owl: EquivalentClasses
        description: named class this is equivalent to
        slot_uri: owl:equivalentClasses
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:a x:b)
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
    description: test metaclass illustrating classes with basic heirarchical existential
      parents
    is_a: NamedThing
    attributes:
      part_of:
        annotations:
          owl: ObjectSomeValuesFrom
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a ObjectSomeValuesFrom(BFO:0000050 x:b))
)

```

## SubClassOf AllValuesFrom


__Description__: _As above, but with universal restrictions_


__Schema__:

```yaml
id: http//example.org/SubClassOf-AllValuesFrom
classes:
  PartOnly:
    description: test metaclass illustrating classes with basic part-of-allValues
      pattern
    is_a: NamedThing
    attributes:
      part_of:
        annotations:
          owl: ObjectAllValuesFrom
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a ObjectAllValuesFrom(BFO:0000050 x:b))
)

```

## SubClassOf DataHasValue


__Description__: _SubClassOf DataHasValue_


__Schema__:

```yaml
id: http//example.org/SubClassOf-DataHasValue
classes:
  HasName:
    description: test metaclass illustrating data has value from
    is_a: NamedThing
    attributes:
      has_name:
        annotations:
          owl: DataHasValue
        slot_uri: schema:name
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:a
  has_name: Violet
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a DataHasValue(schema:name "Violet"))
)

```

## SubClassOf SomeValuesFrom plus label


__Description__: _Demonstrates a mix of slots, some annotation, some logical_


__Schema__:

```yaml
id: http//example.org/SubClassOf-SomeValuesFrom-plus-label
classes:
  Part:
    description: test metaclass illustrating classes with basic heirarchical existential
      parents
    is_a: NamedThing
    attributes:
      part_of:
        annotations:
          owl: ObjectSomeValuesFrom
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a ObjectSomeValuesFrom(BFO:0000050 x:b))
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "foo")
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
    description: test metaclass illustrating classes whose parents are a union
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: SubClassOf, UnionOf
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a ObjectUnionOf(x:b x:c))
)

```

## EquivalentTo Union


__Description__: _As above, but with equivalence_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-Union
classes:
  EquivUnion:
    description: test metaclass illustrating classes defined by a union
    examples:
    - value: prokaryote
      description: a prokaryote is equivalent to a bacteria or an archaea
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, UnionOf
        description: elements of the union expression
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:a ObjectUnionOf(x:b x:c))
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
    description: test metaclass illustrating classes defined by a simple intersection
      of classes
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:a ObjectIntersectionOf(x:b x:c))
)

```

## EquivalentTo Genus and SomeValuesFrom


__Description__: _All slot value interpretations are collected into a single IntersectionOf_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-Genus-and-SomeValuesFrom
classes:
  EquivGenusAndPartOf:
    description: test metaclass illustrating basic simple genus-differentia style
      logical definition, including so-called hidden GCIs
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus of the definition
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      part_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the part-of differentiae
        slot_uri: BFO:0000050
        range: NamedThing
        required: false
        multivalued: true
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
        description: other parts ofs not in the differntating conditions (sometimes
          called hidden GCIs)
        slot_uri: BFO:0000050
        range: NamedThing
        required: false
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:a ObjectIntersectionOf(x:genus ObjectSomeValuesFrom(BFO:0000050 x:b) ObjectSomeValuesFrom(BFO:0000050 x:c)))
)

```

## EquivalentTo Genus and SomeValuesFrom with AutoLabel


__Description__: _Label auto-added using string_serialization_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-Genus-and-SomeValuesFrom-with-AutoLabel
classes:
  EquivGenusAndPartOfWithAutoLabel:
    description: As EquivGenusAndPartOf, demonstrating string serialization
    is_a: NamedThing
    attributes:
      label:
        string_serialization: '{part.label} of {whole.label}'
        slot_uri: rdfs:label
      part:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus of the definition
        slot_uri: rdfs:subClassOf
        range: NamedThing
        required: true
      whole:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the part-of differentia
        slot_uri: BFO:0000050
        range: NamedThing
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true
  NamedThing:
    description: generic grouping for classes, relations, individuals, and other named
      entities
    is_a: Thing
    abstract: true
    attributes:
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:NewClass
  part: x:IN
  whole: x:H
  
-
  id: x:IN
  label: interneuron
  
-
  id: x:H
  label: hippocampus
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:NewClass ObjectIntersectionOf(x:IN ObjectSomeValuesFrom(BFO:0000050 x:H)))
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:H "hippocampus")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:IN "interneuron")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:NewClass "interneuron of hippocampus")
)

```

## EquivalentTo IntersectionOf with axiom annotation


__Description__: _as above, with axiom annotation_


__Schema__:

```yaml
id: http//example.org/EquivalentTo-IntersectionOf-with-axiom-annotation
classes:
  EquivIntersectionWithAxiomAnnotation:
    description: test metaclass illustrating classes defined by a simple intersection
      of classes, including an axion annotation
    is_a: NamedThing
    attributes:
      operands:
        annotations:
          owl: EquivalentClasses, IntersectionOf
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        range: NamedThing
        required: true
        multivalued: true
      logical_definition_source:
        description: origin of logical definition
        slot_uri: dcterms:source
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(Annotation(dcterms:source "Me") x:a ObjectIntersectionOf(x:b x:c))
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
    description: test metaclass illustrating basic simple genus-differentia style
      logical definition, including so-called hidden GCIs
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus of the definition
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      part_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the part-of differentiae
        slot_uri: BFO:0000050
        range: NamedThing
        required: false
        multivalued: true
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
        description: other parts ofs not in the differntating conditions (sometimes
          called hidden GCIs)
        slot_uri: BFO:0000050
        range: NamedThing
        required: false
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a ObjectSomeValuesFrom(BFO:0000050 x:c))
    EquivalentClasses(x:a ObjectIntersectionOf(x:genus ObjectSomeValuesFrom(BFO:0000050 x:b)))
)

```

## Hidden GCI with axiom annotations


__Description__: _End-to-end example with hidden GCIs and different axiom annotations_


__Schema__:

```yaml
id: http//example.org/Hidden-GCI-with-axiom-annotations
classes:
  EquivGenusAndPartOfWithAxiomAnnotation:
    description: test metaclass illustrating basic simple genus-differentia style
      logical definition, including axiom annotation
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      part_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: logical_definition_source
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        required: true
        multivalued: true
      other_part_ofs:
        annotations:
          owl: ObjectSomeValuesFrom
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: axiom_source
        description: for hidden GCIs
        slot_uri: BFO:0000050
        range: NamedThing
        required: false
        multivalued: true
      definition_source:
        description: origin of textual definition
        slot_uri: dcterms:source
        multivalued: true
      logical_definition_source:
        description: origin of logical definition
        slot_uri: dcterms:source
        multivalued: true
      axiom_source:
        description: origin of axiom
        slot_uri: dcterms:source
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl.axiom_annotation.slots:
            tag: owl.axiom_annotation.slots
            value: definition_source
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(Annotation(dcterms:source "Auto") x:a ObjectSomeValuesFrom(BFO:0000050 x:c))
    EquivalentClasses(Annotation(dcterms:source "Me") x:a ObjectIntersectionOf(x:genus ObjectSomeValuesFrom(BFO:0000050 x:b)))
    AnnotationAssertion(Annotation(dcterms:source "Auto") IAO:0000115 x:a "A X:genus that part_of some x:b")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:a "a")
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
    description: test metaclass illustrating a trivial example of generating an axiom
      by a simple templated string
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl.fstring:
            tag: owl.fstring
            value: SubClassOf({id} {V})
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        multivalued: true
      part_of:
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        multivalued: true
      other_part_ofs:
        description: this slot is used to indicate other part-of relationships that
          are not in the logical definition
        slot_uri: BFO:0000050
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a x:b)
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
    description: test metaclass illustrating an example of generating multiple axioms
      by a jinja template
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl.template:
            tag: owl.template
            value: '{% for p in subclass_of %}SubClassOf({{id}} {{p}}){% endfor %}'
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        multivalued: true
      part_of:
        description: element this is a part of
        slot_uri: BFO:0000050
        range: NamedThing
        multivalued: true
      other_part_ofs:
        description: this slot is used to indicate other part-of relationships that
          are not in the logical definition
        slot_uri: BFO:0000050
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:a x:b)
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
    description: test metaclass that illustrates a complex nested multi-part structure,
      where a whole is defined by a collection of repeated parts in specified states.
    is_a: NamedThing
    attributes:
      has_part:
        description: sub-elements
        slot_uri: BFO:0000051
        inverse: part_of
        range: PartWithCounts
        multivalued: true
        inlined: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 ObjectIntersectionOf(x:p1 ObjectSomeValuesFrom(RO:0000053 PATO:0002354) DataHasValue(PATO:0001555 "2"^^<http://www.w3.org/2001/XMLSchema#integer>))))
    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 ObjectIntersectionOf(x:p2 ObjectSomeValuesFrom(RO:0000053 PATO:0002354) DataHasValue(PATO:0001555 "3"^^<http://www.w3.org/2001/XMLSchema#integer>))))
)

```

## Parts collection with counts v2


__Description__: _Demonstrates tr function
                  _


__Schema__:

```yaml
id: http//example.org/Parts-collection-with-counts-v2
classes:
  CollectionOfPartsWithCounts2:
    annotations:
      owl.template:
        tag: owl.template
        value: "{% for p in has_part %}\nSubClassOf( {{id}}\n            ObjectSomeValuesFrom(\
          \ BFO:0000051\n                                  {{ tr(p) }}\n\n       \
          \                          )\n          )\n{% endfor %}"
    description: as CollectionOfPartsWithCounts but using tr function
    is_a: NamedThing
    attributes:
      has_part:
        description: sub-elements
        slot_uri: BFO:0000051
        inverse: part_of
        range: PartWithCounts2
        multivalued: true
        inlined: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 ObjectIntersectionOf(ObjectSomeValuesFrom(linkml:owl/tests/unit x:p1) DataHasValue(linkml:owl/tests/count "2"^^<http://www.w3.org/2001/XMLSchema#integer>) ObjectSomeValuesFrom(linkml:owl/tests/state PATO:0002354))))
    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 ObjectIntersectionOf(ObjectSomeValuesFrom(linkml:owl/tests/unit x:p2) DataHasValue(linkml:owl/tests/count "3"^^<http://www.w3.org/2001/XMLSchema#integer>) ObjectSomeValuesFrom(linkml:owl/tests/state PATO:0002354))))
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
    description: test metaclass illustrating a whole which has a collection of non-overlapping
      parts
    is_a: NamedThing
    attributes:
      has_part:
        description: sub-elements
        slot_uri: BFO:0000051
        inverse: part_of
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 x:p1))
    SubClassOf(x:collection ObjectSomeValuesFrom(BFO:0000051 x:p2))
    DisjointClasses(Annotation(<http://www.w3.org/2000/01/rdf-schema#label> "all parts of x:collection are part-disjoint") ObjectSomeValuesFrom(BFO:0000050 x:p1) ObjectSomeValuesFrom(BFO:0000050 x:p2))
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
    description: test metaclass illustrating a whole which is defined by a collection
      of non-overlapping parts
    is_a: NamedThing
    attributes:
      has_part:
        description: sub-elements
        slot_uri: BFO:0000051
        inverse: part_of
        range: NamedThing
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

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
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:collection ObjectIntersectionOf(ObjectSomeValuesFrom(BFO:0000051 x:dp1) ObjectSomeValuesFrom(BFO:0000051 x:dp2) ObjectAllValuesFrom(BFO:0000051 ObjectSomeValuesFrom(BFO:0000050 ObjectUnionOf(ObjectSomeValuesFrom(BFO:0000051 x:dp1) ObjectSomeValuesFrom(BFO:0000051 x:dp2))))))
)

```

## Disease SubClassOf hierarchy


__Description__: _A simple disease hierarchy using named SubClassOf parents,
                     e.g. 'lung cancer SubClassOf cancer'_


__Schema__:

```yaml
id: http//example.org/Disease-SubClassOf-hierarchy
classes:
  NamedThing:
    description: generic grouping for classes, relations, individuals, and other named
      entities
    is_a: Thing
    abstract: true
    attributes:
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true
  DiseaseClass:
    description: metaclass for disease classes with named superclass parents, modeling
      a simple disease hierarchy (e.g. lung cancer SubClassOf cancer)
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: SubClassOf
        description: named class this is subclass of
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:LungCancer
  label: lung cancer
  subclass_of:
  - x:Cancer
  
-
  id: x:Cancer
  label: cancer
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    SubClassOf(x:LungCancer x:Cancer)
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:Cancer "cancer")
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:LungCancer "lung cancer")
)

```

## Disease defined by anatomical location


__Description__: _A disease defined by genus (nervous system disorder) and
                     anatomical location differentia (brain), following the
                     Mondo disease_by_location design pattern_


__Schema__:

```yaml
id: http//example.org/Disease-defined-by-anatomical-location
classes:
  DiseaseByLocation:
    description: metaclass for diseases defined by anatomical location using a genus-differentia
      pattern (e.g. brain disease EquivalentTo nervous-system-disorder AND has-disease-location
      some brain). Follows the Mondo disease_by_location design pattern.
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus (broad disease category)
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      disease_location:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the anatomical location differentia
        slot_uri: RO:0004026
        range: NamedThing
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:BrainDisease
  label: brain disease
  subclass_of:
  - x:NervousSystemDisorder
  disease_location: x:Brain
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:BrainDisease ObjectIntersectionOf(x:NervousSystemDisorder ObjectSomeValuesFrom(RO:0004026 x:Brain)))
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:BrainDisease "brain disease")
)

```

## Disease defined by phenotype


__Description__: _A disease defined by an associated phenotype,
                     e.g. 'parkinsonism EquivalentTo disease AND has-phenotype some tremor'_


__Schema__:

```yaml
id: http//example.org/Disease-defined-by-phenotype
classes:
  DiseaseByPhenotype:
    description: metaclass for diseases defined by an associated phenotype (e.g. Parkinsonism
      EquivalentTo disease AND has-phenotype some tremor)
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus (broad disease category)
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      has_phenotype:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the phenotypic differentia
        slot_uri: RO:0002200
        range: NamedThing
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:Parkinsonism
  label: parkinsonism
  subclass_of:
  - x:Disease
  has_phenotype: x:Tremor
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:Parkinsonism ObjectIntersectionOf(x:Disease ObjectSomeValuesFrom(RO:0002200 x:Tremor)))
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:Parkinsonism "parkinsonism")
)

```

## Disease defined by location and phenotype


__Description__: _A disease defined by both location and phenotype in a single intersection,
                     illustrating multiple differentiae in one EquivalentClasses axiom_


__Schema__:

```yaml
id: http//example.org/Disease-defined-by-location-and-phenotype
classes:
  DefinedDisease:
    description: metaclass for diseases defined by both anatomical location AND phenotype,
      illustrating intersection with multiple differentiae (e.g. a disease EquivalentTo
      disease AND has-location some L AND has-phenotype some P)
    is_a: NamedThing
    attributes:
      subclass_of:
        annotations:
          owl: EquivalentClasses, IntersectionOf
        description: the genus
        slot_uri: rdfs:subclass_of
        range: NamedThing
        required: true
        multivalued: true
      disease_location:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the anatomical location differentia
        slot_uri: RO:0004026
        range: NamedThing
        required: true
      has_phenotype:
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
        description: the phenotypic differentia
        slot_uri: RO:0002200
        range: NamedThing
        required: true
      id:
        description: the CURIE or IRI of the focal element
        identifier: true
        range: uriorcurie
        required: true
      label:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a descriptive name/label for an element
        slot_uri: rdfs:label
        recommended: true
      definition:
        annotations:
          owl: AnnotationProperty, AnnotationAssertion
        description: a human-readable definition of an element
        slot_uri: IAO:0000115
        recommended: true

```


__Input__:

```yaml
-
  id: x:BrainNeuropathy
  label: brain neuropathy
  subclass_of:
  - x:Neuropathy
  disease_location: x:Brain
  has_phenotype: x:Tremor
  
```

__Generated axioms__:

```
Prefix(linkml:=<https://w3id.org/linkml/>)
Prefix(test:=<https://w3id.org/linkml/owl/tests/>)
Prefix(BFO:=<http://purl.obolibrary.org/obo/BFO_>)
Prefix(IAO:=<http://purl.obolibrary.org/obo/IAO_>)
Prefix(RO:=<http://purl.obolibrary.org/obo/RO_>)
Prefix(PATO:=<http://purl.obolibrary.org/obo/PATO_>)
Prefix(MONDO:=<http://purl.obolibrary.org/obo/MONDO_>)
Prefix(HP:=<http://purl.obolibrary.org/obo/HP_>)
Prefix(UBERON:=<http://purl.obolibrary.org/obo/UBERON_>)
Prefix(skos:=<http://www.w3.org/2004/02/skos/core#>)
Prefix(dcterms:=<http://purl.org/dc/terms/>)
Prefix(schema:=<http://schema.org/>)
Prefix(x:=<http://example.org/>)
Ontology(    EquivalentClasses(x:BrainNeuropathy ObjectIntersectionOf(x:Neuropathy ObjectSomeValuesFrom(RO:0004026 x:Brain) ObjectSomeValuesFrom(RO:0002200 x:Tremor)))
    AnnotationAssertion(<http://www.w3.org/2000/01/rdf-schema#label> x:BrainNeuropathy "brain neuropathy")
)

```

