# Examples

This page showcases the range of OWL constructs that linkml-owl can generate,
from simple annotations to complex axiom patterns. Each example includes the
relevant schema fragment, input data, and generated OWL (in OWL Functional Syntax).

For a full working schema, see [anatomy-schema.yaml](https://github.com/linkml/linkml-owl/blob/main/docs/example-schemas/anatomy-schema.yaml)
and for the complete conformance suite, see [owl_dumper_test.yaml](https://github.com/linkml/linkml-owl/blob/main/tests/inputs/owl_dumper_test.yaml).

## Annotations (labels, definitions, synonyms)

The default behavior maps string-valued slots to `AnnotationAssertion` axioms.
Use `slot_uri` to control which annotation property is used.

**Schema:**

```yaml
slots:
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  definition:
    slot_uri: IAO:0000115
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  synonym:
    slot_uri: skos:altLabel
    multivalued: true
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
```

**Input:**

```yaml
- id: UBERON:0000970
  label: eye
  definition: An organ of sight.
  synonym:
    - oculus
```

**Generated OWL:**

```owl
AnnotationAssertion( rdfs:label UBERON:0000970 "eye" )
AnnotationAssertion( IAO:0000115 UBERON:0000970 "An organ of sight." )
AnnotationAssertion( skos:altLabel UBERON:0000970 "oculus" )
```

## Annotations using IRIs

When the range of a slot is another LinkML class (not a string), the annotation
value is an IRI rather than a literal.

**Schema:**

```yaml
slots:
  exactMatch:
    slot_uri: skos:exactMatch
    range: NamedThing
    annotations:
      owl: AnnotationAssertion
```

**Input:**

```yaml
- id: x:a
  exactMatch: x:b
```

**Generated OWL:**

```owl
AnnotationAssertion( skos:exactMatch x:a x:b )
```

To force a literal value instead, override the range to `string`.

## Existential restrictions (SomeValuesFrom)

The most common pattern in biomedical ontologies: "every X is related to some Y."

**Schema:**

```yaml
slots:
  part_of:
    slot_uri: BFO:0000050
    range: AnatomicalStructure
    multivalued: true

classes:
  AnatomicalStructure:
    slots:
      - id
      - label
      - part_of
    slot_usage:
      part_of:
        annotations:
          owl: ObjectSomeValuesFrom
```

**Input:**

```yaml
- id: UBERON:0000970
  label: eye
  part_of:
    - UBERON:0000033

- id: UBERON:0000033
  label: head
  part_of:
    - UBERON:0000468
```

**Generated OWL:**

```owl
SubClassOf( UBERON:0000970 ObjectSomeValuesFrom( BFO:0000050 UBERON:0000033 ) )
SubClassOf( UBERON:0000033 ObjectSomeValuesFrom( BFO:0000050 UBERON:0000468 ) )
AnnotationAssertion( rdfs:label UBERON:0000970 "eye" )
AnnotationAssertion( rdfs:label UBERON:0000033 "head" )
```

In English: "every eye is part of some head" and "every head is part of some organism."

## Universal restrictions (AllValuesFrom)

To express that *all* fillers of a relationship must be of a given type:

**Schema:**

```yaml
classes:
  PartOnly:
    slots:
      - id
      - part_of
    slot_usage:
      part_of:
        annotations:
          owl: ObjectAllValuesFrom
```

**Input:**

```yaml
- id: x:finger
  part_of:
    - x:hand
```

**Generated OWL:**

```owl
SubClassOf( x:finger ObjectAllValuesFrom( BFO:0000050 x:hand ) )
```

In English: "everything a finger is part of is a hand."

## SubClassOf (named superclasses)

Direct named superclass axioms, without any restriction:

**Schema:**

```yaml
slots:
  subclass_of:
    slot_uri: rdfs:subClassOf
    range: NamedThing
    multivalued: true

classes:
  Child:
    slots:
      - id
      - subclass_of
    slot_usage:
      subclass_of:
        annotations:
          owl: SubClassOf
```

**Input:**

```yaml
- id: x:cat
  subclass_of:
    - x:mammal
    - x:carnivore
```

**Generated OWL:**

```owl
SubClassOf( x:cat x:mammal )
SubClassOf( x:cat x:carnivore )
```

## Equivalent class definitions (genus-differentia)

The hallmark of OBO-style ontologies: define a class as the intersection of
a genus (broad category) and one or more differentiae (distinguishing relationships).

**Schema:**

```yaml
classes:
  DefinedAnatomicalStructure:
    slots:
      - id
      - label
      - genus
      - differentia_part_of
    slot_usage:
      genus:
        slot_uri: rdfs:subClassOf
        range: AnatomicalStructure
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
      differentia_part_of:
        slot_uri: BFO:0000050
        range: AnatomicalStructure
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
```

**Input:**

```yaml
- id: UBERON:0004801
  label: lens of camera-type eye
  genus: UBERON:0000389
  differentia_part_of: UBERON:0000019
```

**Generated OWL:**

```owl
EquivalentClasses(
  UBERON:0004801
  ObjectIntersectionOf(
    UBERON:0000389
    ObjectSomeValuesFrom( BFO:0000050 UBERON:0000019 )
  )
)
```

In English: "a lens of camera-type eye is equivalent to a lens that is part of some camera-type eye."

## Hidden GCIs (additional necessary conditions)

Sometimes a class has both a logical definition (EquivalentClasses) and
additional SubClassOf axioms that go beyond the definition. These are often
called "hidden GCIs" (General Class Inclusions).

**Schema:**

```yaml
classes:
  EquivGenusAndPartOf:
    slots:
      - id
      - subclass_of
      - part_of
      - other_part_ofs
    slot_usage:
      subclass_of:
        description: the genus of the definition
        annotations:
          owl: EquivalentClasses, IntersectionOf
      part_of:
        description: differentia in the equivalence axiom
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
      other_part_ofs:
        description: additional SubClassOf conditions (hidden GCIs)
        annotations:
          owl: ObjectSomeValuesFrom
```

**Input:**

```yaml
- id: x:finger-of-hand
  subclass_of:
    - x:finger
  part_of:
    - x:hand
  other_part_ofs:
    - x:forelimb
```

**Generated OWL:**

```owl
EquivalentClasses(
  x:finger-of-hand
  ObjectIntersectionOf(
    x:finger
    ObjectSomeValuesFrom( BFO:0000050 x:hand )
  )
)
SubClassOf( x:finger-of-hand ObjectSomeValuesFrom( BFO:0000050 x:forelimb ) )
```

## Union classes

Use `UnionOf` to define a class as the union of its members:

**Schema:**

```yaml
classes:
  EquivUnion:
    slots:
      - id
      - operands
    slot_usage:
      operands:
        annotations:
          owl: EquivalentClasses, UnionOf
```

**Input:**

```yaml
- id: x:prokaryote
  operands:
    - x:bacteria
    - x:archaea
```

**Generated OWL:**

```owl
EquivalentClasses(
  x:prokaryote
  ObjectUnionOf( x:bacteria x:archaea )
)
```

## Disjoint unions

Declare that a set of classes is both a union and pairwise disjoint:

**Schema:**

```yaml
classes:
  DisjointUnion:
    slots:
      - id
      - operands
    slot_usage:
      operands:
        annotations:
          owl: DisjointUnion
```

**Input:**

```yaml
- id: x:cell
  operands:
    - x:neuron
    - x:epithelial_cell
    - x:muscle_cell
```

**Generated OWL:**

```owl
DisjointUnion( x:cell x:neuron x:epithelial_cell x:muscle_cell )
```

## Data properties

Map slots to OWL DataPropertyAssertion or DataHasValue axioms:

**Schema:**

```yaml
slots:
  has_name:
    slot_uri: schema:name
    annotations:
      owl: DataHasValue
```

**Input:**

```yaml
- id: x:bob
  has_name: Robert
```

**Generated OWL:**

```owl
SubClassOf( x:bob DataHasValue( schema:name "Robert" ) )
```

For individual-level data property assertions, use `DataPropertyAssertion`:

```yaml
slots:
  weight:
    range: float
    annotations:
      owl: DatatypeProperty, DataPropertyAssertion
```

## Enums mapped to ontology terms

LinkML enums with `meaning` annotations map enum values to OWL named entities.
When used with `ObjectSomeValuesFrom`, enum values become class fillers:

**Schema:**

```yaml
enums:
  LateralityEnum:
    permissible_values:
      LEFT:
        meaning: PATO:0000346
      RIGHT:
        meaning: PATO:0000344

slots:
  has_laterality:
    range: LateralityEnum
    annotations:
      owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
```

**Input:**

```yaml
- id: x:left-eye
  parent: x:eye
  has_laterality: LEFT
```

**Generated OWL:**

```owl
EquivalentClasses(
  x:left-eye
  ObjectIntersectionOf(
    x:eye
    ObjectSomeValuesFrom( RO:0000053 PATO:0000346 )
  )
)
```

The `LEFT` enum value is resolved to its `meaning` IRI (`PATO:0000346`).

## Individuals and class assertions

To generate OWL individuals (ABox) instead of classes (TBox), set the
class-level `owl` annotation to `NamedIndividual`:

**Schema:**

```yaml
classes:
  CreatureInstance:
    annotations:
      owl: NamedIndividual
    slot_usage:
      instance_of:
        slot_uri: rdf:type
        annotations:
          owl: ClassAssertion
      has_location:
        annotations:
          owl: ObjectPropertyAssertion
```

**Input:**

```yaml
- id: mnm:goblin-1
  instance_of:
    - mnm:Goblin
  has_location: mnm:dark-cave
```

**Generated OWL:**

```owl
ClassAssertion( mnm:Goblin mnm:goblin-1 )
ObjectPropertyAssertion( mnm:has_location mnm:goblin-1 mnm:dark-cave )
```

## Axiom annotations

Annotate axioms themselves (not just entities). For example, attach a source
to a definition:

**Schema:**

```yaml
classes:
  DefinitionWithAxiomAnnotation:
    slots:
      - id
      - definition
      - definition_source
    slot_usage:
      definition:
        annotations:
          owl.axiom_annotation.slots: definition_source
```

**Input:**

```yaml
- id: x:a
  definition: a foo is a foo
  definition_source:
    - Me
```

**Generated OWL:**

```owl
AnnotationAssertion(
  Annotation( dcterms:source "Me" )
  IAO:0000115 x:a "a foo is a foo"
)
```

The `definition_source` value becomes an annotation on the definition axiom itself.

## Jinja templates for complex axioms

For axiom patterns that go beyond what annotations can express, use Jinja2 templates.

### Parts with disjointness

**Schema:**

```yaml
classes:
  OrganWithParts:
    slots:
      - id
      - has_part
    annotations:
      owl.template: |-
        {% for p in has_part %}
        SubClassOf( {{id}} ObjectSomeValuesFrom( BFO:0000051 {{p}} ) )
        {% endfor %}
        DisjointClasses(
          {% for p in has_part %}
          ObjectSomeValuesFrom( BFO:0000050 {{p}} )
          {% endfor %}
        )
```

**Input:**

```yaml
- id: UBERON:0015228
  label: limb
  has_part:
    - UBERON:0003821
    - UBERON:0003822
    - UBERON:0003823
```

**Generated OWL:**

```owl
SubClassOf( UBERON:0015228 ObjectSomeValuesFrom( BFO:0000051 UBERON:0003821 ) )
SubClassOf( UBERON:0015228 ObjectSomeValuesFrom( BFO:0000051 UBERON:0003822 ) )
SubClassOf( UBERON:0015228 ObjectSomeValuesFrom( BFO:0000051 UBERON:0003823 ) )
DisjointClasses(
  ObjectSomeValuesFrom( BFO:0000050 UBERON:0003821 )
  ObjectSomeValuesFrom( BFO:0000050 UBERON:0003822 )
  ObjectSomeValuesFrom( BFO:0000050 UBERON:0003823 )
)
```

### Nested structures with counts

Templates can iterate over nested/inlined objects. This example models
parts of a complex with stoichiometry and activation states:

**Schema:**

```yaml
classes:
  PartWithCounts:
    annotations:
      owl: AnonymousClassExpression
    attributes:
      unit:
        range: NamedThing
        annotations:
          owl: SomeValuesFrom
      count:
        range: integer
        annotations:
          owl: HasValue
      state:
        range: ActivationStateEnum
        annotations:
          owl: SomeValuesFrom

  CollectionOfPartsWithCounts:
    slots:
      - has_part
    slot_usage:
      has_part:
        range: PartWithCounts
        inlined: true
    annotations:
      owl.template: |-
        {% for p in has_part %}
        SubClassOf( {{id}}
          ObjectSomeValuesFrom( BFO:0000051
            ObjectIntersectionOf( {{p.unit}}
              ObjectSomeValuesFrom( RO:0000053 {{p.state.meaning}} )
              {% if p.count %}
              DataHasValue( PATO:0001555 "{{p.count}}"^^xsd:integer )
              {% endif %}
            )
          )
        )
        {% endfor %}
```

**Input:**

```yaml
- id: x:complex-p1-p2
  has_part:
    - unit: x:p1
      count: 2
      state: ACTIVATED
    - unit: x:p2
      count: 3
      state: ACTIVATED
```

**Generated OWL:**

```owl
SubClassOf( x:complex-p1-p2
  ObjectSomeValuesFrom( BFO:0000051
    ObjectIntersectionOf( x:p1
      ObjectSomeValuesFrom( RO:0000053 PATO:0002354 )
      DataHasValue( PATO:0001555 "2"^^xsd:integer )
    )
  )
)
SubClassOf( x:complex-p1-p2
  ObjectSomeValuesFrom( BFO:0000051
    ObjectIntersectionOf( x:p2
      ObjectSomeValuesFrom( RO:0000053 PATO:0002354 )
      DataHasValue( PATO:0001555 "3"^^xsd:integer )
    )
  )
)
```

### F-string shorthand

For simple one-line axiom patterns, use `owl.fstring` instead of a full Jinja template:

```yaml
slot_usage:
  subclass_of:
    annotations:
      owl.fstring: SubClassOf({id} {V})
```

Here `{id}` refers to the identifier of the focal element, and `{V}` to the slot value.

## GCI propagation meta-patterns

Templates can express *meta-patterns* for ontology design, such as propagation
rules for General Class Inclusions (GCIs):

**Schema:**

```yaml
classes:
  GCIPropagationMetapattern:
    mixin: true
    attributes:
      genus:
        range: NamedThing
      differentia_relation:
        range: NamedThing
      differentia_filler:
        range: NamedThing
      inferred_predicate:
        range: NamedThing
      propagation_relation:
        range: NamedThing
    annotations:
      owl.template: |-
        SubClassOf(
          ObjectSomeValuesFrom(
            ObjectIntersectionOf( {{genus}}
              ObjectSomeValuesFrom(
                {{differentia_relation}}
                ObjectSomeValuesFrom( {{propagation_relation}}
                                      {{differentia_filler}} ))))
          ObjectSomeValuesFrom(
            {{inferred_predicate}}
            ObjectIntersectionOf( {{genus}}
              ObjectSomeValuesFrom(
                {{differentia_relation}}
                {{differentia_filler}} )))
```

This generates GCI axioms of the form: if something is a *genus* that has
*differentia_relation* to something that *propagation_relation* to *differentia_filler*,
then it also has *inferred_predicate* to a *genus* with *differentia_relation*
to *differentia_filler*.

## Real-world example: Disease ontology (Mondo-style)

Disease ontologies like [Mondo](https://mondo.monarchinitiative.org/) use genus-differentia
patterns extensively. Here we show how linkml-owl models the "disease by anatomical location"
pattern that accounts for hundreds of Mondo classes.

**Schema** (see [disease-schema.yaml](https://github.com/linkml/linkml-owl/blob/main/docs/example-schemas/disease-schema.yaml)):

```yaml
prefixes:
  MONDO: http://purl.obolibrary.org/obo/MONDO_
  UBERON: http://purl.obolibrary.org/obo/UBERON_
  RO: http://purl.obolibrary.org/obo/RO_
  IAO: http://purl.obolibrary.org/obo/IAO_

slots:
  subclass_of:
    slot_uri: rdfs:subClassOf
    range: Disease
    multivalued: true
  location:
    slot_uri: RO:0004026
    range: Disease
    description: anatomical location of the disease

classes:
  DiseaseByLocation:
    description: >-
      A disease defined by its anatomical location (genus + differentia).
    slots:
      - id
      - label
      - definition
      - subclass_of
      - location
    slot_usage:
      subclass_of:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
      location:
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
```

**Input:**

```yaml
- id: MONDO:0005560
  label: brain disease
  definition: A disease affecting the brain.
  subclass_of:
    - MONDO:0005071
  location: UBERON:0000955
```

**Generated OWL:**

```owl
EquivalentClasses(
  MONDO:0005560
  ObjectIntersectionOf(
    MONDO:0005071
    ObjectSomeValuesFrom( RO:0004026 UBERON:0000955 )
  )
)
AnnotationAssertion( rdfs:label MONDO:0005560 "brain disease" )
AnnotationAssertion( IAO:0000115 MONDO:0005560 "A disease affecting the brain." )
```

In English: "brain disease is equivalent to a nervous system disorder that has disease location some brain."

### Disease with inheritance (template-based)

When you need conditional logic — e.g. only adding an inheritance axiom when the
field is populated — use a Jinja template:

```yaml
classes:
  DiseaseWithInheritance:
    slots:
      - id
      - subclass_of
    attributes:
      inheritance:
        range: InheritanceEnum
    annotations:
      owl.template: |-
        {% for sc in subclass_of %}
        SubClassOf( {{id}} {{sc}} )
        {% endfor %}
        {% if inheritance %}
        SubClassOf( {{id}} ObjectSomeValuesFrom( RO:0000053 {{inheritance.meaning}} ) )
        {% endif %}

enums:
  InheritanceEnum:
    permissible_values:
      AUTOSOMAL_DOMINANT:
        meaning: HP:0000006
      AUTOSOMAL_RECESSIVE:
        meaning: HP:0000007
```

**Input:**

```yaml
- id: MONDO:0007915
  label: Marfan syndrome
  subclass_of:
    - MONDO:0003900
  inheritance: AUTOSOMAL_DOMINANT
```

**Generated OWL:**

```owl
SubClassOf( MONDO:0007915 MONDO:0003900 )
SubClassOf( MONDO:0007915 ObjectSomeValuesFrom( RO:0000053 HP:0000006 ) )
```

## Real-world example: Phenotype ontology (EQ decomposition)

Phenotype ontologies like [HPO](https://hpo.jax.org/) and [uPheno](https://obophenotype.github.io/upheno/)
define phenotypes using an Entity-Quality (EQ) decomposition: a phenotype is a
quality that inheres in an anatomical entity.

**Schema** (see [phenotype-schema.yaml](https://github.com/linkml/linkml-owl/blob/main/docs/example-schemas/phenotype-schema.yaml)):

```yaml
prefixes:
  HP: http://purl.obolibrary.org/obo/HP_
  UBERON: http://purl.obolibrary.org/obo/UBERON_
  PATO: http://purl.obolibrary.org/obo/PATO_

enums:
  QualityModifierEnum:
    permissible_values:
      INCREASED:
        meaning: PATO:0000462
      DECREASED:
        meaning: PATO:0000463
      ABNORMAL:
        meaning: PATO:0000460

classes:
  EntityQualityPhenotype:
    attributes:
      entity:
        range: EntityQualityPhenotype
        required: true
        description: the anatomical entity affected
      quality:
        range: QualityModifierEnum
        required: true
        description: the quality modifier
      genus:
        range: EntityQualityPhenotype
        required: true
        slot_uri: rdfs:subClassOf
    annotations:
      owl.template: |-
        EquivalentClasses(
          {{id}}
          ObjectIntersectionOf(
            {{genus}}
            ObjectSomeValuesFrom( BFO:0000051
              ObjectIntersectionOf(
                {{quality.meaning}}
                ObjectSomeValuesFrom( RO:0000052
                  ObjectSomeValuesFrom( BFO:0000050 {{entity}} )
                )
              )
            )
          )
        )
```

**Input:**

```yaml
- id: HP:0001263
  label: Abnormal brain morphology
  definition: An abnormality of the brain.
  genus: HP:0000118
  entity: UBERON:0000955
  quality: ABNORMAL
```

**Generated OWL:**

```owl
EquivalentClasses(
  HP:0001263
  ObjectIntersectionOf(
    HP:0000118
    ObjectSomeValuesFrom( BFO:0000051
      ObjectIntersectionOf(
        PATO:0000460
        ObjectSomeValuesFrom( RO:0000052
          ObjectSomeValuesFrom( BFO:0000050 UBERON:0000955 )
        )
      )
    )
  )
)
```

In English: "Abnormal brain morphology is equivalent to a phenotypic abnormality
that has-part some (abnormal quality that inheres-in something part-of some brain)."

The enum `ABNORMAL` is automatically resolved to `PATO:0000460` via its `meaning` field.
This pattern scales to hundreds of phenotype terms by adding rows to the data file.

## Integration with existing ontologies

LinkML-OWL uses CURIEs and prefix maps to integrate with existing OWL ontologies.
Declare prefixes for the ontologies you reference:

```yaml
prefixes:
  UBERON: http://purl.obolibrary.org/obo/UBERON_
  CL: http://purl.obolibrary.org/obo/CL_
  GO: http://purl.obolibrary.org/obo/GO_
  BFO: http://purl.obolibrary.org/obo/BFO_
  RO: http://purl.obolibrary.org/obo/RO_
  CHEBI: http://purl.obolibrary.org/obo/CHEBI_
```

Then use CURIEs freely in both schemas and data:

```yaml
- id: GO:0006915
  label: apoptotic process
  part_of:
    - GO:0012501
  has_participant:
    - CHEBI:18243
```

This generates axioms using the full IRIs:

```owl
SubClassOf(
  <http://purl.obolibrary.org/obo/GO_0006915>
  ObjectSomeValuesFrom(
    <http://purl.obolibrary.org/obo/BFO_0000050>
    <http://purl.obolibrary.org/obo/GO_0012501>
  )
)
```

## Running the examples

Convert data to OWL using the command line:

```bash
# Specify the metaclass explicitly
linkml-data2owl -s anatomy-schema.yaml -C AnatomicalStructure anatomy-data.yaml -o anatomy.ofn

# Use @type in the data to auto-detect the metaclass
linkml-data2owl -s anatomy-schema.yaml anatomy-data.yaml -o anatomy.ofn

# Output as Turtle instead of OWL Functional Syntax
linkml-data2owl -s anatomy-schema.yaml -C AnatomicalStructure anatomy-data.yaml -O ttl -o anatomy.ttl
```

## Summary of OWL annotation keywords

| Annotation keyword | OWL construct generated |
|---|---|
| `AnnotationAssertion` | AnnotationAssertion axiom |
| `AnnotationProperty` | Declares the slot as an annotation property |
| `SubClassOf` | SubClassOf axiom (named superclass) |
| `EquivalentClasses` | EquivalentClasses axiom |
| `ObjectSomeValuesFrom` | Existential restriction (SubClassOf by default) |
| `ObjectAllValuesFrom` | Universal restriction |
| `IntersectionOf` | ObjectIntersectionOf (combine with EquivalentClasses) |
| `UnionOf` | ObjectUnionOf |
| `DisjointUnion` | DisjointUnion axiom |
| `DataHasValue` | Data has-value restriction |
| `DataPropertyAssertion` | Data property assertion (ABox) |
| `ObjectPropertyAssertion` | Object property assertion (ABox) |
| `ClassAssertion` | Class assertion (rdf:type for individuals) |
| `NamedIndividual` | Declares instances as OWL individuals |

Multiple keywords can be combined with commas, e.g. `owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom`.
