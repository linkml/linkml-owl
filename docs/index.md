# linkml-owl

## Overview

A framework for translating LinkML instance data to OWL Ontologies (TBoxes and ABoxes)

![img](images/LinkML-OWL-fig.png)

## Background

[LinkML](https://linkml/io/linkml) is a general purpose data modeling
language for authoring schemas to structure data. The perspective of
linkml-owl is that elements of an OWL ontology (in particular,
classes) are data elements that should conform to a schema

[OWL](https://www.w3.org/OWL/) is a semantic web language for representing
ontologies. Large OWL ontologies consisting of many classes and axioms are common
in fields like health, biology, environmental science, and material science.

OWL is usually authored in a dedicated editing environment like Protege,
but in many cases we want to automate producing parts of ontologies, or
automatically translate data or databases to ontologies.

LinkML-OWL is a framework for mapping arbitrarily shaped data into potentially
complex OWL constructs.