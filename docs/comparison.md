# Comparison with other frameworks

LinkML-OWL is one of several approaches for generating OWL ontologies from
structured data. This page compares it to hand-written OWL, ROBOT templates,
DOSDP (Dead Simple OWL Design Patterns), and OTTR (Reasonable Ontology Templates).

## At a glance

| Feature | Hand-written OWL | ROBOT templates | DOSDP | OTTR | **LinkML-OWL** |
|---|---|---|---|---|---|
| Input format | OWL syntax | TSV | TSV/YAML | RDF/stOTTR | YAML, JSON, TSV, RDF |
| Nested/hierarchical data | No | No | No | Yes | **Yes** |
| Schema validation | OWL profile checks | None | Minimal | Type checking | **Full (JSON-Schema, SHACL, ShEx)** |
| Cardinality constraints | N/A | None | None | Limited | **Required, multivalued, ranges** |
| Documentation generation | N/A | None | None | None | **Markdown, JSON-Schema docs** |
| Enum/value set support | N/A | Manual | Limited | N/A | **Semantic enums with `meaning`** |
| Template language | N/A | String substitution | YAML-based | stOTTR | **Jinja2 + annotations** |
| Ecosystem | Protege | ROBOT CLI | DOSDP-tools | Lutra | **LinkML toolchain** |

## Side-by-side: defining an anatomy class

### Goal

Define "lens of camera-type eye" as equivalent to "lens AND part-of some camera-type eye."

### Hand-written OWL (Functional Syntax)

```owl
Prefix( rdfs: = <http://www.w3.org/2000/01/rdf-schema#> )
Prefix( UBERON: = <http://purl.obolibrary.org/obo/UBERON_> )
Prefix( BFO: = <http://purl.obolibrary.org/obo/BFO_> )
Prefix( IAO: = <http://purl.obolibrary.org/obo/IAO_> )

Ontology(
  Declaration( Class( UBERON:0004801 ) )
  Declaration( Class( UBERON:0000389 ) )
  Declaration( Class( UBERON:0000019 ) )
  Declaration( ObjectProperty( BFO:0000050 ) )

  AnnotationAssertion( rdfs:label UBERON:0004801
    "lens of camera-type eye" )
  AnnotationAssertion( IAO:0000115 UBERON:0004801
    "The transparent structure in the eye that focuses light." )

  EquivalentClasses(
    UBERON:0004801
    ObjectIntersectionOf(
      UBERON:0000389
      ObjectSomeValuesFrom( BFO:0000050 UBERON:0000019 )
    )
  )
)
```

**Downsides:** Verbose. Every entity needs explicit declarations. Prefix management
is manual. Easy to make syntax errors. No validation of data integrity. Adding 100
classes means 100 copies of this pattern.

### ROBOT template

**Template (TSV):**

| ID | LABEL | DEFINITION | EquivalentTo |
|---|---|---|---|
| ID | LABEL | A IAO:0000115 | EC % |
| UBERON:0004801 | lens of camera-type eye | The transparent structure... | UBERON:0000389 and (BFO:0000050 some UBERON:0000019) |

```bash
robot template --template lens.tsv --output lens.owl
```

**Downsides:** The Manchester Syntax expression in the `EquivalentTo` column is
a raw string — no validation until ROBOT parses it. No schema for the TSV
(columns are ad-hoc). Nested data (e.g. parts-with-counts) cannot be represented
in a flat TSV. No reuse of column definitions across templates.

### DOSDP

**Pattern (YAML):**

```yaml
pattern_name: anatomical_structure_part_of
classes:
  anatomical_structure: UBERON:0000061
  whole: UBERON:0000061
relations:
  part_of: BFO:0000050

vars:
  anatomical_structure: "'anatomical_structure'"
  whole: "'anatomical_structure'"

name:
  text: "%s of %s"
  vars:
    - anatomical_structure
    - whole

def:
  text: "A %s that is part of a %s."
  vars:
    - anatomical_structure
    - whole

equivalentTo:
  text: "'anatomical_structure' and 'part_of' some 'whole'"
  vars:
    - anatomical_structure
    - whole
```

**Data (TSV):**

| defined_class | anatomical_structure | whole |
|---|---|---|
| UBERON:0004801 | UBERON:0000389 | UBERON:0000019 |

**Downsides:** Patterns are expressed using a custom YAML DSL. The OWL
expression is still a string template. No schema validation of the input TSV.
Cannot handle nested data or variable-length lists of differentiae.

### LinkML-OWL

**Schema (YAML):**

```yaml
classes:
  DefinedAnatomicalStructure:
    slots:
      - id
      - label
      - definition
      - genus
      - differentia_part_of
    slot_usage:
      genus:
        slot_uri: rdfs:subClassOf
        range: AnatomicalStructure
        required: true
        annotations:
          owl: EquivalentClasses, IntersectionOf
      differentia_part_of:
        slot_uri: BFO:0000050
        range: AnatomicalStructure
        annotations:
          owl: EquivalentClasses, IntersectionOf, ObjectSomeValuesFrom
```

**Data (YAML):**

```yaml
- id: UBERON:0004801
  label: lens of camera-type eye
  definition: The transparent structure in the eye that focuses light.
  genus: UBERON:0000389
  differentia_part_of: UBERON:0000019
```

```bash
linkml-data2owl -s anatomy-schema.yaml -C DefinedAnatomicalStructure data.yaml -o lens.ofn
```

**Advantages:**

- The schema *is* the documentation: slot names, ranges, cardinality, and descriptions are all formal
- Input data is validated against the schema before OWL generation
- The same schema generates JSON-Schema, SHACL shapes, SQL DDL, and Markdown docs
- Nested/hierarchical data is fully supported
- Semantic enums map directly to ontology terms
- OWL mapping is declarative (annotation keywords), not string-based

## Where other tools may be better

LinkML-OWL is not always the right choice:

- **Simple, flat term lists**: If you have a simple TSV of terms with labels and
  parent classes, ROBOT templates are simpler with less setup overhead.
- **Existing DOSDP infrastructure**: Projects already using DOSDP-tools with
  established patterns may not benefit from migrating.
- **Pure OWL editing**: For interactive, visual ontology editing, Protege
  remains the standard tool.
- **RDF-native workflows**: If your source data is already RDF, tools like
  SPARQL CONSTRUCT or OTTR may integrate more naturally.

## When to choose LinkML-OWL

LinkML-OWL is most valuable when:

1. **Your source data is complex** — nested structures, variable-length lists,
   cross-references between entities
2. **You need data validation** — catch errors before they become bad axioms
3. **You generate multiple outputs** — the same schema can produce OWL, JSON-Schema,
   SQL, documentation, and SHACL shapes
4. **You have design patterns that repeat** — define the pattern once in the schema,
   instantiate it many times in data
5. **You want to auto-generate labels and definitions** — use `string_serialization`
   to populate annotation slots from other slot values
6. **Your axioms are complex** — Jinja templates handle arbitrary OWL Functional Syntax,
   including GCIs, axiom annotations, and nested class expressions
