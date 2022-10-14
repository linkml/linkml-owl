# Part 3: Individuals

Ontologies are typically comprised of *classes* but sometimes we
want to include *instances* (*Individuals*) -- for example, when 
relating a pizza class to a country of origin

## Schema

```yaml
id: http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl
name: Pizza-Ontology-Metamodel
prefixes:
  pizza: http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl#
  linkml: https://w3id.org/linkml/
  dcterms: http://purl.org/dc/terms/
default_curi_maps:
    - semweb_context
default_prefix: pizza
imports:
  - linkml:types

classes:
  ## ---
  ## The Country class is new in part 2
  ## ---
  Country:
    annotations:
      owl: NamedIndividual
    attributes:
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationAssertion
        slot_uri: rdfs:label
      conforms_to:
        annotations:
          owl.fstring: AnnotationAssertion( dcterms:conformsTo {id} pizza:{V} )
        slot_uri: dcterms:conformsTo
        designates_type: true
      typeOf:
        name: typeOf
        annotations:
          owl:
            tag: owl
            value: ClassAssertion
        from_schema: http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl
        slot_uri: rdf:type
  NamedPizza:
    annotations:
      owl: Class
    attributes:
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationAssertion
        slot_uri: rdfs:label
      conforms_to:
        annotations:
          owl.fstring: AnnotationAssertion( dcterms:conformsTo {id} pizza:{V} )
        slot_uri: dcterms:conformsTo
        designates_type: true
      subClassOf:
        annotations:
          owl: SubClassOf
        slot_uri: rdfs:subClassOf
      hasToppings:
        annotations:
          owl: ObjectSomeValuesFrom
        singular_name: hasTopping
        multivalued: true
        range: PizzaTopping
      ## ---
      ## This attribute is new in part 3:
      ## ---
      hasCountryOfOrigin:
        annotations:
          owl: ObjectHasValue
        range: Country
  PizzaTopping:
    attributes:
      id:
        identifier: true
        range: uriorcurie
      label:
        annotations:
          owl: AnnotationAssertion
        slot_uri: rdfs:label
      conforms_to:
        annotations:
          owl.fstring: AnnotationAssertion( dcterms:conformsTo {id} pizza:{V} )
        slot_uri: dcterms:conformsTo
        designates_type: true
      subClassOf:
        annotations:
          owl: SubClassOf
        slot_uri: rdfs:subClassOf
      hasToppings:
        singular_name: hasTopping
        range: PizzaTopping
        multivalued: true
        annotations:
          owl: ObjectSomeValuesFrom

```

## Input Records

```yaml
# named pizzas
- id: pizza:NamedPizza
  conforms_to: NamedPizza
  label: named pizza

- id: pizza:AmericanPizza
  conforms_to: NamedPizza
  label: american
  subClassOf: pizza:NamedPizza
  hasToppings:
    - pizza:MozzarellaTopping
    - pizza:PepperoniSausageTopping
    - pizza:TomatoTopping
  hasCountryOfOrigin: pizza:America
- id: pizza:Mushroom
  conforms_to: NamedPizza
  label: mushroom
  subClassOf: pizza:NamedPizza
  hasToppings:
    - pizza:MozzarellaTopping
    - pizza:MushroomTopping
    - pizza:TomatoTopping
- id: pizza:Margherita
  conforms_to: NamedPizza
  label: Margherita
  subClassOf: pizza:NamedPizza
  hasToppings:
    - pizza:MozzarellaTopping
    - pizza:TomatoTopping

# toppings
- id: pizza:FishTopping
  label: fish topping
  conforms_to: PizzaTopping
  subClassOf: pizza:PizzaTopping
- id: pizza:MeatTopping
  label: meat topping
  conforms_to: PizzaTopping
  subClassOf: pizza:PizzaTopping
- id: pizza:VegetableTopping
  label: vegetable topping
  conforms_to: PizzaTopping
  subClassOf: pizza:PizzaTopping
- id: pizza:CheeseTopping
  label: cheese topping
  conforms_to: PizzaTopping
  subClassOf: pizza:PizzaTopping

- id: pizza:PepperoniSausageTopping
  label: pepperoni sausage topping
  conforms_to: PizzaTopping
  subClassOf: pizza:MeatTopping

- id: pizza:AnchoviesTopping
  label: anchovies topping
  conforms_to: PizzaTopping
  subClassOf: pizza:FishTopping

- id: pizza:ArtichokeTopping
  label: artichoke topping
  conforms_to: PizzaTopping
  subClassOf: pizza:VegetableTopping

- id: pizza:MushroomTopping
  label: mushroom topping
  conforms_to: PizzaTopping
  subClassOf: pizza:VegetableTopping

- id: pizza:TomatoTopping
  label: tomato topping
  conforms_to: PizzaTopping
  subClassOf: pizza:VegetableTopping

- id: pizza:MozzarellaTopping
  label: mozzarella topping
  conforms_to: PizzaTopping
  subClassOf: pizza:CheeseTopping
```


## OWL Output

