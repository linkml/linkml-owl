from collections import defaultdict
from typing import Optional, List, Set, Any, Union, Dict, Tuple
from dataclasses import dataclass, field
import logging

import click
from funowl.converters.functional_converter import to_python
from jinja2 import Template
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import meta
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.eval_utils import eval_expr
from linkml_runtime.index.object_index import ObjectIndex
from linkml_runtime.utils.inference_utils import infer_all_slot_values, infer_slot_value, Config

from rdflib import URIRef

from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition, Definition, \
    ClassDefinitionName
from linkml_runtime.utils.formatutils import underscore, camelcase
from linkml_runtime.linkml_model.types import Uri, Uriorcurie

from funowl import OntologyDocument, Ontology, IRI, ObjectSomeValuesFrom, \
    Literal, \
    ObjectUnionOf, SubClassOf, ClassAssertion, \
    Class, \
    AnnotationAssertion, ObjectPropertyAssertion, \
    Prefix, AnonymousIndividual, ObjectAllValuesFrom, EquivalentClasses, ObjectIntersectionOf, ClassExpression, Axiom, \
    ObjectProperty, Declaration, InverseObjectProperties, ObjectPropertyDomain, ObjectPropertyRange, \
    SubObjectPropertyOf, TransitiveObjectProperty, SymmetricObjectProperty, AsymmetricObjectProperty, \
    ReflexiveObjectProperty, IrreflexiveObjectProperty, Annotation, ObjectMinCardinality, ObjectHasValue, \
    NamedIndividual, DataSomeValuesFrom, DataHasValue, DataAllValuesFrom, AnnotationProperty, DataProperty, Datatype, \
    DisjointClasses

from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.yamlutils import YAMLRoot

from linkml_owl.util.loader_wrapper import load_structured_file

INTERPRETATION = str
AXIOM_TYPE_NAME = str
OPERAND = str  ## e.g IntersectionOf, UnionOf

LEVEL = int
OP_KEY = Tuple[LEVEL, OPERAND, AXIOM_TYPE_NAME]


@dataclass
class EntityAxiomIndex:
    """
    An index of axioms (plus annotations), indexed by entity, plus aggregate grouping criteria (intersection, union)

    Motivation: any entity (such as a class) might have an arbitrary number of equivalence, disjointness, etc axioms
    associated with it; e.g.

    >>> A = B or C
    >>> A = D and E
    >>> A SubClassOf F or G
    >>>       ...

    This index allows these axioms to be incrementally constructed

    The index is via a tripartite key (OP_KEY) with elements:

    - Operator (e.g. AND/IntersectionOf, OR/Union)
    - AxiomType (e.g. SubClassOf, EquivalentClasses)
    - Level (default 0), allows for example multiple equivalence axioms using intersection
    """
    operand_list_index: Dict[OP_KEY, List[ClassExpression]] = field(default_factory=lambda: defaultdict(list))
    annotation_list_index: Dict[OP_KEY, List[Annotation]] = field(default_factory=lambda: defaultdict(list))
    annotations: List[Annotation] = field(default_factory=lambda: [])
    object_index: ObjectIndex = None

    def add_operand(self, key: OP_KEY, op: ClassExpression, anns: List[Annotation] = None):
        """
        Adds to part of an index

        :param key: combo of operator/axiomType/level
        :param op: operand - an element of the list used to construct the operator construct
        :return:
        """
        if key not in self.operand_list_index:
            self.operand_list_index[key] = []
        self.operand_list_index[key].append(op)
        if anns:
            if key not in self.annotation_list_index:
                self.annotation_list_index[key] = []
            ann_ix = self.annotation_list_index[key]
            for ann in anns:
                if ann not in ann_ix:
                    ann_ix.append(ann)


    def add_operands(self, key: OP_KEY, ops: List[ClassExpression], anns: List[Annotation] = None):
        """
        Adds to part of an index

        :param key:
        :param ops:
        :param anns:
        :return:
        """
        for op in ops:
            self.add_operand(key, op, anns)

