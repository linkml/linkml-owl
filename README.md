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

## Basics

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

```owl
AnnotationAssertion(rdfs:label UBERON:1 "eye")
AnnotationAssertion(rdfs:label UBERON:2 "head")
AnnotationAssertion(rdfs:label UBERON:3 "organism")
SubClassOf( UBERON:1  ObjectSomeValuesFrom( BFO:0000050 UBERON:2))
SubClassOf( UBERON:2  ObjectSomeValuesFrom( BFO:0000050 UBERON:3))
```

See [EXAMPLES.md](EXAMPLES.md) for a complete set of examples/conformance suite

## Templates and Fstrings

The above method of annotating slots with OWL interpretations works well for cases where there is a relatively straightforward mapping between slots and axioms.

For full grained control you can use either

 * fstrings, e.g. `SubClassOf({id} {sublass_of})`, for cases with no or minimal logic
 * Jinja2 templates, for cases where control logic or advanced mappings are required

Here is an example of a more advanced schema involving nesting where we might want to model parts with counts - examples include reaction participants with stoichiometry, or protein complexes where members may be present with different counts or activation states:

```yaml
PartWithCounts:
    is_a: Anonymous
    attributes:
      unit:
        range: NamedThing
        multivalued: false
        annotations:
          owl: SomeValuesFrom
      count:
        range: integer
        minimum_value: 1
        annotations:
          owl: HasValue
      state:
        range: ActivationStateEnum
        annotations:
          owl: SomeValuesFrom

  CollectionOfPartsWithCounts:
    is_a: NamedThing
    slots:
      - has_part
    slot_usage:
      has_part:
        range: PartWithCounts
        inlined: true
    annotations:
      owl.template: |-
        {% for p in has_part %}
        SubClassOf( {{id}}
                    ObjectSomeValuesFrom( BFO:0000051
                                          ObjectIntersectionOf( {{p.unit }}
                                                                ObjectSomeValuesFrom(RO:0000053 {{p.state.meaning}})
                                                                {% if p.count %}
                                                                DataHasValue(PATO:0001555 {{p.count}})
                                                                {% endif %}
                                                              )

                                         )
                  )
        {% endfor %}
```        

Given an input file:

```yaml
id: x:collection
has_part:
  - unit: x:p1
    count: 2
    state: ACTIVATED
  - unit: x:p2
    count: 3
    state: ACTIVATED
```

(note that we use using nesting / a normalized representation here, this is harder to represent in a spreadsheet).

This will generate the following OWL:

```owl
SubClassOf( x:collection
            ObjectSomeValuesFrom( BFO:0000051
                                  ObjectIntersectionOf(
                                                       x:p1
                                                       ObjectSomeValuesFrom( RO:0000053 <http://purl.obolibrary.org/obo/PATO_0002354> )
                                                       DataHasValue( PATO:0001555 "2"^^xsd:integer ))))
SubClassOf( x:collection
            ObjectSomeValuesFrom( BFO:0000051
                                  ObjectIntersectionOf(
                                                       x:p2
                                                       ObjectSomeValuesFrom( RO:0000053 <http://purl.obolibrary.org/obo/PATO_0002354> )
                                                       DataHasValue( PATO:0001555 "3"^^xsd:integer ))))
```

## Vocabulary

Use the following keywords to annotate your schema elements:

 * Slots
    - Axiom type designators
        - SubClassOf
        - EquivalentClasses
        - AnnotationAssertion
        - ...
    - Expression modifier designators
        - ObjectSomeValuesFrom
        - ObjectAllValuesFrom
        - ...
    - Collection type designators
        - ObjectIntersectionOf
        - ObjectUnionOf
        - ...
 * Classes
    - Class
    - Individual
    - ...
    

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
* rdflib_dumper in linkml-runtime generates RDF graphs (ABoxes) from LinkML instances graphs using a standard 1:1 mapping
