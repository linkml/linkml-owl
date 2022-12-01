# Auto-filling

## Introduction

Sometimes it is convenient to auto-fill lexical fields and other annotation properties,
following templated patterns.

For example, given a data model for cars where cars have three slots, *make*, *color*, and *model*,
we may want to auto-populate rdfs:label using the template `{color} (make} {model}`.

## Usage

This can be done by providing additional information in the YAML file, as follows:

```yaml
classes:
    NamedThing:
      slots:
        - id
        - label
    Car:
        is_a: NamedThing
        slots:
          - make
          - color
          - model
        slot_usage:
            label:
                string_serialization: "{color.label} {make.label} {model.label}"
```

Note that for this to work, the range of *make*, *color*, and *model* must be an is_a child of NamedThing, or otherwise
have a *label* slot.

Then, when calling `linkml-data2owl`, pass the `--autofill` flag.

This will populate the *label* slot of each car with a string such as "red Toyota Camry".

Note that this functionality is not part of LinkML-OWL, rather it is part of the core
LinkML framework. More information can be found in the documentation for [inferring missing values](https://linkml.io/linkml/developers/inference.html) on
the main LinkML site.

## Comparison with OWL templating systems

The DOSDP OWL templating system uses a uniform templating mechanism for generating both structured OWL axioms and lexical annotations.

In contrast, LinkML-OWL treats these as separate concerns.

- Mapping to OWL-axioms is largely considered a *mapping* problem (although [templates](templates.md) can be used).
- Procedures for auto-filling missing values is treated as distinct from OWL mapping and is a general data-level functionality,

