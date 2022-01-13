# linkml-owl

This is an ALPHA version of a tool for translating LinkML instance data to OWL (TBoxes and ABoxes)

[LinkML](https://linkml/io/linkml) is a general purpose data modeling
language for authoring schemas to structure data. The perspective of
linkml-owl is that elements of an OWL ontology (in particular,
classes) are data elements that should conform to a schema

* [EXAMPLES.md](EXAMPLES.md)
* [SPECIFICATION.md](SPECIFICATION.md)

## Usage

```bash
linkml-data2owl -s my_schema.yaml my_data.{yaml,json,tsv,rdf} -o my_ontology.owl.ttl 
```

## How it works

First specify your schema

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
  part_of:
    slot_uri: BFO:0000050
    annotations:
      owl: SubClassOf, ObjectSomeValuesFrom
```

Then provide OWL classes as LinkML data instances using any of the standard ways of providing data in LinkML (see [working with data](https://linkml.io/linkml/data/index.html))

For example, as TSV or YAML:

```
'UBERON:1':
  label: eye
  part_of: ['UBERON:2']
'UBERON:2':
  label: head
  part_of: ['UBERON:3']
'UBERON:3':
  label: organism
  part_of: []
```

then run this through the command line tool to generate an ontology

See [EXAMPLES.md](EXAMPLES.md) for a complete set of examples/conformance suite


## Relationship to OWL template languages

Although LinkML is robust and stable, LinkML-OWL is alpha software and incomplete. For now, to convert from TSV to OWL you should for now use a dedicated environment:

 * dosdp-tools
 * robot-templates
 * ottr

For most purposes, these frameworks are also simpler and less
overhead, they treat ontology generation as a *string templating*
problem, and the emphasis is on the generation of axioms from
templates over formal descriptions of the source input file.

In contrast, linkml-owl leverages the linkml framework for rich
modeling of the source data structures used to generate the ontology,
in particular:

 * Clear computable description of which columns are required, which columns are multivalued etc
 * Ability to use arbitrarily nested JSON trees or RDF graphs as input
 * Use of [semantic enumerations](https://linkml.io/linkml/intro/tutorial06.html)
    - for example, a field value may be restricted to two ontology terms such as "off" or "on"
 * Translation of source schema to other formalisms such as JSON-Schema, JSON-LD Contexts, shape languages, SQL, ...
 * Flexible validation of source input files leveraging any combination of JSON-Schema, SHACL, or ShEx
 * Generation of markdown documentation from source schemas

An example of a domain where this kind of rich data modeling of input
data includes generation of chemical entity ontologies from data. See
the [chemrof](https://chemkg.github.io/chemrof/) project

## See Also

* [OWL Generator](https://linkml.io/linkml/generators/owl.html) in the LinkML core generates OWL from Schemas, **not** data
