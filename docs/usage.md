# Installation and Usage

## Installation

```bash
pip install linkml-owl
```

## Usage

Minimally you need to specify two inputs:

* A [linkml schema](https://linkml.io/linkml/schemas), with annotations describing mappings
* A datafile in YAML, JSON, RDF, or TSV conformant with the schema

To convert:

```bash
linkml-data2owl -s my_schema.yaml my_data.{yaml,json,tsv,rdf} -o my_ontology.owl.ttl 
```

For all options, see:

```bash
linkml-data2owl --help
```

