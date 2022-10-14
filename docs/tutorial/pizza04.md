# Part 4: Refactoring to use inheritance

In previous parts we noticed a lot of repetition in our schema
definitions, in that we were repeating the same information for
attributes when the same attribute was used across classes.

In this section we will see how to refactor the schema to make use of
LinkML reuse features. It may help to refer to the LinkML core docs
for explanations of some of these concepts; in particular:

1. We will use [slots](https://linkml.io/linkml/schemas/slots.html) that are reusable across classes
2. We will use [inheritance](https://linkml.io/linkml/schemas/inheritance.html) to place shared slots in a superclass
3. We will use [slot usage](https://linkml.io/linkml/schemas/slots.html#slot-usage) to refine usage of a slot in the context of a class

## Schema

Here is the revised schema:

```yaml
id: http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl
name: Pizza-Ontology-Metamodel
prefixes:
  pizza: http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl#
  linkml: https://w3id.org/linkml/
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
default_curi_maps:
    - semweb_context
default_prefix: pizza
imports:
  - linkml:types

classes:

  ## ---
  ## Mixins
  ## ---
  Named:
    mixin: true
    slots:
      - id
      - label
      - altLabels
      - definition
      - conforms_to
  InstanceAspect:
    mixin: true
    slots:
      - typeOf
    annotations:
      owl: Individual
  ClassAspect:
    mixin: true
    slots:
      - subClassOf
    annotations:
      owl: Class

  ## ---
  ## Main Food Template Hierarchy
  ## ---
  Food:
    description: grouping template for various foodstuffs
    slots:
      - conforms_to
    
  Pizza:
    is_a: Food
    slots:
      - hasBase
      - hasToppings
      - hasCountryOfOrigin
  NamedPizza:
    slots:
      - id
    is_a: Pizza
    mixins:
      - ClassAspect
      - Named
    slot_usage:
      subClassOf:
        range: NamedPizza
      hasBase:
        annotations:
          owl: ObjectSomeValuesFrom
      hasToppings:
        annotations:
          owl: ObjectSomeValuesFrom

  PizzaBase:
    is_a: Food
    mixins:
      - ClassAspect
      - Named
  PizzaTopping:
    is_a: Food
    mixins:
      - ClassAspect
      - Named
  Country:
    mixins:
      - InstanceAspect
      - Named
    annotations:
      owl: Class
    slots:
      - typeOf
    comments:
      - A class that is equivalent to the set of individuals that are described in the
        enumeration - ie Countries can only be either America, England, France, Germany
        or Italy and nothing else. Note that these individuals have been asserted to
        be allDifferent from each other.@en

slots:
  id:
    identifier: true
    range: uriorcurie
  conforms_to:
    designates_type: true
    slot_uri: dcterms:conformsTo
    range: string
    annotations:
      owl.fstring: |-
        AnnotationAssertion( dcterms:conformsTo {id} pizza:{V} )
  label:
    slot_uri: rdfs:label
    annotations:
      owl: AnnotationAssertion
  subClassOf:
    slot_uri: rdfs:subClassOf
    range: Named
    annotations:
      owl: SubClassOf
  typeOf:
    slot_uri: rdf:type
    range: Named
    annotations:
      owl: ClassAssertion
  hasBase:
    range: PizzaBase
    is_a: hasIngredient
    multivalued: true
    annotations:
      owl: ObjectProperty
  hasToppings:
    singular_name: hasTopping
    range: PizzaTopping
    is_a: hasIngredient
    multivalued: true
    annotations:
      owl: ObjectProperty
  hasCountryOfOrigin:
    multivalued: true
    annotations:
      owl: ObjectHasValue, ObjectProperty
    range: Country
  hasIngredient:
    multivalued: true
    annotations:
      owl: ObjectProperty
    range: Food
  altLabels:
    singular_name: altLabel
    slot_uri: skos:altLabel
    multivalued: true
  definition:
    slot_uri: skos:definition
    multivalued: true

```

## Explanation

- we have placed very generic slots that apply to anyything with an id in `Named`
- we treat being a class vs an instance as an *aspect* - the advantages of this will be shown later in this tutorial
- slots now have their own section at the end
   - slots do not inherently 'belong' to any class, and can be used by any class
   - a class that wants to use a slot simply lists it in their 'slots' section
- we refine usage of slots using `slot_usage`
   - the subClassOf slot is generic, but when used for PizzaTopping, the range must be PizzaTopping
   - we place OWL interpretations in slot usages
   - the advantages of this will ne shown later

Note that the use of these features are optional. You can choose to
repeat information if you prefer, or you can adopt some
features. Sometimes it is possible to over-abstract or
over-generalize, your own mileage may vary.


## Data and output

The data remains the same, as does the generated OWL output