@dataclass
class OWLDumper(Dumper):
    """
    Translate LinkML instances to OWL

    This differs from rdf_dumper in that each edge in the linkml instance graph
    may have a more complex OWL interpretation; for example:

    - lists may be treat as unions, rather than conjunctions of triples
    - linkml instances may be OWL classes

        - edges from these instances may be treated as axiom types such as SubClassOf R some Y

    Note that currently the OWL interpretation is "smuggled" into a model by way of special-syntax
    comments. In future we will either have a formal mapping file or extend the mapping syntax

    For context, see:
    https://github.com/linkml/linkml/issues/267
    """
    ontology: Ontology = None
    """Background ontology to use."""

    schema: SchemaDefinition = None
    """A LinkML schema that defines templates for generating OWL axioms"""

    schemaview: SchemaView = None
    """View over the schema."""

    object_index: ObjectIndex = None
    """Index of LinkML objects."""

    autofill: bool = False
    """If True, infer missing values in data."""

    def to_ontology_document(self, element: Union[YAMLRoot, List[YAMLRoot]], schema: Union[SchemaDefinition, str],
                             iri: str = None) -> OntologyDocument:
        """
        Recursively convert a linkml instance tree to an OWL Ontology Document

        :param element: element to convert
        :param schema:
        :param iri:
        :return:
        """
        o = Ontology(schema.id)
        self.ontology = o
        if isinstance(schema, SchemaDefinition):
            self.schema = schema
            self.schemaview = SchemaView(schema)
        else:
            self.schemaview = SchemaView(schema)
            self.schema = self.schemaview.schema
            schema = self.schema
        doc = OntologyDocument(iri, o)
        if isinstance(element, list):
            for e1 in element:
                self.transform(e1, schema)
        else:
            self.transform(element, schema)
        for pfx in schema.prefixes.values():
            doc.prefixDeclarations.append(Prefix(pfx.prefix_prefix, pfx.prefix_reference))
        return doc

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition = None, schemaview: SchemaView = None, iri=None) -> str:
        """
        Dump a linkml instance tree to a function syntax OWL ontology string

        :param element:
        :param schema:
        :param schemaview:
        :param iri:
        :return:
        """
        if schemaview:
            schema = schemaview.schema
        doc = self.to_ontology_document(element, schema, iri=iri)
        return str(doc)

    def transform(self, element: YAMLRoot, schema: SchemaDefinition, is_element_an_object=True) -> Any:
        """
        Recursively transform a LinkML element

        Each field is introspected, and translated to an OWL axiom.
        The field value is recursively transformed

        :param element:
        :param schema:
        :param is_element_an_object:
        :param is_element_an_owl_class:
        :return: IRI or node of transformation of element
        """
        logging.debug(f"transform: {element}")
        if element is None:
            return None
        try:
            # translate Enum
            meaning = element.meaning
            return self._get_IRI_str(meaning)
        except AttributeError:
            pass
        if not self._instance_of_linkml_class(element):
            # TODO: better way of detecting atoms
            if is_element_an_object:
                # foreign key
                return URIRef(self._get_IRI_str(element))
            elif isinstance(element, Uriorcurie):
                return URIRef(self._get_IRI_str(element))
            elif isinstance(element, Uri):
                return URIRef(element)
            else:
                # literal
                return Literal(element)
        o = self.ontology
        python_type = type(element)
        linkml_class_name = python_type.class_name
        if self.autofill:
            if not self.object_index:
                raise ValueError("object_index must be set if infer_missing_values is True")
            proxy = self.object_index.bless(element)
            for k, v in vars(element).items():
                if v is None:
                    infer_slot_value(proxy, k, schemaview=self.schemaview, class_name=linkml_class_name,
                                     config=Config(use_string_serialization=True,
                                                   use_expressions=True,
                                                   ))
        c = schema.classes[linkml_class_name]
        for fstr in self._get_inferred_class_annotations(c, 'owl.fstring'):
            self.add_axioms_from_fstring(fstr, element)
        for tmpl_str in self._get_inferred_class_annotations(c, 'owl.template'):
            self.add_axioms_from_template(tmpl_str, element)
        cls_interps = self._get_class_interpretations(c)
        subj = None
        eai = EntityAxiomIndex()
        unprocessed_parents = []
        # set subj = IRI for element
        for k, v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            if slot is None:
                raise ValueError(f'Lookup slot in {c.name} failed for {k} // element={element}')
            if slot.identifier:
                subj = URIRef(self._get_IRI_str(v))
                logging.debug(f"set subj from {slot.name}={v} asURI: {subj}")
        if AnonymousIndividual.__name__ in cls_interps or (subj is None and "Individual" in cls_interps):
            subj = AnonymousIndividual()
            logging.debug(f"No identifier slot; Creating anon individual for element = {subj}")
        else:
            for obj_type in [ObjectProperty, DataProperty, AnnotationProperty, NamedIndividual, Class, Datatype]:
                if obj_type.__name__ in cls_interps:
                    decl = Declaration(obj_type(subj))
                    logging.debug(f"Inferred {decl} based on {obj_type.__name__} in {cls_interps}")
                    o.axioms.append(decl)
        logging.info(f"Subject={subj}")
        expression_termset = {"IntersectionOf", "UnionOf", "ComplementOf", "OneOf", "SomeValuesFrom", "AllValuesFrom"}
        is_returns_expression = len(expression_termset.intersection(cls_interps)) > 0
        # iterate through all slot-value assignments for element;
        # generate axioms or add axioms to EntityAxiomIndex for each
        for k, v in vars(element).items():
            slot: SlotDefinition
            # TODO: unify slot/schema_level_slot
            slot = self._lookup_slot(c, k)
            if slot is None:
                logging.error(f'No slot for {k}')
                continue
            if slot.identifier:
                # the role of the identifier slot is to determine the IRI for the element;
                # it generates no axioms of its own
                continue
            schema_level_slot = self._get_schema_level_slot(slot)
            # lookup OWL settings on each slot
            owl_templates = self._get_inferred_slot_annotations(slot, 'owl.template', linkml_class_name)
            owl_fstrings = self._get_inferred_slot_annotations(slot, 'owl.fstring', linkml_class_name)
            boolean_form_of = self._get_inferred_slot_annotations(slot, 'boolean_form_of', linkml_class_name)
            axiom_annotation_slots = self._get_inferred_slot_annotations(slot, 'owl.axiom_annotation.slots', linkml_class_name)
            axiom_annotations: List[Annotation] = []
            if axiom_annotation_slots:
                # Axiom annotation
                for ann_slot_name in axiom_annotation_slots:
                    ann_slot = self._lookup_slot(c, ann_slot_name)
                    ann_vals = getattr(element, ann_slot_name)
                    if ann_vals:
                        if not isinstance(ann_vals, list):
                            ann_vals = [ann_vals]
                        for ann_val in ann_vals:
                            ann_val = self.transform(ann_val, schema, is_element_an_object=ann_slot.range in self.schema.classes)
                            ann_slot_iri = self._get_IRI_str(ann_slot.slot_uri)
                            axiom_annotations.append(Annotation(ann_slot_iri, ann_val))
            # templates
            for tmpl in owl_templates:
                self.add_axioms_from_template(tmpl, element)
            if schema_level_slot.slot_uri is not None:
                slot_uri = self._get_IRI_str(schema_level_slot.slot_uri)
            else:
                slot_uri = self._get_IRI_str(self.schemaview.get_uri(slot.name))
            logging.debug(f'SlotVal {subj}.{k} = {v} (URI={schema_level_slot.slot_uri}) // slot = {slot.name}')
            slot_interps = self._get_slot_interpretations(slot, linkml_class_name)
            logging.debug(f'OWL interpretations for {k}={slot_interps}')
            is_object_ref = slot.range in self.schema.classes
            # normalize input_vals to a list, then recursively transform
            if isinstance(v, list):
                input_vals = v
            elif isinstance(v, dict):
                input_vals = v.values()
            else:
                input_vals = [v]
            tr_vals = [self.transform(x, schema, is_element_an_object=is_object_ref) for x in input_vals]
            logging.debug(f'TR Vals={tr_vals}')
            parents = []  ## expressions that are the referents of the axioms to be generated
            is_class_logical_axiom = False
            # TODO: make this more generic
            is_disjunction = 'UnionOf' in slot_interps
            is_conjunction = 'IntersectionOf' in slot_interps
            is_annotation = 'AnnotationProperty' in slot_interps or 'Annotation' in slot_interps
            closure_axiom_parents = []
            for tr_val in tr_vals:
                logging.debug(f'  TR_VAL = {tr_val}')
                if tr_val is None:
                    continue
                if owl_fstrings:
                    for owl_fstring in owl_fstrings:
                        self.add_axioms_from_fstring(owl_fstring, element, tr_val)
                    continue
                if is_object_ref:
                    if isinstance(tr_val, str):
                        tr_val = self._get_IRI_str(tr_val)
                parent = tr_val
                if boolean_form_of:
                    # owl.boolean_form_of allows mapping between boolean slots and an owl object type
                    if parent and parent == Literal(True):
                        for owl_uri in boolean_form_of:
                            if owl_uri == 'owl:TransitiveProperty':
                                o.axioms.append(TransitiveObjectProperty(subj))
                            elif owl_uri == 'owl:SymmetricProperty':
                                o.axioms.append(SymmetricObjectProperty(subj))
                            elif owl_uri == 'owl:AsymmetricProperty':
                                o.axioms.append(AsymmetricObjectProperty(subj))
                            elif owl_uri == 'owl:ReflexiveProperty':
                                o.axioms.append(ReflexiveObjectProperty(subj))
                            elif owl_uri == 'owl:IrreflexiveProperty':
                                o.axioms.append(IrreflexiveObjectProperty(subj))
                            else:
                                raise ValueError(f'Cannot interpret {owl_uri}')
                # transform parents if an expression type is specified
                # TODO: use a mapping rather than repetitive code
                simple_expression_types = [ObjectSomeValuesFrom, DataSomeValuesFrom, ObjectHasValue, DataHasValue, ObjectAllValuesFrom, DataAllValuesFrom]
                for expression_type in simple_expression_types:
                    if expression_type.__name__ in slot_interps:
                        parent = expression_type(slot_uri, tr_val)
                        is_class_logical_axiom = True
                for logical_axiom_type in [SubClassOf, EquivalentClasses, DisjointClasses]:
                    if logical_axiom_type.__name__ in slot_interps:
                        is_class_logical_axiom = True
                parents.append(parent)
                if 'Closed' in slot_interps:
                    closure_axiom_parents.append(ObjectAllValuesFrom(slot_uri, tr_val))
            if closure_axiom_parents:
                if len(closure_axiom_parents) == 1:
                    closure_axiom_parent_expr = closure_axiom_parents[0]
                else:
                    closure_axiom_parent_expr = ObjectUnionOf(*closure_axiom_parents)
                self.add_axiom(SubClassOf(subj, closure_axiom_parent_expr), o, [])
            #    eai.add_operands((0, SubClassOf.__name__, ObjectUnionOf.__name__), parents, axiom_annotations)
            axiom_type = None
            # TODO: make this more generic / less repetitive
            axiom_types = [SubClassOf, SubObjectPropertyOf, ClassAssertion, ObjectPropertyAssertion, EquivalentClasses, InverseObjectProperties,ObjectPropertyDomain, ObjectPropertyRange, AnnotationAssertion]
            for candidate_axiom_type in axiom_types:
                if candidate_axiom_type.__name__ in slot_interps:
                    axiom_type = candidate_axiom_type
            # fill in default axiom type
            if axiom_type is None:
                # default: SubClassOf R some V for logical; otherwise annotation
                if is_class_logical_axiom and not is_returns_expression:
                    if is_annotation:
                        raise ValueError(f'{slot.name} cannot be both logical and an annotation')
                    axiom_type = SubClassOf
                else:
                    if is_annotation:
                        axiom_type = AnnotationAssertion
                    else:
                        axiom_type = None
                        logging.info(f"Cannot determine axiom type for {slot.name}, unprocessed={parents}")
                        unprocessed_parents += parents
                        #continue
            logging.debug(f'AXIOM TYPE = {axiom_type}')
            if axiom_type:
                # special case handling of conjunctions and disjunctions;
                # these are added to the index, to be processed at the entity level
                if is_disjunction:
                    # translate the filler list to a single entry that is a disjunction
                    # TODO: allow for different groupings; for now default to 0
                    level = 0
                    eai.add_operands((level, axiom_type.__name__, ObjectUnionOf.__name__), parents, axiom_annotations)
                    #eai.annotations += axiom_annotations
                    parents = []
                if is_conjunction:
                    # translate the filler list to a single entry that is a conjunction
                    # TODO: allow for different groupings; for now default to 0
                    level = 0
                    eai.add_operands((level, axiom_type.__name__, ObjectIntersectionOf.__name__), parents, axiom_annotations)
                    #eai.annotations += axiom_annotations
                    parents = []
                for parent in parents:
                    # Note: when considering making this more generic,
                    # bear in mind that order or number of arguments may vary
                    if axiom_type == SubClassOf:
                        logging.debug(f'type(subj) = {type(subj)} // {subj}')
                        if isinstance(subj, AnonymousIndividual):
                            axiom = None
                        else:
                            axiom = SubClassOf(subj, parent)
                    elif axiom_type == SubObjectPropertyOf:
                        axiom = SubObjectPropertyOf(subj, parent)
                    elif axiom_type == EquivalentClasses:
                        axiom = EquivalentClasses(subj, parent)
                    elif axiom_type == ClassAssertion:
                        # Note: ClassAssertion axioms are "inverted"
                        axiom = ClassAssertion(parent, subj)
                    elif axiom_type == ObjectPropertyAssertion:
                        axiom = ObjectPropertyAssertion(slot_uri, subj, parent)
                    elif axiom_type == InverseObjectProperties:
                        axiom = InverseObjectProperties(subj, parent)
                    elif axiom_type == ObjectPropertyDomain:
                        axiom = ObjectPropertyDomain(subj, parent)
                    elif axiom_type == ObjectPropertyRange:
                        axiom = ObjectPropertyRange(subj, parent)
                    elif axiom_type == AnnotationAssertion:
                        axiom = AnnotationAssertion(slot_uri, subj, parent)
                    else:
                        raise Exception(f'Unknown: {axiom_type}')
                    if axiom is not None:
                        self.add_axiom(axiom, o, axiom_annotations)
                    else:
                        unprocessed_parents.append(parent)
        # all per-slot axioms have been processed; axioms that span
        # multiple slots are now processed
        if "IntersectionOf" in cls_interps:
            expr = ObjectIntersectionOf(*unprocessed_parents)
            logging.debug(f"Returning expression {expr} // {eai.operand_list_index.items()}")
            return expr
        for op_key, operands in eai.operand_list_index.items():
            _, interp, operator = op_key
            logging.debug(f'EntityAxiomIndex {subj}: {interp} => {operator} over {operands}')
            if len(operands) < 2:
                raise ValueError(f'Too few operands: {operands} for {operator} in {subj}')
            if operator == ObjectUnionOf.__name__:
                expr = ObjectUnionOf(*operands)
            elif operator == ObjectIntersectionOf.__name__:
                expr = ObjectIntersectionOf(*operands)
            else:
                raise ValueError(f'Cannot handle operator: {operator}')
            if interp == EquivalentClasses.__name__:
                axiom = EquivalentClasses(subj, expr)
            elif interp == SubClassOf.__name__:
                axiom = SubClassOf(subj, expr)
            elif interp == DisjointClasses.__name__:
                axiom = DisjointClasses(subj, expr)
            else:
                raise ValueError(f'Not handled: {interp}')
            logging.debug(f'Adding axiom: {axiom}')
            self.add_axiom(axiom, o, eai.annotation_list_index.get(op_key, []))
        logging.debug(f"Returning {subj}")
        return subj

    def add_axiom(self, axiom: Axiom, ontology: Ontology, axiom_annotations: List[Annotation]) -> None:
        """
        Add an axiom to the ontology, appending any annotations to the axiom.

        :param axiom:
        :param ontology:
        :param axiom_annotations:
        :return:
        """
        axiom.annotations = axiom_annotations
        ontology.axioms.append(axiom)

    def _instance_of_linkml_class(self, v) -> bool:
        try:
            if type(v).class_name:
                return True
        except Exception:
            return False

    def _lookup_slot(self, cls: ClassDefinition, field: str) -> SlotDefinition:
        matching_slot = None
        for s in self.schemaview.class_induced_slots(cls.name):
            if underscore(s.name) == field:
                matching_slot = s
                break
            if s.alias and underscore(s.alias) == field:
                matching_slot = s
                break
        if matching_slot:
            if not matching_slot.slot_uri:
                uri = self.schemaview.get_uri(matching_slot)
                matching_slot.slot_uri = uri
            return matching_slot
        else:
            logging.error(f'Did not find {field} in {cls.name} slots =  {cls.slots}')

    def _get_inferred_slot_annotations(self, slot: SlotDefinition, ann_key: str,
                                       class_name: ClassDefinitionName) -> List[str]:
        vals = set()
        anc_slots = [slot]
        sv = self.schemaview
        for anc_c in sv.class_ancestors(class_name, reflexive=True):
            induced_slot = sv.induced_slot(slot.name, anc_c)
            anc_slots.append(induced_slot)
        for a in sv.slot_ancestors(slot.name, reflexive=True):
            anc_slots.append(sv.get_slot(a))
        for s in anc_slots:
            if ann_key == 'owl':
                # inject inferred annotations
                slot_uri = s.slot_uri
                if slot_uri == 'owl:inverseOf':
                    vals.add(InverseObjectProperties.__name__)
                if slot_uri == 'rdfs:domain':
                    vals.add(ObjectPropertyDomain.__name__)
                if slot_uri == 'rdfs:range':
                    vals.add(ObjectPropertyRange.__name__)
            if ann_key in s.annotations:
                if ann_key == 'owl':
                    vals.update([v.strip() for v in s.annotations[ann_key].value.split(',')])
                else:
                    vals.add(s.annotations[ann_key].value)
        return list(vals)

    def _get_inferred_class_annotations(self, cls: ClassDefinition, ann_key: str) -> List[str]:
        vals = set()
        anc_classes = [cls]
        sv = self.schemaview
        for anc_c in sv.class_ancestors(cls.name, reflexive=True):
            anc_classes.append(sv.get_class(anc_c))
        for s in anc_classes:
            if ann_key in s.annotations:
                if ann_key == 'owl':
                    vals.update([v.strip() for v in s.annotations[ann_key].value.split(',')])
                else:
                    vals.add(s.annotations[ann_key].value)
        return list(vals)

    def _get_class_interpretations(self, cls: ClassDefinition) -> Set[INTERPRETATION]:
        return set(self._get_inferred_class_annotations(cls, 'owl'))

    def _get_slot_interpretations(self, slot: SlotDefinition, class_name: ClassDefinitionName) -> Set[INTERPRETATION]:
        return set(self._get_inferred_slot_annotations(slot, 'owl', class_name))

    def _get_interpretations(self, x: Definition) -> Set[INTERPRETATION]:

        if isinstance(x, SlotDefinition):
            anc_names = self.schemaview.slot_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_slot(a) for a in anc_names] + [x]
        elif isinstance(x, ClassDefinition):
            anc_names = self.schemaview.class_ancestors(x.name, reflexive=False)
            ancs = [self.schemaview.get_class(a) for a in anc_names] + [x]
        else:
            raise ValueError(f'Not supported: {type(x)}')
        interps = set()
        #OWL_MARKER = 'OWL>>'
        for x in ancs:
            #for c in x.comments:
            #    logging.warning('Use of OWL>> is deprecated - replace with an annotation')
            #    # TODO: deprecated comment-based way of doing this
            #    if c.startswith(OWL_MARKER) and False:
            #        n = c.replace(OWL_MARKER, '').strip()
            #        interps.add(n)
            if 'owl' in x.annotations:
                interps.update([s.strip() for s in x.annotations['owl'].value.split(',')])
            # TODO: make this more declarative/generic; use a mapping of URIs => OWL types
            if isinstance(x, SlotDefinition):
                slot_uri = x.slot_uri
                if slot_uri == 'owl:inverseOf':
                    interps.add(InverseObjectProperties.__name__)
                if slot_uri == 'rdfs:domain':
                    interps.add(ObjectPropertyDomain.__name__)
                if slot_uri == 'rdfs:range':
                    interps.add(ObjectPropertyRange.__name__)
        return interps

    def _get_IRI_str(self, id: str) -> str:
        if id is None:
            raise ValueError(f'Must pass an id')
        if not isinstance(id, str):
            # TODO: more principled casting
            id = str(id)
        if ':' not in id:
            # TODO: https://github.com/linkml/linkml/issues/576
            #id = f'{self.ontology.iri}#{id}'
            id = f'{self.schema.default_prefix}:{id}'
        uri = self.schemaview.expand_curie(id)
        if uri:
            return uri

    # TODO: deprecate this
    def _get_schema_level_slot(self, slot: SlotDefinition) -> SlotDefinition:
        """
        See
        https://github.com/linkml/linkml/issues/270
        for context
        """
        alias = slot.alias
        if alias in self.schema.slots:
            schema_level_slot = self.schema.slots[alias]
        else:
            schema_level_slot = slot
        if schema_level_slot.name != slot.name:
            logging.warning(f'Using actual slot uri: {schema_level_slot.name} >> {slot.name}')
        return schema_level_slot

    def parse_axioms_string(self, owl_str: str, schemaview: SchemaView = None) -> OntologyDocument:
        if schemaview is None:
            schemaview = self.schemaview
        prefix_lines = []
        for prefix, url in schemaview.namespaces().items():
            prefix_lines.append(f'Prefix( {prefix}: = <{url}> )')
        header = "\n".join(prefix_lines)
        owl_str = f'{header}\nOntology(\n{owl_str}\n)'
        logging.debug(owl_str)
        try:
            doc = to_python(owl_str)
        except Exception as e:
            logging.error(f'Error parsing generated OWL: {owl_str}')
            raise e
        from funowl.writers.FunctionalWriter import FunctionalWriter
        from rdflib import Graph
        g = Graph()
        for p in doc.prefixDeclarations:
            g.namespace_manager.bind(p.prefixName, p.fullIRI)
        fw = FunctionalWriter(g=g)
        owl_str_roundtrip = doc.to_functional(fw)
        #logging.debug(f'ROUNDTRIP = {owl_str_roundtrip}')
        return doc

    def _element_to_template_dict(self, element: YAMLRoot, val: Any = None):
        d = {'this': element, 'V': val}
        for k, v in vars(element).items():
            d[k] = v
        return d

    def add_axioms_from_fstring(self, fstring: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None):
        if isinstance(fstring, meta.Annotation):
            fstring = fstring.value
        d = self._element_to_template_dict(element, val)
        owl_str = fstring.format(**d)
        logging.debug(f'FSTRING = {owl_str}')
        axioms = self.parse_axioms_string(owl_str).ontology.axioms
        logging.debug(f'AXIOMS >> = {axioms}')
        self.ontology.axioms += axioms

    def add_axioms_from_template(self, template_ann: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None):
        # TODO: simplify, change arg to str
        d = self._element_to_template_dict(element, val)
        if isinstance(template_ann, str):
            tstr = template_ann
        else:
            tstr = template_ann.value
        jt = Template(tstr)
        owl_str = jt.render(**d)
        axioms = self.parse_axioms_string(owl_str).ontology.axioms
        self.ontology.axioms += axioms

    def populate_missing_values(self, element: YAMLRoot):
        """
        Perform inference on data and populate missing data.

        Uses string_serialization.

        :param element:
        :return:
        """
        python_type = type(element)
        linkml_class_name = python_type.class_name
        c = self.schema.classes[linkml_class_name]
        for k, v in vars(element).items():
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            if v is None:
                if slot.string_serialization:
                    ctxt_obj = self.object_index.bless(element)
                    ctxt_dict = {k: getattr(ctxt_obj, k) for k in ctxt_obj._attributes()}
                    v = eval_expr(sd.expr, **ctxt_dict)
                    setattr(element, k, v)


