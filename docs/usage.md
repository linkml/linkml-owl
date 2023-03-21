# Installation and Usage

## Installation

LinkML-OWL is pure python and can be installed from PyPI:

```bash
pip install linkml-owl
```

You will need Python 3.8 or higher.

This will give you the command line tools you need. 

## Usage

Minimally you need to specify two inputs:

* A [linkml schema](https://linkml.io/linkml/schemas), with *annotations* describing mappings from data to OWL
* A datafile in YAML, JSON, RDF, or TSV conformant with the schema

To convert:

```bash
linkml-data2owl -s my_schema.yaml my_data.{yaml,json,tsv,rdf} -o my_ontology.ofn
```

For all options, see:

```bash
linkml-data2owl --help
```

