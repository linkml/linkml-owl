# Relationship to OWL template languages

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

 * Clear computable description of [cardinality](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) which columns are required, which columns are multivalued etc
 * Ability to use arbitrarily nested JSON trees or RDF graphs as input
    - TSVs can still be used for "flat" schemas
 * Use of [semantic enumerations](https://linkml.io/linkml/intro/tutorial06.html)
    - for example, a field value may be restricted to two ontology terms such as "off" or "on"
 * [Translation](https://linkml.io/linkml/schemas/generators.html) of source schema to other formalisms such as JSON-Schema, JSON-LD Contexts, shape languages, SQL, ...
 * Flexible [validation](https://linkml.io/linkml/data/validating-data.html) of source input files leveraging any combination of JSON-Schema, SHACL, or ShEx
 * Powerful abilities to infer missing values
    * For example, populate a stereotypical textual definition based on slot values
 * [Generation of markdown documentation](https://linkml.io/linkml/generators/markdown.html) from source schemas

An example of a domain where this kind of rich data modeling of input
data includes generation of chemical entity ontologies from data. See
the [chemrof](https://chemkg.github.io/chemrof/) project.

The overall philosophy of linkml-owl is **composability of distinct parts**. It is a relatively lightweight library that
is only concerned with mapping or templating from a source dataset to OWL. It delegates other aspects to other libraries,
in particular the following are seen as separate concerns:

- Validation of input
- Organizing templates hierarchically
- Specifying complex rules for inferring membership of a template
- Template reuse, including reuse of core slots, and an [import](https://linkml.io/linkml/schemas/imports.html) mechanism
- Generation of documentation
- Automatic filling in of default values, and checking of consistency between dependent values
- Lexical manipulation, including pre-populating labels, synomyms, and text definitions
