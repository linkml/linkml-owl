import json
import logging
from copy import copy
from io import StringIO

from typing import Union, TextIO, Type, Optional, List, Dict

import yaml
from hbreader import FileInfo, hbread
from jsonasobj2 import as_dict
from linkml.utils import datautils
from linkml.utils.datautils import infer_index_slot
from linkml_runtime import SchemaView
from linkml_runtime.loaders import json_loader, yaml_loader, csv_loader, rdf_loader, rdflib_loader

from linkml_runtime.utils.yamlutils import YAMLRoot, DupCheckYamlLoader


def load_structured_file(source: Union[str, dict, TextIO], target_class: Union[str, Type[YAMLRoot]], fmt: str = None,
                         python_module = None,
                         schema: SchemaDefinition = None,
                         schemaview: SchemaView = None) -> Union[YAMLRoot, List[YAMLRoot]]:
    """
    Wraps multiple runtime loaders, loading from a variety of source types, yielding a LinkML object or objects

    The input can be a YAML/JSON, RDF, or CSV/TSV. For YAML/JSON files, these can be either lists or a dict.

    All objects created will be of type target_class; if this is not specified, then it may be inferred:

    - if the schema specified a tree_root, this is used
    - if the objects contain a type designator, this is used

    TODO: add tests
    
    :param source: path or data or stream
    :param target_class: class to be instantiated, either name or the python class
    :param fmt: Any of yaml, json, csv, ttl. inferred if None and source is a file path
    :param python_module: python module for datamodel classes
    :param schemaview: required if the input is CSV or RDF
    :return: Either a single LinkML object OR a list of them
    """
    if schema is not None:
        if schemaview is not None:
            if schemaview.schema == schema:
                logging.warning(f'schemaview and schema redundantly specified')
            else:
                raise ValueError(f'schemaview OR schema should be specified')
        else:
            schemaview = SchemaView(schema)
    if target_class is None:
        target_class = datautils.infer_root_class(schemaview)
    if target_class and isinstance(target_class, str):
        target_class = python_module.__dict__[target_class]
    if isinstance(source, str):
        fmt = datautils._get_format(source, fmt)
    if datautils._is_xsv(fmt):
        if index_slot is None:
            index_slot = infer_index_slot(sv, target_class)
            if index_slot is None:
                raise Exception('--index-slot is required for CSV input')
        loader = csv_loader
        out_obj = csv_loader.load(source, index_slot=index_slot, schema=schema)
    elif datautils._is_rdf_format(fmt):
        loader = rdflib_loader
        out_obj = rdflib_loader.load(source, schemaview=schemaview, fmt=fmt)
    elif fmt == 'yaml' or fmt == 'json':
        if not isinstance(source, dict) and not isinstance(source, list):
            data = hbread(source, FileInfo())
        else:
            data = source
        if fmt == 'yaml':
            obj = yaml.load(StringIO(data), DupCheckYamlLoader) if isinstance(data, str) else data
            loader = yaml_loader
        else:
            obj = json.loads(data) if isinstance(data, str) else data
            loader = json_loader
            loader.json_clean(obj)
        if isinstance(obj, list):
            out_obj = [instantiate_object(x, target_class, python_module=python_module) for x in obj]
        else:
            out_obj = instantiate_object(obj, target_class, python_module=python_module)
    else:
        raise ValueError(f'Unknown format: {fmt}')
    logging.info(f'Loaded {type(out_obj)} using {loader}')
    return out_obj

def instantiate_object(data: Dict, target_class: Type[YAMLRoot] = None, schemaview: SchemaView = None, python_module=None) -> YAMLRoot:
    #if not(target_class or schemaview):
    #    raise ValueError(f'Must pass AT LEAST ONE OF target_class OR schemaview')
    if not target_class:
        if '@type' in data:
            target_class_name = data['@type']
            data = copy(data)
        else:
            raise ValueError(f'Cannot determine type for {data}')
        target_class = python_module.__dict__[target_class_name]
        if '@type' in data:
            del data['@type']
    return target_class(**as_dict(data))




