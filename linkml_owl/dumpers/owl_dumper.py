import sys
from collections import defaultdict
from enum import Enum, auto
from typing import Optional, List, Set, Any, Union, Dict, Tuple
from dataclasses import dataclass, field
import logging
import re

import click
import pyhornedowl
from jinja2 import Template
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import meta
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.eval_utils import eval_expr
from linkml_runtime.index.object_index import ObjectIndex
from linkml_runtime.utils.inference_utils import infer_all_slot_values, infer_slot_value, Config

from linkml_runtime.linkml_model.meta import ClassDefinition, SchemaDefinition, SlotDefinition, Definition, \
    ClassDefinitionName
from linkml_runtime.utils.formatutils import underscore, camelcase
from linkml_runtime.linkml_model.types import Uri, Uriorcurie

from pyhornedowl import PyIndexedOntology
from pyhornedowl.model import IRI, ObjectSomeValuesFrom, \
    Literal, \
    ObjectUnionOf, SubClassOf, ClassAssertion, \
    Class, \
    AnnotationAssertion, ObjectPropertyAssertion, \
    AnonymousIndividual, ObjectAllValuesFrom, EquivalentClasses, ObjectIntersectionOf, ClassExpression, \
    ObjectProperty, InverseObjectProperties, ObjectPropertyDomain, ObjectPropertyRange, \
    SubObjectPropertyOf, TransitiveObjectProperty, SymmetricObjectProperty, AsymmetricObjectProperty, \
    ReflexiveObjectProperty, IrreflexiveObjectProperty, Annotation, ObjectMinCardinality, ObjectHasValue, \
    NamedIndividual, DataSomeValuesFrom, DataHasValue, DataAllValuesFrom, AnnotationProperty, DataProperty, Datatype, \
    DisjointClasses, DisjointUnion, DataPropertyAssertion, Component, SimpleLiteral, DatatypeLiteral, DeclareClass, \
    DeclareObjectProperty, DeclareDataProperty, DeclareAnnotationProperty, DeclareNamedIndividual, DeclareDatatype, \
    AnnotatedComponent

from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.yamlutils import YAMLRoot

from linkml_owl.util.loader_wrapper import load_structured_file
from linkml_owl.util.owl_util import get_declarations, as_class_expression, as_class_expression_list, Axiom, Ontology, \
    add_axiom, instantiate_restriction


class IRIRepairPolicy(Enum):
    """
    Policy for handling IRIs in OWL Functional Syntax output.

    In OFN syntax, full IRIs must be wrapped in angle brackets (<http://...>),
    while CURIEs (prefix:local) do not need brackets. When templates produce
    mixed output (some CURIEs, some expanded IRIs), this policy controls behavior.
    """
    REPAIR = auto()
    """Silently repair malformed IRIs by wrapping full IRIs in angle brackets."""

    WARN = auto()
    """Repair malformed IRIs but emit a warning for each repair."""

    STRICT = auto()
    """Raise an error if a malformed IRI is detected."""


# Regex to detect full IRIs that need wrapping (has scheme://, not already wrapped)
_FULL_IRI_PATTERN = re.compile(r'(?<![<"\'])(\b\w+://[^\s<>"\')]+)')


INTERPRETATION = str
AXIOM_TYPE_NAME = str
OPERAND = str  ## e.g IntersectionOf, UnionOf



LEVEL = int
OP_KEY = Tuple[LEVEL, OPERAND, AXIOM_TYPE_NAME]


def _skip_key_in_element(k: str, element: YAMLRoot) -> bool:
    return k.startswith("unknown_") and k.replace("unknown_", "") in vars(element)


