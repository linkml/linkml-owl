# Assorted tips and best practices

## IDE support for ontology authoring

If you are entering data in either YAML or JSON (YAML is recommended),
then you can get IDE support (e.g. autocomplete on tag names)

- Convert your schema to jsonschema using `gen-schema`
- Load this into your IDE
- When editing your yaml data file, set the schema

For info on how to do this with PyCharm see [these slides](https://docs.google.com/presentation/d/10fVBY5m89wKd8qyIvDwNHvCRnJnQx1YCXmyiVIbyNYI/edit#slide=id.p)

## Provide rich documentation

LinkML provides a rich metamodel for providing metadata about your design pattern elements.
You can provide provenance (e.g who authored it), status information,
editor-level docs, end-user level docs, etc

See

- [schema element metadata](https://linkml.io/linkml/schemas/metadata.html)

Minimally, we recommend providing at least `description` fields for all slots and all classes

## Validating data

We recommend validating:

- *input* data, using linkml data validation
- *output* owl ontologies, using robot
- internal consistency of the *schema* (pattern templates)

If source data is managed in github, set up github actions to validate

See [validating data](https://linkml.io/linkml/data/validating-data.html) in the main linkml guide

We recommend you constrain things as strictly as possible

- For example, use enums for smaller value sets
- Classes in your schema can be declared disjoint (*note this is distinct from disjointness axioms for generated classes*)
- Declare ranges for all slots
- Use `pattern` to constraint string values

Note that the general LinkML framework can be used to *structurally validate* input data,
but to *semantically validate* the OWL output you should use an OWL reasoner.

We recommend use of ROBOT and ODK to build pipelines for validating and releasing ontologies.

## Auto-filling in data

The linkml-owl framework does not provide extensive mechanisms for auto-filling data. Here auto-filling means:

- assigning default values
- assigning string fields based on format strings

These are considered *separate concerns* from mapping to OWL, and can be done upstream of linkml-owl,
including in the linkml framework itself.

However, if you are using the jinja template generation route, you
can also do a lot of auto-filling using jinja template logic
