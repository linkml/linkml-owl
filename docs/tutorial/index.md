# LinkML-OWL Pizza Tutorial

In this tutorial we will walk through an example of how to generate a complete ontology
from *linkml data files* by transforming into OWL using the `linkml-owl` command.

Our example draws heavily from the Manchester Pizza Tutorial. You can
use the linkml tutorial without having looked at the original Pizza tutorial.
However, we assume some basic knowledge of OWL, and the Mancheser Pizza tutorial
is a great place to start!

## Pre-requisites

Note the original Manchester tutorial tells you how to create an ontology using Protege.
You don't need Protege at all for the linkml tutorial, as we will
be generating OWL from YAML files which you edit.

We strongly recommend a text editor or IDE that is YAML-aware.

You may still find it useful to have Protege at hand, as
Protege provides a very user-friendly way to look at the contents of
the OWL files we will make along the way

Some parts of the tutorial require the use of robot to perform reasoning
over the ontology. These parts can be skipped but we strongly recommend
that robot is a part of your ultimate ontology release pipeline.

You don't need any programming knowledge to do this tutorial, but initial
setup does require installation of a python module and running a script on
the command line, so basic unix concepts are helpful.

## Main LinkML tutorial

You may also find it useful to do the [linkml tutorial](https://linkml.io/linkml/intro/tutorial.html) first,
or at least to have some grasp of core linkml concepts, since linkml-owl is
simply an optional layer on top of linkml. However, if you are already familiar
with basic data modeling concepts then you may be able to wing it by diving
straight into the linkml-owl tutorial.

## Installation

See the main LinkML guide for details on installation. For this tutorial you will
not need to do any Python programming but you will need the `linkml-owl` command,
which is part of the Python distribution:

```
pip install linkml-owl
```