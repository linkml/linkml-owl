# Templates and Fstrings

The [previous method](basics.md) of annotating slots with OWL interpretations works well for cases where there is a relatively straightforward mapping between slots and axioms.

For full grained control you can use either

 * [formatted strings](https://docs.python.org/3/tutorial/inputoutput.html), e.g. `SubClassOf({id} {sublass_of})`, for cases with no or minimal logic
 * [Jinja templates](https://jinja.palletsprojects.com/), for cases where control logic or advanced mappings are required

Either of these methods can be used to make either annotations or logical axioms

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
        SubClassOf(
          {{id}}
          ObjectSomeValuesFrom(
             BFO:0000051
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

(note that we use using nesting / a normalized representation here, this is harder to represent in a spreadsheet/TSV).

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
