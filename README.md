# linkml-owl

## Formalism

A LinkML **model** `M` consists of:

 * slots `MS = {s1, ...}`
 * classes `MC = {c1,...}`
 * enums `MEn = {En1, ...}`
 * types `MT = {t1, ...}`
 * subsets `MSu = {su1, ..}`

Each slot `s ∈ MS` and each class `c ∈ MC` has an *interpretation* Δ:

* `Δ(s) ∈ P( {SubClassOf, ClassAssertion, SomeValuesFrom, AllValuesFrom, AnnotationAssertion, ObjectPropertyAssertion, AnnotationPropertyAssertion, UnionOf, DataOneOf, ObjectOneOf } ) `
* `Δ(c) ∈ P( {Class, Individual, ObjectProperty, DataProperty, AnnotationAssertion} )`

(here `P` denotes the powerset, i.e. Δ maps to class or slot to a set of valid terms)

The interpretation dictates how elements that instantiate the model are translated to OWL-DL

Informative note:

* any class `c ∈ MC` where `Class ∈ Δ(c)` is considered a *metaclass*
* any class `c ∈ MC` where `*Property ∈ Δ(c)` is considered a *metaproperty*
* in the linkml metamodel, the class `ClassDefinition` is a metaclass

A LinkML **element** `e ∈ E` is either:

 1. An instance of a class in `MC`
 2. A *reference* to an instance of a class in `MC`
 3. A *literal* taken from the universe of literals `L`
 4. A *permissible value* from the set of permissible values of a member of `MEn`

Note that the distinction between 1 and 2 only holds for tree representations such as YAML and JSON serializations.

Each `e` has a set of slot-value assignments `A(e)`,
where each assignment is a pair `s, V`

 * `s` is a slot in `MS`
 * `V` is a list of elements `v1, ..., vn` each of which can be:
    * if `s.range ∈ MT`: `v_i` must be a `Literal`
    * if `s.range ∈ MC`: `v_i` must be either:
        * another element in `I` OR
        * a reference to an element in `I`
        * (this distinction only holds for yaml/json tree representations)
    * if `s.range ∈ MEn`: `v_i` must be a member of the permissible value in `ME`
    
* `A(i) ⊆ { (s,V) ∈  MS x I ∪ Ref(I) ∪ ME ∪ L }`

Any slot marked as `identifier` is not considered among the list of slots.

* The identifier slot for a class `c` is marked `c.id`
* The identifier value for an element `e` is marked `e.id`

Only elements that instantiate classes in `MC` can have identifiers.
Not all instantiating elements have identifiers - instantiating elements without *anonymous*

Any linkml element can be translated using the rules below. The translation is recursive, i.e. mapping an element that
has slot-value associations will invoke mappings on the values of these associations.

If the linkml element graph is a tree, then invoking mapping on the root will map the whole graph

## Mapping elements

The function `Tr(e)` will translate an element `e` to an OWL *entity*, and as
a side-effect will generate OWL *axioms*

### Table 1: Translation of elements to OWL entities

|condition|returns|
|---|---|
|`e.type ∈ MC` and `hasId(e)`| `IRI(e.id)` |
|`e.type ∈ MC` and `noId(e)`| `BlankNode()` |
|`e.type ∈ Ref(MC)` | `IRI(e)` |
|`e.type ∈ MEn` | `IRI(e.meaning)` |
|`e.type ∈ T`| `Literal(e)` |

### Generation of OWL axioms

Invoking `Tr(e)` will additionally generate further OWL axioms:

* for all `(s,V) in A(e)`, a mapping `Tr(e,s,V)` is applied

See *mapping slot values* below.

### Generation of OWL declarations

TODO

|Function|`Δ(e.type)`|generates|cond|
|---|---|---|---|
|`C(i)`|*|`Class(IRI(i.id))` |`i.id` exists|
|`OP(i)`|*|`ObjectProperty(IRI(i.id))`|`i.id` exists|
|`DP(i)`|*|`DataProperty(IRI(i.id))`|`i.id` exists|
|`AP(i)`|*|`AnnotationProperty(IRI(i.id))`|`i.id` exists|
|`*|*|`BlankNode(i)` |`i.id` not exists|


## Mapping slot values: Tr(i,s,V)

interpretation of an element `i` with slot `s` with values `V=v1..vn`

### Table 2: single-valued or conjunctive lists

If `s` is not `multivalued` OR `{UnionOf, DataOneOf, ObjectOneOf} ∩ Δ(s) = {}`
**then** the following table generates an axiom for all `v ∈ V`

|`Δ(e.type)`|`Δ(s)`|expression|cond|
|---|---|---|---|
|*|`SubClassOf` ∈ Δ|`C(e) ⊑ C(v)` |
|*|`SubObjectPropertyOf` ∈ Δ|`OP(e) ⊑ OP(v)` |
|*|`ClassAssertion` ∈ Δ|`I(e) : C(v)` |
|`Class`|`SomeValuesFrom` ∈ Δ|`C(e) ⊑ ∃ OP(s) C(v)` |
|`Class`|`AllValuesFrom` ∈ Δ|`C(e) ⊑ ∀ OP(s) C(v)` |
|`Individual`|`SomeValuesFrom` ∈ Δ|`I(e) : ∃ OP(s) C(v)` |
|`Individual`|`AllValuesFrom` ∈ Δ|`I(e) : ∀ OP(s) C(v)` |
| `*` | `AnnotationAssertion ∈ Δ` OR `Δ = {}`|`Ann(P(s) IRI(e) Tr(v))` |
| `*` | `ObjectPropertyAssertion ∈ Δ`|`OPA(OP(s) IRI(e) Tr(v))` |
| `*` | `DataPropertyAssertion ∈ Δ`|`DPA(DP(s) IRI(e) Tr(v))` |

See [DL article](https://en.wikipedia.org/wiki/Description_logic) on Wikipedia for explanation of symbols

### multi-valued or disjunctive lists

If `s` is `multivalued` AND `{UnionOf, DataOneOf, ObjectOneOf} ∩ Δ(s) ≠ {}`
**then** apply the following steps, and *then* apply table 2 rules

|`Δ(s)`|`Tr(V)`|
|---|---|
|`UnionOf` ∈ Δ|`UnionOf(C(v1), ..., C(vn))` |
|`ObjectOneOf` ∈ Δ|`ObjectOneOf(I(v1), ..., I(vn))` |
|`DataOneOf` ∈ Δ|`DataOneOf(D(v1), ..., D(vn))` |

### pre-processing

For uncommitted slots that have a slot iri with a pre-existing interpretation, these are used: 

 * If `s.iri = rdf:type`, and `Δ(s) = {}` then set `Δ(s) = {ClassAssertion}`
 * If `s.iri = rdfs:subClassOf`, and `Δ(s) = {}` then set `Δ(s) = {SubClassOf}`
 * etc TODO

