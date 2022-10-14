# Basics

## Create a schema (data model)

First specify your schema using [LinkML](https://linkml.io/linkml). Note that LinkML classes will typically be *metaclasses* at the OWL level.

A very simple schema for an anatomical ontology like [Uberon](http://obofoundry.org/ontology/uberon):

```yaml
prefixes:
  UBERON: http://purl.obolibrary.org/obo/UBERON_
  BFO: http://purl.obolibrary.org/obo/BFO_
classes:
  Class:
    slots:
      - id
      - label
    class_uri: owl:Class
  AnatomicalEntityClass:
    is_a: Class
    slots:
      - part_of
     slot_usage:
       range: AnatomicalEntityClass

slots:
  id:
    identifier: true
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationAssertion
  part_of:
    slot_uri: BFO:0000050
    annotations:
      owl: SubClassOf, ObjectSomeValuesFrom
```

Without going into the mapping to OWL, we can see this simple schema
allows us to represent anatomical parts (eyes, ears, hands, etc) as data
with instances organized as a simple recursive part-of structure (e.g. finger part-of hand).

Like all LinkML schemas, URIs can be provided for schema elements. Here we are providing
URIs that map `label` in our schema to rdfs:label, and `part_of` to [BFO:000005](http://purl.obolibrary.org/obo/BFO_0000050).
These will be used in the translation.

Note the schema includes *annotations* that indicate how each schema element should map to
an OWL construct. Here we are mapping labels to [AnnotationAssertion](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities) axioms,
and mapping part-of to a combination of [SubClassOf](https://www.w3.org/TR/owl2-primer/#Class_Hierarchies) and
[SomeValuesFrom](https://www.w3.org/TR/owl2-primer/#Property_Restrictions).

## Input Data

Next we provide OWL classes as LinkML data instances, using any of the standard ways of providing data in LinkML (see [working with data](https://linkml.io/linkml/data/index.html))

For example, as TSV or YAML:

```yaml
- id: UBERON:1
  label: eye
  part_of: ['UBERON:2']
- id: UBERON:2
  label: head
  part_of: ['UBERON:3']
- id: UBERON:3
  label: organism
```

This is 3 instances of data, each with a label field populated,
and some with a part-of slot populated

## OWL Output

then run this through the command line tool to generate an ontology

```bash
linkml-data2owl -C AnatomicalEntityClass -s my_schema.yaml my_data.yaml -o my_ont.ofn
```

This generates:

```owl
AnnotationAssertion(rdfs:label UBERON:1 "eye")
AnnotationAssertion(rdfs:label UBERON:2 "head")
AnnotationAssertion(rdfs:label UBERON:3 "organism")
SubClassOf( UBERON:1  ObjectSomeValuesFrom( BFO:0000050 UBERON:2))
SubClassOf( UBERON:2  ObjectSomeValuesFrom( BFO:0000050 UBERON:3))
```

Note that the instance data on the LinkML side maps to classes and class axioms (aka TBox)
in the OWL. For example, axioms like "every eye is part of some head".

The `-C` option indicates that the `AnatomicalEntityClass` in our schema should be used.

## Type designator

The `-C` option can be omitted if you explicitly declare the
(meta)class being instantiated in the file, either using `@type` or an
slot declared a type_designator.

```yaml
- id: UBERON:1
  "@type": AnatomicalEntityClass
  label: eye
  part_of: ['UBERON:2']
- id: UBERON:2
  "@type": AnatomicalEntityClass
  label: head
  part_of: ['UBERON:3']
- id: UBERON:3
  "@type": AnatomicalEntityClass
  label: organism
```

This can be useful when you have a heterogeneous collection of objects.

## More examples

See [examples](examples.md) for a complete set of examples/conformance suite

## Different from gen-owl

The core linkml toolkit has a command [gen-owl](https://linkml.io/linkml/generators/owl.html)
which generates OWL from a LinkML *schema*.

LinkML-OWL is for generating OWL from LinkML data, according to a mapping