@dataclass
class EntityAxiomIndex:
    """
    An index of axioms (plus annotations), indexed by entity, plus aggregate grouping criteria (intersection, union)

    Motivation: any entity (such as a class) might have an arbitrary number of equivalence, disjointness, etc axioms
    associated with it; e.g.

    .. code-block:: python

         A = B or C
         A = D and E
         A SubClassOf F or G
                ...

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

    iri_policy: IRIRepairPolicy = IRIRepairPolicy.REPAIR
    """Policy for handling full IRIs in OFN template output."""

    _blank_node_counter: int = 0
    """Counter for generating unique blank node IDs."""

    def _next_blank_node_id(self) -> str:
        """Generate a unique blank node ID."""
        self._blank_node_counter += 1
        return f"_:b{self._blank_node_counter}"

    def to_ontology_document(self, element: Union[YAMLRoot, List[YAMLRoot]], schema: Union[SchemaDefinition, str],
                             iri: str = None) -> PyIndexedOntology:
        """
        Recursively convert a linkml instance tree to an OWL Ontology Document.

        :param element: element to convert
        :param schema:
        :param iri:
        :return:
        """
        # TODO: Figure how to set ontology IRI
        # o = PyIndexedOntology(schema.id)
        o = PyIndexedOntology()
        self.ontology = o
        if isinstance(schema, SchemaDefinition):
            self.schema = schema
            self.schemaview = SchemaView(schema)
        else:
            self.schemaview = SchemaView(schema)
            self.schema = self.schemaview.schema
            schema = self.schema
        # TODO: remove vestiges of funowl
        doc =o
        if isinstance(element, list):
            for e1 in element:
                self.transform(e1, schema)
        else:
            self.transform(element, schema)
        for pfx in schema.prefixes.values():
            doc.add_prefix_mapping(pfx.prefix_prefix, pfx.prefix_reference)
        return doc

    def dumps(self, element: YAMLRoot, schema: SchemaDefinition = None, schemaview: SchemaView = None, iri=None, output_type=None) -> str:
        """
        Dump a linkml instance tree to a function syntax OWL ontology string

        :param element:
        :param schema:
        :param schemaview:
        :param iri:
        :param output_type: Output format - "ofn" (default), "owl" (RDF/XML), "owx" (OWL/XML)
        :return:
        """
        if schemaview:
            schema = schemaview.schema
        doc = self.to_ontology_document(element, schema, iri=iri)
        # Map output types to py-horned-owl serialization formats
        format_map = {"ttl": "owl", "ofn": "ofn", "owl": "owl", "owx": "owx", None: "ofn"}
        serialization = format_map.get(output_type, "ofn")
        result = doc.save_to_string(serialization)
        # For OFN output, fix invalid CURIEs that contain '#' in the local part
        if serialization == "ofn" and self.schema:
            prefix_map = {pfx.prefix_prefix: pfx.prefix_reference for pfx in self.schema.prefixes.values()}
            result = self._fix_invalid_curies(result, prefix_map)
        return result

    def transform(self, element: YAMLRoot, schema: SchemaDefinition, is_element_an_object=True) -> Any:
        """
        Recursively transform a LinkML element

        Each field is introspected, and translated to an OWL axiom or expression.
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
            # naive method to test if an object is an enum:
            # try accessing the `meaning` field. If this fails,
            # an exception is thrown, and we carry on.
            # (when owl_duper is refactored to not be dependent on
            #  python dataclasses this will no longer be necessary)
            meaning = element.meaning
            if is_element_an_object:
                # enum is used in an object context: translate to URI
                if not meaning:
                    enum_uri = schema.default_prefix + ":" + type(element).__name__
                    meaning = enum_uri + "#" + str(element).replace(" ", "+")
                return self._get_IRI_str(meaning)
            else:
                # enum is used in a data context - stringify
                return str(element)
        except AttributeError:
            # not an enum - carry on
            pass
        if not self._instance_of_linkml_class(element):
            ont = self.ontology
            # TODO: better way of detecting atoms
            if is_element_an_object:
                # foreign key
                return ont.iri(self._get_IRI_str(element))
            elif isinstance(element, Uriorcurie):
                return ont.iri(self._get_IRI_str(element))
            elif isinstance(element, Uri):
                return ont.iri(self._get_IRI_str(element))
            elif isinstance(element, str):
                return SimpleLiteral(element)
            elif isinstance(element, bool):
                # bool must come before int since bool is a subclass of int
                datatype = ont.iri("http://www.w3.org/2001/XMLSchema#boolean")
                return DatatypeLiteral(str(element).lower(), datatype)
            elif isinstance(element, int):
                datatype = ont.iri("http://www.w3.org/2001/XMLSchema#integer")
                return DatatypeLiteral(str(element), datatype)
            elif isinstance(element, float):
                datatype = ont.iri("http://www.w3.org/2001/XMLSchema#double")
                return DatatypeLiteral(str(element), datatype)
            else:
                # Fallback: convert to string literal
                return SimpleLiteral(str(element))
        o = self.ontology

        def _as_class_expression(x: Union[ClassExpression, IRI, str]) -> Union[ClassExpression, Class]:
            return as_class_expression(o, x)

        def _as_class_expression_list(*x: Union[ClassExpression, IRI, str]) -> List[Union[ClassExpression, Class]]:
            return as_class_expression_list(o, *x)

        python_type = type(element)
        # TODO: allow for pydantic
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
            self.add_axioms_from_template(tmpl_str, element, schema=schema)
        cls_interps = self._get_class_interpretations(c)
        subj = None
        eai = EntityAxiomIndex()
        unprocessed_parents = []
        # set subj = IRI for element
        for k, v in vars(element).items():
            if _skip_key_in_element(k, element):
                continue
            slot: SlotDefinition
            slot = self._lookup_slot(c, k)
            if slot is None:
                raise ValueError(f'Cannot find slot {c.name}.{k} // {vars(element)} element={element}')
            if slot.identifier:
                subj = o.iri(self._get_IRI_str(v))
                logging.debug(f"set subj from {slot.name}={v} asURI: {subj}")
        if AnonymousIndividual.__name__ in cls_interps or (subj is None and "Individual" in cls_interps):
            subj = AnonymousIndividual(self._next_blank_node_id())
            logging.debug(f"No identifier slot; Creating anon individual for element = {subj}")
        else:
            for declaration in get_declarations(o, subj, interpretations=cls_interps):
                o.add_axiom(declaration)
        logging.info(f"Subject={subj}")
        expression_termset = {"IntersectionOf", "UnionOf", "ComplementOf", "OneOf", "SomeValuesFrom", "AllValuesFrom"}
        is_returns_expression = len(expression_termset.intersection(cls_interps)) > 0
        # iterate through all slot-value assignments for element;
        # generate axioms or add axioms to EntityAxiomIndex for each
        for k, v in vars(element).items():
            if _skip_key_in_element(k, element):
                continue
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
            if 'owl.ignore' in slot.annotations:
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
                            ann_slot_iri = o.iri(self._get_IRI_str(ann_slot.slot_uri))
                            axiom_annotations.append(Annotation(AnnotationProperty(ann_slot_iri), ann_val))
            # templates
            for tmpl in owl_templates:
                self.add_axioms_from_template(tmpl, element, schema=schema)
            if schema_level_slot.slot_uri is not None:
                slot_uri = self._get_IRI_str(schema_level_slot.slot_uri)
            else:
                slot_uri = self._get_IRI_str(self.schemaview.get_uri(slot.name))
            logging.debug(f'SlotVal {subj}.{k} = {v} (URI={schema_level_slot.slot_uri}) // slot = {slot.name}')
            slot_interps = self._get_slot_interpretations(slot, linkml_class_name)
            logging.debug(f'OWL interpretations for {k}={slot_interps}')
            is_object_ref = slot.range in self.schema.classes
            if "ObjectPropertyAssertion" in slot_interps or "ObjectProperty" in slot_interps:
                is_object_ref = True
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
                    # Check if parent is a True boolean literal
                    is_true_literal = (
                        (isinstance(parent, SimpleLiteral) and parent.literal == "true") or
                        (isinstance(parent, DatatypeLiteral) and parent.literal == "true") or
                        parent is True
                    )
                    if parent and is_true_literal:
                        for owl_uri in boolean_form_of:
                            # TODO: genericize this
                            op = o.object_property(str(slot_uri))
                            if owl_uri == 'owl:TransitiveProperty':
                                o.add_axiom(TransitiveObjectProperty(op))
                            elif owl_uri == 'owl:SymmetricProperty':
                                o.add_axiom(SymmetricObjectProperty(op))
                            elif owl_uri == 'owl:AsymmetricProperty':
                                o.add_axiom(AsymmetricObjectProperty(op))
                            elif owl_uri == 'owl:ReflexiveProperty':
                                o.add_axiom(ReflexiveObjectProperty(op))
                            elif owl_uri == 'owl:IrreflexiveProperty':
                                o.add_axiom(IrreflexiveObjectProperty(op))
                            else:
                                raise ValueError(f'Cannot interpret {owl_uri}')
                # transform parents if an expression type is specified
                # TODO: use a mapping rather than repetitive code
                simple_expression_types = [ObjectSomeValuesFrom, DataSomeValuesFrom, ObjectHasValue, DataHasValue, ObjectAllValuesFrom, DataAllValuesFrom]
                for expression_type in simple_expression_types:
                    if expression_type.__name__ in slot_interps:
                        parent = instantiate_restriction(expression_type, slot_uri, tr_val, o)
                        #parent = expression_type(slot_uri, tr_val)
                        is_class_logical_axiom = True
                for logical_axiom_type in [SubClassOf, EquivalentClasses, DisjointClasses]:
                    if logical_axiom_type.__name__ in slot_interps:
                        is_class_logical_axiom = True
                parents.append(parent)
                if 'Closed' in slot_interps:
                    # Create proper ObjectProperty and ClassExpression for ObjectAllValuesFrom
                    prop = o.object_property(slot_uri)
                    filler = _as_class_expression(tr_val)
                    closure_axiom_parents.append(ObjectAllValuesFrom(prop, filler))
            if closure_axiom_parents:
                if len(closure_axiom_parents) == 1:
                    closure_axiom_parent_expr = closure_axiom_parents[0]
                else:
                    closure_axiom_parent_expr = ObjectUnionOf(_as_class_expression_list(*closure_axiom_parents))
                self.add_axiom(SubClassOf(_as_class_expression(subj), closure_axiom_parent_expr), o, [])
            #    eai.add_operands((0, SubClassOf.__name__, ObjectUnionOf.__name__), parents, axiom_annotations)
            axiom_type = None
            # TODO: make this more generic / less repetitive
            axiom_types = [SubClassOf, SubObjectPropertyOf, ClassAssertion, ObjectPropertyAssertion, DataPropertyAssertion, EquivalentClasses, InverseObjectProperties,ObjectPropertyDomain, ObjectPropertyRange, AnnotationAssertion]
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
                            axiom = SubClassOf(_as_class_expression(subj), _as_class_expression(parent))
                    elif axiom_type == SubObjectPropertyOf:
                        # Convert IRIs to ObjectProperty if needed
                        sub_prop = o.object_property(str(subj)) if isinstance(subj, IRI) else subj
                        super_prop = o.object_property(str(parent)) if isinstance(parent, IRI) else parent
                        axiom = SubObjectPropertyOf(sub_prop, super_prop)
                    elif axiom_type == EquivalentClasses:
                        axiom = EquivalentClasses(_as_class_expression_list(subj, parent))
                    elif axiom_type == ClassAssertion:
                        # Note: ClassAssertion axioms are "inverted"
                        # subj can be AnonymousIndividual or needs conversion to NamedIndividual
                        if isinstance(subj, AnonymousIndividual):
                            ind = subj
                        else:
                            ind = o.named_individual(str(subj))
                        # parent must be a ClassExpression
                        class_expr = _as_class_expression(parent)
                        axiom = ClassAssertion(class_expr, ind)
                    elif axiom_type == ObjectPropertyAssertion:
                        op = o.object_property(slot_uri)
                        # Subject can be AnonymousIndividual or needs conversion
                        if isinstance(subj, AnonymousIndividual):
                            subj_ind = subj
                        else:
                            subj_ind = o.named_individual(str(subj))
                        # Object can also be AnonymousIndividual
                        if isinstance(parent, AnonymousIndividual):
                            obj_ind = parent
                        else:
                            obj_ind = o.named_individual(str(parent))
                        axiom = ObjectPropertyAssertion(op, subj_ind, obj_ind)
                    elif axiom_type == DataPropertyAssertion:
                        dp = o.data_property(slot_uri)
                        # Subject can be AnonymousIndividual or needs conversion
                        if isinstance(subj, AnonymousIndividual):
                            ind = subj
                        else:
                            ind = o.named_individual(str(subj))
                        # Value must be a proper Literal
                        if isinstance(parent, str):
                            literal_val = SimpleLiteral(parent)
                        elif isinstance(parent, (SimpleLiteral, DatatypeLiteral)):
                            literal_val = parent
                        else:
                            # Fallback: convert to string literal
                            literal_val = SimpleLiteral(str(parent))
                        axiom = DataPropertyAssertion(dp, ind, literal_val)
                    elif axiom_type == InverseObjectProperties:
                        sub_prop = o.object_property(str(subj)) if isinstance(subj, IRI) else subj
                        inv_prop = o.object_property(str(parent)) if isinstance(parent, IRI) else parent
                        axiom = InverseObjectProperties(sub_prop, inv_prop)
                    elif axiom_type == ObjectPropertyDomain:
                        prop = o.object_property(str(subj)) if isinstance(subj, IRI) else subj
                        axiom = ObjectPropertyDomain(prop, _as_class_expression(parent))
                    elif axiom_type == ObjectPropertyRange:
                        prop = o.object_property(str(subj)) if isinstance(subj, IRI) else subj
                        axiom = ObjectPropertyRange(prop, _as_class_expression(parent))
                    elif axiom_type == AnnotationAssertion:
                        ap = AnnotationProperty(o.iri(slot_uri))
                        axiom = AnnotationAssertion(subj, Annotation(ap, parent))
                    else:
                        raise ValueError(f'Unknown axiom type: {axiom_type}')
                    if axiom is not None:
                        self.add_axiom(axiom, o, axiom_annotations)
                    else:
                        unprocessed_parents.append(parent)
        # all per-slot axioms have been processed; axioms that span
        # multiple slots are now processed
        if "IntersectionOf" in cls_interps:
            if len(unprocessed_parents) == 0:
                raise ValueError(f"Cannot process IntersectionOf with no parents for {element}")
            if len(unprocessed_parents) == 1:
                logging.debug(f"Simplifying IntersectionOf(...) to {unprocessed_parents[0]}")
                return unprocessed_parents[0]
            expr = ObjectIntersectionOf(_as_class_expression_list(*unprocessed_parents))
            logging.debug(f"Returning expression {expr} // {eai.operand_list_index.items()}")
            return expr
        for op_key, operands in eai.operand_list_index.items():
            _, interp, operator = op_key
            logging.debug(f'EntityAxiomIndex {subj}: {interp} => {operator} over {operands}')
            # pre-process operands
            if len(operands) == 0:
                raise ValueError(f'Too few operands: {operands} for {operator} in {subj}')
            if len(operands) == 1:
                logging.debug(f"Simplifying {operator}(...) to {operands[0]}")
                return operands[0]
            elif operator == ObjectUnionOf.__name__:
                expr = ObjectUnionOf(_as_class_expression_list(*operands))
            elif operator == ObjectIntersectionOf.__name__:
                if len(operands) == 1:
                    logging.debug(f"Simplifying IntersectionOf(...) to {operands[0]}")
                    expr = operands[0]
                else:
                    expr = ObjectIntersectionOf(_as_class_expression_list(*operands))
            else:
                raise ValueError(f'Cannot handle operator: {operator}')
            # interpret as axiom
            if interp == EquivalentClasses.__name__:
                axiom = EquivalentClasses(_as_class_expression_list(subj, expr))
            elif interp == SubClassOf.__name__:
                axiom = SubClassOf(_as_class_expression(subj), _as_class_expression(expr))
            elif interp == DisjointClasses.__name__:
                axiom = DisjointClasses(subj, expr)
            elif interp == DisjointUnion.__name__:
                axiom = DisjointUnion(operands[0], operands[1:])
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
        ontology.add_axiom(axiom, set(axiom_annotations))

    def _instance_of_linkml_class(self, v) -> bool:
        try:
            if type(v).class_name:
                return True
        except Exception:
            return False

    def _lookup_slot(self, cls: ClassDefinition, field: str) -> SlotDefinition:
        """
        Lookup a slot in a class by name
        """
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
            if slot.name in sv.class_slots(anc_c):
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
        """
        Retrieve owl annotations for a class, including those inherited from ancestors.

        OWL annotations are specified in LinkML using the annotations slot, where the
        key is "owl" or something in the owl namespace.

        :param cls: class to query
        :param ann_key: annotation key to query
        :return:
        """
        vals = set()
        anc_classes = []
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
        for x in ancs:
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

    def _repair_ofn_iris(self, owl_str: str) -> str:
        """
        Repair OWL Functional Syntax strings by wrapping bare full IRIs in angle brackets.

        In OFN syntax:
        - CURIEs like `ex:Foo` do not need brackets
        - Full IRIs like `http://example.org/Foo` MUST be wrapped: `<http://example.org/Foo>`

        This method detects bare full IRIs and wraps them according to the configured iri_policy.

        Example:
            >>> dumper = OWLDumper()
            >>> dumper._repair_ofn_iris('SubClassOf(ex:A http://example.org/B)')
            'SubClassOf(ex:A <http://example.org/B>)'

        :param owl_str: OWL Functional Syntax string potentially containing bare IRIs
        :return: Repaired string with full IRIs wrapped in angle brackets
        :raises ValueError: If iri_policy is STRICT and bare IRIs are found
        """
        def replace_iri(match):
            iri = match.group(1)
            if self.iri_policy == IRIRepairPolicy.STRICT:
                raise ValueError(
                    f"Bare IRI found in OFN string (iri_policy=STRICT): {iri}\n"
                    f"Full IRIs must be wrapped in angle brackets: <{iri}>"
                )
            if self.iri_policy == IRIRepairPolicy.WARN:
                logging.warning(f"Repairing bare IRI in OFN string: {iri} -> <{iri}>")
            return f'<{iri}>'

        return _FULL_IRI_PATTERN.sub(replace_iri, owl_str)

    def _fix_invalid_curies(self, owl_str: str, prefix_map: Dict[str, str]) -> str:
        """
        Fix invalid CURIEs in OFN output that contain special characters in the local part.

        py-horned-owl may serialize IRIs with special characters as CURIEs, but this is
        invalid in OFN syntax because the CURIE local part has restrictions.

        Invalid characters include:
        - '#' (fragment delimiter)
        - '%' (percent-encoding)
        - '[', ']' (brackets)
        - spaces and other special characters

        This method finds such patterns and expands them to full IRI form.

        Example:
            >>> dumper = OWLDumper()
            >>> prefix_map = {'ex': 'http://example.org/'}
            >>> dumper._fix_invalid_curies('ex:Foo#Bar', prefix_map)
            '<http://example.org/Foo#Bar>'

        :param owl_str: OFN string to fix
        :param prefix_map: Dict mapping prefix names to IRI bases
        :return: Fixed OFN string with invalid CURIEs expanded
        """
        result = owl_str
        for prefix, base in prefix_map.items():
            # Pattern: prefix:localpart with invalid characters (#, %, [, ], etc.)
            # We need to match the CURIE but NOT if it's inside angle brackets
            # Invalid characters in CURIE local parts: #, %, [, ]
            pattern = rf'(?<!<)({re.escape(prefix)}:)([^\s\(\)<>]+[#%\[\]][^\s\(\)<>]*)'

            def replace_curie(match):
                full_local = match.group(2)
                full_iri = base + full_local
                return f'<{full_iri}>'

            result = re.sub(pattern, replace_curie, result)
        return result

    def parse_axioms_string(self, owl_str: str, schemaview: SchemaView = None, prefix_map = None) -> List[AnnotatedComponent]:
        """
        Parse an OWL string into an ontology.

        Example:

            >>> dumper = OWLDumper()
            >>> axiom_components = dumper.parse_axioms_string('SubClassOf(ex:A ex:B)', prefix_map={'ex': 'http://example.org/'})
            >>> assert len(axiom_components) == 1
            >>> axiom_component = axiom_components[0]
            >>> axiom = axiom_component.component
            >>> assert isinstance(axiom, SubClassOf)

        :param owl_str:
        :param schemaview:
        :return:
        """
        prefix_lines = []
        if not schemaview:
            schemaview = self.schemaview
        if schemaview:
            for prefix, url in schemaview.namespaces().items():
                prefix_lines.append(f'Prefix( {prefix}: = <{url}> )')
        if prefix_map:
            for prefix, url in prefix_map.items():
                prefix_lines.append(f'Prefix( {prefix}: = <{url}> )')
        # Note: py-horned-owl does not yet supporting parsing of axioms. Our hack is to
        # create a single-axiom ontology and parse that, and extract the axioms
        header = "\n".join(prefix_lines)
        # Repair bare IRIs before constructing the full document
        owl_str = self._repair_ofn_iris(owl_str)
        owl_str = f'{header}\nOntology(<http://example.org>\n{owl_str}\n)'
        logging.debug(owl_str)
        ont = pyhornedowl.open_ontology_from_string(owl_str, "ofn")
        # TODO: unlike the owlapi, pyhornedowl does not treat some elements
        # as axioms; we may need to broaden this.
        return ont.get_axioms()

    def _element_to_template_dict(self, element: YAMLRoot, val: Any = None):
        def _to_template_value(v):
            """Convert py-horned-owl types to strings for template rendering."""
            if isinstance(v, SimpleLiteral):
                return v.literal
            elif isinstance(v, DatatypeLiteral):
                return v.literal
            elif isinstance(v, IRI):
                iri_str = str(v)
                if '://' in iri_str:
                    return f'<{iri_str}>'
                return iri_str
            return v

        d = {'this': element, 'V': _to_template_value(val)}
        for k, v in vars(element).items():
            d[k] = _to_template_value(v)
        return d

    def add_axioms(self, axioms: List[Union[Axiom, AnnotatedComponent]]):
        for ax in axioms:
            add_axiom(self.ontology, ax)

    def add_axioms_from_fstring(self, fstring: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None):
        if isinstance(fstring, meta.Annotation):
            fstring = fstring.value
        d = self._element_to_template_dict(element, val)
        owl_str = fstring.format(**d)
        logging.debug(f'FSTRING = {owl_str}')
        axioms = self.parse_axioms_string(owl_str)
        logging.debug(f'AXIOMS >> = {axioms}')
        self.add_axioms(axioms)

    def add_axioms_from_template(self, template_ann: Union[str, meta.Annotation], element: YAMLRoot, val: Any = None, schema: SchemaDefinition = None):
        # TODO: simplify, change arg to str
        d = self._element_to_template_dict(element, val)
        if isinstance(template_ann, str):
            tstr = template_ann
        else:
            tstr = template_ann.value
        def _element_to_ofn_str(x) -> str:
            """Transform an element to its OFN string representation for use in templates."""
            expr = self.transform(x, schema=schema, is_element_an_object=False)
            logging.debug(f"template.transform({x}) = {expr}")
            return _serialize_to_ofn(expr)

        def _serialize_to_ofn(expr) -> str:
            """Serialize a py-horned-owl expression to OFN string."""
            if expr is None:
                return ""
            if isinstance(expr, IRI):
                # Wrap full IRIs in angle brackets, leave CURIEs as-is
                iri_str = str(expr)
                if '://' in iri_str:
                    return f'<{iri_str}>'
                return iri_str
            elif isinstance(expr, Class):
                # Class.first is the IRI
                return _serialize_to_ofn(expr.first)
            elif isinstance(expr, ObjectProperty):
                # ObjectProperty.first is the IRI
                return _serialize_to_ofn(expr.first)
            elif isinstance(expr, SimpleLiteral):
                # OFN literal: "value"
                return f'"{expr.literal}"'
            elif isinstance(expr, DatatypeLiteral):
                # OFN typed literal: "value"^^<datatype>
                return f'"{expr.literal}"^^{_serialize_to_ofn(expr.datatype_iri)}'
            elif isinstance(expr, ObjectSomeValuesFrom):
                # ObjectSomeValuesFrom has ope (property) and bce (class expression)
                prop = _serialize_to_ofn(expr.ope)
                filler = _serialize_to_ofn(expr.bce)
                return f'ObjectSomeValuesFrom({prop} {filler})'
            elif isinstance(expr, ObjectAllValuesFrom):
                prop = _serialize_to_ofn(expr.ope)
                filler = _serialize_to_ofn(expr.bce)
                return f'ObjectAllValuesFrom({prop} {filler})'
            elif isinstance(expr, ObjectIntersectionOf):
                # ObjectIntersectionOf.first is a list of class expressions
                operands = ' '.join(_serialize_to_ofn(op) for op in expr.first)
                return f'ObjectIntersectionOf({operands})'
            elif isinstance(expr, ObjectUnionOf):
                operands = ' '.join(_serialize_to_ofn(op) for op in expr.first)
                return f'ObjectUnionOf({operands})'
            elif isinstance(expr, ObjectMinCardinality):
                # Check attribute names for cardinality
                prop = _serialize_to_ofn(expr.ope)
                n = expr.n
                if hasattr(expr, 'bce') and expr.bce:
                    filler = _serialize_to_ofn(expr.bce)
                    return f'ObjectMinCardinality({n} {prop} {filler})'
                return f'ObjectMinCardinality({n} {prop})'
            elif isinstance(expr, DataHasValue):
                # DataHasValue has dp (data property) and l (literal)
                prop = _serialize_to_ofn(expr.dp)
                lit = _serialize_to_ofn(expr.l)
                return f'DataHasValue({prop} {lit})'
            elif isinstance(expr, DataSomeValuesFrom):
                prop = _serialize_to_ofn(expr.dp)
                dr = _serialize_to_ofn(expr.dr)
                return f'DataSomeValuesFrom({prop} {dr})'
            elif isinstance(expr, DataAllValuesFrom):
                prop = _serialize_to_ofn(expr.dp)
                dr = _serialize_to_ofn(expr.dr)
                return f'DataAllValuesFrom({prop} {dr})'
            elif isinstance(expr, DataProperty):
                return _serialize_to_ofn(expr.first)
            elif isinstance(expr, Datatype):
                return _serialize_to_ofn(expr.first)
            elif isinstance(expr, str):
                # Already a string (e.g., from earlier processing)
                if '://' in expr:
                    return f'<{expr}>'
                return expr
            else:
                # Fallback: try str(), but log a warning
                logging.warning(f"Unknown expression type in template serialization: {type(expr)}")
                result = str(expr)
                # Check if it looks like a Python repr
                if 'object at 0x' in result:
                    raise ValueError(f"Cannot serialize {type(expr)} to OFN: {result}")
                return result

        # Register the transform function under both names for compatibility
        if "tr" in d:
            d["_tr"] = _element_to_ofn_str
        else:
            d["tr"] = _element_to_ofn_str
        jt = Template(tstr)
        d["tr"] = _element_to_ofn_str
        owl_str = jt.render(**d)
        axioms = self.parse_axioms_string(owl_str)
        self.add_axioms(axioms)

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
@click.option('-o', '--output',
              type=click.File(mode="w"),
              default=sys.stdout,
              help="Path to OWL functional syntax output")