@click.command()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.option('-s', '--schema', required=True,
              help="Path to LinkML schema")
@click.option("--target-class", "-C",
              help="name of class in datamodel that the root node instantiates")
@click.option("--module", "-m",
              help="Path to python datamodel module")
@click.option("--format", "-f",
              help="Input format (will be inferred from file suffix if not specified)")
@click.option('-o', '--output', required=True,
              help="Path to OWL functional syntax output")
@click.option("--autofill/--no-autofill",
              default=False,
              show_default=True,
              help="If True, fill missing data slots using string_serialization")
@click.argument('inputfile')
def cli(inputfile: str, schema: str, target_class, module, output, format, autofill: bool, verbose: int, quiet: bool, **args):
    """
    Dump LinkML instance data as OWL

    Examples:

    Convert a CSV to OWL

        linkml-data2owl -s tests/inputs/owl_dumper_test.yaml tests/inputs/parts.csv -o parts.ofn

        Note in this example, there must be a class type designator column `@type` in the CSV

    Convert a CSV to OWL, homogeneous classes:

        linkml-data2owl -C EquivGenusAndPartOf -s tests/inputs/owl_dumper_test.yaml \
            tests/inputs/parts_implicit_type.csv -o parts.ofn

    Convert YAML or JSON to OWL:

        linkml-data2owl -s tests/inputs/owl_dumper_test.yaml tests/inputs/owl_dumper_test_data.yaml -o ont.ofn

    """
    logger = logging.getLogger()
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)
    if module is None:
        if schema is None:
            raise Exception('must pass one of module OR schema')
        else:
            python_module = PythonGenerator(schema).compile_module()
    else:
        python_module = compile_python(module)
    sv = SchemaView(schema)
    element = load_structured_file(inputfile, target_class=target_class, python_module=python_module, schemaview=sv, fmt=format)

    dumper = OWLDumper()
    if autofill:
        dumper.autofill = True
    doc = dumper.dumps(element, schemaview=sv)
    with open(output, 'w') as stream:
        stream.write(str(doc))


if __name__ == '__main__':
    cli()