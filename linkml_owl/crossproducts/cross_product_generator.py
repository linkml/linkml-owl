"""
Cross-Product Generator

For any instance a that has an xp declaration:

1. compute all instances G=i1..in that are reachable from a over xp.propagates_over
2. for each i in combination of i1..in, create a new instance i' that is a copy of i
    - tr(i) = i'
    - i' = xp.create(i), this assigns parentage
    - the identifier for i' is computed from xp.id_format
    - for all slot-values i.s=v, if v is in G, then i'.s = tr(v)

"""
import itertools
import logging
from dataclasses import dataclass
from types import ModuleType
from typing import List, Any

import yaml
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import SlotDefinition, ClassDefinitionName
from linkml_runtime.utils.yamlutils import YAMLRoot


XP_PROPERTY = "cross_product_generator"

@dataclass
class CrossProductGenerator:
    """
    Generate cross products of a set of classes
    """
    schemaview: SchemaView
    python_model: ModuleType = None

    def materialize(self, inst: YAMLRoot) -> int:
        """
        Materialize cross products
        """
        num_new_elements = 0
        if isinstance(inst, list):
            for i in inst:
                num_new_elements += self.materialize(i)
            return num_new_elements
        elif isinstance(inst, dict):
            for _, v in inst.items():
                num_new_elements += self.materialize(v)
            return num_new_elements
        try:
            vars(inst)
        except TypeError:
            return 0
        sv = self.schemaview
        typ = type(inst)
        cls = sv.get_class(typ.__name__)
        if cls is None:
            logging.debug(f"Bottomed out at {inst}")
            return num_new_elements
        id_slot = sv.get_identifier_slot(cls.name)
        id = getattr(inst, id_slot.name) if id_slot is not None else None
        for s in sv.class_induced_slots(cls.name):
            if XP_PROPERTY in s.annotations:
                xp = s.annotations[XP_PROPERTY].value
                xp_parsed = yaml.safe_load(xp)
                num_new_elements += self.generate_cross_products(id, inst, s, xp_parsed, ClassDefinitionName(s.range))
        for k, v in vars(inst).items():
            num_new_elements += self.materialize(v)
        return num_new_elements

    def generate_cross_products(self, id: str, inst: YAMLRoot, index_slot: SlotDefinition, xp: dict, target_class: ClassDefinitionName) -> int:
        """
        Generate cross product for a slot
        """
        target_class_id_slot = self.schemaview.get_identifier_slot(target_class)
        xp_slots = xp["slots"]
        propagates_over = xp["propagates_over"]
        id_format = xp["id_format"]
        gen = []
        n = 0
        slot_names = []
        for sn, expr in xp_slots.items():
            slot_names.append(sn)
            if expr == ".":
                gen.append(["."])
            else:
                vs = getattr(inst, expr, [])
                if vs:
                    gen.append(vs)
                    n += 1
        if n == 0:
            return 0
        num_new_elements = 0
        for idx in itertools.product(*[combo for combo in gen]):
            obj = self.from_template(inst, id, slot_names, idx, id_format, target_class, target_class_id_slot, propagates_over)
            id_val = obj[target_class_id_slot.name]
            curr_objs = getattr(inst, index_slot.name)
            if isinstance(curr_objs, list):
                if id_val in [getattr(o, target_class_id_slot.name) for o in curr_objs]:
                    print(f"Skipping {id_val} because it already exists")
                else:
                    curr_objs.append(obj)
                    num_new_elements += 1
            elif isinstance(curr_objs, dict):
                if id_val in curr_objs:
                    print(f"GOT: {id_val}")
                else:
                    curr_objs[id_val] = obj
                    num_new_elements += 1
            else:
                raise ValueError(f"Unexpected type for {index_slot.name}: {type(curr_objs)}")
        return num_new_elements

    def from_template(self, inst: YAMLRoot, id: str, slot_names: List[str], idx: List[Any], id_format: str, target_class: ClassDefinitionName, target_class_id_slot: SlotDefinition, propagates_over: List[str]) -> dict:
        """
        Generate a cross product object from a template
        """
        obj = {}
        for i in range(0, len(slot_names)):
            v = idx[i]
            if v == '.':
                v = id
            obj[slot_names[i]] = v
        id_val = id_format.format(**obj)
        obj[target_class_id_slot.name] = id_val
        for p in propagates_over:
            rng = self.schemaview.induced_slot(p, target_class).range
            children = getattr(inst, p, [])
            if isinstance(children, dict):
                obj[p] = {}
                for k, v in children.items():
                    child = self.from_template(v, k, slot_names, idx, id_format, rng, target_class_id_slot, propagates_over)
                    child_id = getattr(child, target_class_id_slot.name)
                    obj[p][child_id] = child
            else:
                raise NotImplementedError(f"{p} range is type {type(children)} which must be a dict")
        py_cls = self.python_model.__dict__[target_class]
        #print(f"GENERATING {target_class} = {obj}")
        return py_cls(**obj)




