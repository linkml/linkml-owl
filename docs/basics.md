# Basics

First specify your schema using LinkML. Note that LinkML classes will typically be *metaclasses*.

A very simple schema for an anatomical ontology:

```yaml
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
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationAssertion
  part_of:
    slot_uri: BFO:0000050
    annotations:
      owl: SubClassOf, ObjectSomeValuesFrom
```

Then provide OWL classes as LinkML data instances using any of the standard ways of providing data in LinkML (see [working with data](https://linkml.io/linkml/data/index.html))

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