@click.option('-O', '--output-type',
              type=click.Choice(["ofn", "ttl"]),
              help="Output format")
@click.option("--autofill/--no-autofill",
              default=False,
              show_default=True,
              help="If True, fill missing data slots using string_serialization")
@click.option("--iri-policy",
              type=click.Choice(["repair", "warn", "strict"], case_sensitive=False),
              default="repair",
              show_default=True,
              help="Policy for handling bare IRIs in OFN output: repair (silently fix), warn (fix with warning), strict (error)")
@click.argument('inputfile')
def cli(inputfile: str, schema: str, target_class, module, output, output_type, format, autofill: bool, iri_policy: str, verbose: int, quiet: bool, **args):
    """
    Dump LinkML instance data as OWL

    Examples:

    Convert a CSV to OWL

        linkml-data2owl -s owl_dumper_test.yaml parts.csv -o parts.ofn

    Note in this example, there must be a class type designator column `@type` in the CSV

    Convert a CSV to OWL, homogeneous classes:

        linkml-data2owl -C EquivGenusAndPartOf -s owl_dumper_test.yaml \
            parts_implicit_type.csv -o parts.ofn

    Convert YAML or JSON to OWL:

        linkml-data2owl -s owl_dumper_test.yaml owl_dumper_test_data.yaml -o ont.ofn

    More documentation:

        https://linkml.io/linkml-owl/
    """
    logger = logging.getLogger()
    # Set handler for the root logger to output to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    # Clear existing handlers to avoid duplicate messages if function runs multiple times
    logger.handlers = []
    # Add the newly created console handler to the logger
    logger.addHandler(console_handler)
    if verbose >= 2:
        logger.setLevel(level=logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.WARNING)
    if quiet:
        logger.setLevel(level=logging.ERROR)
    logger.info(f"Loading and compiling schema {schema}")
    if module is None:
        if schema is None:
            raise Exception('must pass one of module OR schema')
        else:
            python_module = PythonGenerator(schema).compile_module()
    else:
        python_module = compile_python(module)
    sv = SchemaView(schema)
    logger.info(f"Loading {inputfile} into schema {sv.schema.name}")
    element = load_structured_file(inputfile, target_class=target_class, python_module=python_module, schemaview=sv, fmt=format)

    dumper = OWLDumper()
    if autofill:
        dumper.autofill = True
    # Map CLI string to enum
    policy_map = {"repair": IRIRepairPolicy.REPAIR, "warn": IRIRepairPolicy.WARN, "strict": IRIRepairPolicy.STRICT}
    dumper.iri_policy = policy_map[iri_policy.lower()]
    doc = dumper.dumps(element, schemaview=sv, output_type=output_type)
    output.write(str(doc))


if __name__ == '__main__':
    cli()