```owl
Prefix( xml: = <http://www.w3.org/XML/1998/namespace> )
Prefix( rdf: = <http://www.w3.org/1999/02/22-rdf-syntax-ns#> )
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( xsd: = <http://www.w3.org/2001/XMLSchema#> )
Prefix( owl: = <http://www.w3.org/2002/07/owl#> )
Prefix( pizza: = <http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl#> )
Prefix( linkml: = <https://w3id.org/linkml/> )
Prefix( dcterms: = <http://purl.org/dc/terms/> )

Ontology( <http://www.co-ode.org/ontologies/pizza/2005/10/18/pizza.owl>
    AnnotationAssertion( rdfs:label pizza:NamedPizza "named pizza" )
    AnnotationAssertion( dcterms:conformsTo pizza:NamedPizza pizza:NamedPizza )
    AnnotationAssertion( rdfs:label pizza:AmericanPizza "american" )
    AnnotationAssertion( dcterms:conformsTo pizza:AmericanPizza pizza:NamedPizza )
    SubClassOf( pizza:AmericanPizza pizza:NamedPizza )
    SubClassOf( pizza:AmericanPizza     ObjectSomeValuesFrom( pizza:hasToppings pizza:MozzarellaTopping ) )
    SubClassOf( pizza:AmericanPizza     ObjectSomeValuesFrom( pizza:hasToppings pizza:PepperoniSausageTopping ) )
    SubClassOf( pizza:AmericanPizza     ObjectSomeValuesFrom( pizza:hasToppings pizza:TomatoTopping ) )
    SubClassOf( pizza:AmericanPizza     ObjectHasValue( pizza:hasCountryOfOrigin pizza:America ) )
    AnnotationAssertion( rdfs:label pizza:Mushroom "mushroom" )
    AnnotationAssertion( dcterms:conformsTo pizza:Mushroom pizza:NamedPizza )
    SubClassOf( pizza:Mushroom pizza:NamedPizza )
    SubClassOf( pizza:Mushroom     ObjectSomeValuesFrom( pizza:hasToppings pizza:MozzarellaTopping ) )
    SubClassOf( pizza:Mushroom     ObjectSomeValuesFrom( pizza:hasToppings pizza:MushroomTopping ) )
    SubClassOf( pizza:Mushroom     ObjectSomeValuesFrom( pizza:hasToppings pizza:TomatoTopping ) )
    AnnotationAssertion( rdfs:label pizza:Margherita "Margherita" )
    AnnotationAssertion( dcterms:conformsTo pizza:Margherita pizza:NamedPizza )
    SubClassOf( pizza:Margherita pizza:NamedPizza )
    SubClassOf( pizza:Margherita     ObjectSomeValuesFrom( pizza:hasToppings pizza:MozzarellaTopping ) )
    SubClassOf( pizza:Margherita     ObjectSomeValuesFrom( pizza:hasToppings pizza:TomatoTopping ) )
    AnnotationAssertion( rdfs:label pizza:FishTopping "fish topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:FishTopping pizza:PizzaTopping )
    SubClassOf( pizza:FishTopping pizza:PizzaTopping )
    AnnotationAssertion( rdfs:label pizza:MeatTopping "meat topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:MeatTopping pizza:PizzaTopping )
    SubClassOf( pizza:MeatTopping pizza:PizzaTopping )
    AnnotationAssertion( rdfs:label pizza:VegetableTopping "vegetable topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:VegetableTopping pizza:PizzaTopping )
    SubClassOf( pizza:VegetableTopping pizza:PizzaTopping )
    AnnotationAssertion( rdfs:label pizza:CheeseTopping "cheese topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:CheeseTopping pizza:PizzaTopping )
    SubClassOf( pizza:CheeseTopping pizza:PizzaTopping )
    AnnotationAssertion( rdfs:label pizza:PepperoniSausageTopping "pepperoni sausage topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:PepperoniSausageTopping pizza:PizzaTopping )
    SubClassOf( pizza:PepperoniSausageTopping pizza:MeatTopping )
    AnnotationAssertion( rdfs:label pizza:AnchoviesTopping "anchovies topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:AnchoviesTopping pizza:PizzaTopping )
    SubClassOf( pizza:AnchoviesTopping pizza:FishTopping )
    AnnotationAssertion( rdfs:label pizza:ArtichokeTopping "artichoke topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:ArtichokeTopping pizza:PizzaTopping )
    SubClassOf( pizza:ArtichokeTopping pizza:VegetableTopping )
    AnnotationAssertion( rdfs:label pizza:MushroomTopping "mushroom topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:MushroomTopping pizza:PizzaTopping )
    SubClassOf( pizza:MushroomTopping pizza:VegetableTopping )
    AnnotationAssertion( rdfs:label pizza:TomatoTopping "tomato topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:TomatoTopping pizza:PizzaTopping )
    SubClassOf( pizza:TomatoTopping pizza:VegetableTopping )
    AnnotationAssertion( rdfs:label pizza:MozzarellaTopping "mozzarella topping" )
    AnnotationAssertion( dcterms:conformsTo pizza:MozzarellaTopping pizza:PizzaTopping )
    SubClassOf( pizza:MozzarellaTopping pizza:CheeseTopping )
)
```

In Protege:

![screenshot](pizza03.png)
