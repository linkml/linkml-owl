# Quick Start

Get from zero to generated OWL in under 5 minutes.

## 1. Install

```bash
pip install linkml-owl
```

Requires Python 3.10+. This installs the `linkml-data2owl` command.

## 2. Write a schema

Create `my_schema.yaml`. This tells linkml-owl *how* your data maps to OWL:

```yaml
id: https://example.org/my-ontology
name: my-ontology
imports:
  - linkml:types

prefixes:
  linkml: https://w3id.org/linkml/
  ex: https://example.org/
  BFO: http://purl.obolibrary.org/obo/BFO_
  IAO: http://purl.obolibrary.org/obo/IAO_

default_prefix: ex
default_curi_maps:
  - semweb_context

slots:
  id:
    identifier: true
    range: uriorcurie
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  definition:
    slot_uri: IAO:0000115
    annotations:
      owl: AnnotationProperty, AnnotationAssertion
  subclass_of:
    slot_uri: rdfs:subClassOf
    range: MyClass
    multivalued: true
  part_of:
    slot_uri: BFO:0000050
    range: MyClass
    multivalued: true

classes:
  MyClass:
    slots:
      - id
      - label
      - definition
      - subclass_of
      - part_of
    slot_usage:
      subclass_of:
        annotations:
          owl: SubClassOf
      part_of:
        annotations:
          owl: ObjectSomeValuesFrom
```

Key points:

- **`slots`** describe the columns/fields in your data
- **`slot_uri`** maps a slot name to an OWL property IRI
- **`annotations: owl:`** controls what OWL axiom type is generated
- **`range`** constrains what values the slot can hold

## 3. Write your data

Create `my_data.yaml`. Each entry becomes an OWL class:

```yaml
- id: ex:Animal
  label: animal
  definition: A multicellular organism.

- id: ex:Vertebrate
  label: vertebrate
  definition: An animal with a backbone.
  subclass_of:
    - ex:Animal

- id: ex:Limb
  label: limb
  part_of:
    - ex:Vertebrate

- id: ex:Forelimb
  label: forelimb
  subclass_of:
    - ex:Limb
  part_of:
    - ex:Vertebrate
```

## 4. Generate OWL

```bash
linkml-data2owl -s my_schema.yaml -C MyClass my_data.yaml -o my_ontology.ofn
```

- `-s` — the schema file
- `-C` — the metaclass in the schema to use
- `-o` — output file (OWL Functional Syntax by default)

You can also output Turtle:

```bash
linkml-data2owl -s my_schema.yaml -C MyClass my_data.yaml -O ttl -o my_ontology.ttl
```

## 5. Inspect the output

The generated `my_ontology.ofn` will contain:

```owl
SubClassOf( ex:Vertebrate ex:Animal )
SubClassOf( ex:Forelimb ex:Limb )
SubClassOf( ex:Limb ObjectSomeValuesFrom( BFO:0000050 ex:Vertebrate ) )
SubClassOf( ex:Forelimb ObjectSomeValuesFrom( BFO:0000050 ex:Vertebrate ) )
AnnotationAssertion( rdfs:label ex:Animal "animal" )
AnnotationAssertion( rdfs:label ex:Vertebrate "vertebrate" )
AnnotationAssertion( rdfs:label ex:Limb "limb" )
AnnotationAssertion( rdfs:label ex:Forelimb "forelimb" )
AnnotationAssertion( IAO:0000115 ex:Animal "A multicellular organism." )
AnnotationAssertion( IAO:0000115 ex:Vertebrate "An animal with a backbone." )
```

Each data entry produced:

- **Annotation axioms** from `label` and `definition` (because `owl: AnnotationAssertion`)
- **SubClassOf axioms** from `subclass_of` (because `owl: SubClassOf`)
- **Existential restrictions** from `part_of` (because `owl: ObjectSomeValuesFrom`)

## What next?

- **[Basics](basics.md)** — deeper explanation of how the mapping works
- **[Examples](examples.md)** — full catalog of supported OWL constructs (equivalent classes, disjointness, templates, etc.)
- **[Templates](templates.md)** — Jinja2 templates for complex axiom patterns
- **[Comparison](comparison.md)** — how linkml-owl compares to ROBOT templates, DOSDP, and others
- **[Tutorial](tutorial/index.md)** — step-by-step pizza ontology tutorial
