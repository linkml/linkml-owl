import csv
import json
import logging
from copy import copy
from dataclasses import dataclass
from io import StringIO
from types import ModuleType

from typing import Union, TextIO, Type, Optional, List, Dict

import click
import yaml
from hbreader import FileInfo, hbread
from jsonasobj2 import as_dict
from linkml.generators.pythongen import PythonGenerator
from linkml.utils import datautils
from linkml.utils.datautils import infer_index_slot, _is_xsv, get_dumper
from linkml_runtime import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition, SlotDefinition
from linkml_runtime.loaders import json_loader, yaml_loader, csv_loader, rdf_loader, rdflib_loader
from linkml_runtime.utils.compile_python import compile_python

from linkml_runtime.utils.yamlutils import YAMLRoot, DupCheckYamlLoader

@dataclass
class Container:
    objects: List = None


def load_from_csv(source: str, delimiter=None) -> List[Dict]:
    if not delimiter and isinstance(source, str):
        with open(source) as tmpstream:
            line = tmpstream.readline()
            if '\t' in line:
                delimiter = '\t'
            elif ',' in line:
                logging.warning(f'Using implicit delimiter: {delimiter}')
                delimiter = ','
            else:
                raise ValueError(f'Cannot infer delimited - please pass explicitly')
    if isinstance(source, str):
        instream = open(source)
    else:
        instream = source
    r = csv.DictReader(instream, delimiter=delimiter, quoting=csv.QUOTE_NONE, escapechar="\\")
    def opt_split(s:str) -> Union[List, str]:
        if s != "":
            if '|' in s:
                return s.split('|')
            else:
                return s
        else:
            return None
    objs = []
    for row in r:
        if row:
            obj = {k: opt_split(v) for k, v in row.items() if v != ""}
            objs.append(obj)
    return objs


def load_structured_file(source: Union[str, dict, TextIO], target_class: Union[str, Type[YAMLRoot]] = None, fmt: str = None,
                         index_slot: str = None,
                         python_module = None,
                         normalize_csvs = False,
                         delimiter = None,
                         schema: Union[str, SchemaDefinition] = None,
                         schemaview: SchemaView = None) -> Union[YAMLRoot, List[YAMLRoot]]:
    """
    Wraps multiple runtime loaders, loading from a variety of source types, yielding a LinkML object or objects

    The input can be a YAML/JSON, RDF, or CSV/TSV. For YAML/JSON files, these can be either lists or a dict.

    All objects created will be of type target_class; if this is not specified, then it may be inferred:

    - if the schema specified a tree_root, this is used
    - if the objects contain a type designator, this is used

    :param source: path or data or stream
    :param target_class: class to be instantiated, either name or the python class
    :param fmt: Any of yaml, json, csv, ttl. inferred if None and source is a file path
    :param python_module: python module for datamodel classes
    :param schema:
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
            schema = schemaview.schema
    if target_class is None:
        # TODO: de-convolute this
        # attempt to infer root class, but if this cannot
        # be found then we rely on there being a type designator present
        try:
            target_class = datautils.infer_root_class(schemaview)
        except:
            pass
    if target_class and isinstance(target_class, str):
        target_class = python_module.__dict__[target_class]
    if isinstance(source, str):
        fmt = datautils._get_format(source, fmt)
    type_designator = get_type_designator(schemaview)
    if datautils._is_xsv(fmt):
        loader = csv_loader
        if normalize_csvs:
            if index_slot is None:
                index_slot = infer_index_slot(schemaview, target_class)
                if index_slot is None:
                    raise Exception('--index-slot is required for CSV input')
            out_obj = csv_loader.load(source, index_slot=index_slot, schema=schema)
        else:
            obj = load_from_csv(source, delimiter=delimiter)
            logging.debug(f'INST {target_class} <= {obj}')
            out_obj = [instantiate_object(x, target_class, python_module=python_module, schemaview=schemaview) for x in obj]
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
            out_obj = [instantiate_object(x, target_class, type_designator=type_designator, python_module=python_module, schemaview=schemaview) for x in obj]
        else:
            out_obj = instantiate_object(obj, target_class, type_designator=type_designator, python_module=python_module, schemaview=schemaview)
    else:
        raise ValueError(f'Unknown format: {fmt}')
    logging.info(f'Loaded {type(out_obj)} using {loader}')
    return out_obj

def instantiate_object(data: Dict, target_class: Type[YAMLRoot] = None, schemaview: SchemaView = None,
                       type_designator: str = '@type',
                       python_module: ModuleType = None) -> YAMLRoot:
    #if not(target_class or schemaview):
    #    raise ValueError(f'Must pass AT LEAST ONE OF target_class OR schemaview')
    if not target_class:
        if type_designator in data:
            target_class_name = data[type_designator]
            if ':' in target_class_name:
                pfx, loc = str(target_class_name).split(':')
                target_class_name = loc
            data = copy(data)
        else:
            raise ValueError(f'Cannot determine type for {data}')
        target_class = python_module.__dict__[target_class_name]
        if '@type' in data:
            del data['@type']
    return target_class(**as_dict(data))

def get_type_designator(schemaview: SchemaView = None) -> str:
    designators = []
    for s in schemaview.all_slots().values():
        if s.designates_type:
            designators.append(s.name)
    if len(designators) > 1:
        logging.error(f'Multiple type designators: {designators}')
    if designators:
        return designators[0]
    else:
        return '@type'

def add_index_slot(sv: SchemaView) -> None:
    container = ClassDefinition('Container', from_schema='http://x.org/')
    for cn in sv.all_classes():
        a = SlotDefinition(cn, multivalued=True, range=cn, inlined=True, inlined_as_list=True)
        container.attributes[a.name] = a
    sv.add_class(container)
    sv.set_modified()


@click.command()
@click.option('-s', '--schema', required=True,
              help="Path to LinkML schema")
@click.option("--target-class", "-C",
              help="name of class in datamodel that the root node instantiates")
@click.option("--module", "-m",
              help="Path to python datamodel module")
@click.option("--index-slot", "-S",
              help="top level slot. Required for CSV dumping/loading")
@click.option("--format", "-f",
              help="Input format (will be inferred from file suffix if not specified)")
@click.option('-o', '--output', required=True,
              help="Path to OWL functional syntax output")
@click.option('-t', '--output-format',
              default='tsv',
              help="Output format")
@click.argument('inputfile')
def cli(inputfile: str, schema: str, target_class, module, output, format, index_slot, output_format, **args):
    """
    converts

    """
    sv = SchemaView(schema)
    add_index_slot(sv)
    if module is None:
        if schema is None:
            raise Exception('must pass one of module OR schema')
        else:
            python_module = PythonGenerator(sv.schema).compile_module()
    else:
        python_module = compile_python(module)
    element = load_structured_file(inputfile, target_class=target_class,
                                   python_module=python_module, schemaview=sv, fmt=format)
    outargs = {}
    if _is_xsv(output_format):
        if index_slot is None:
            index_slot = infer_index_slot(sv, target_class)
            if index_slot is None:
                raise Exception('--index-slot is required for CSV output')
        outargs['index_slot'] = index_slot
        outargs['schema'] = schema
    dumper = get_dumper(output_format)
    if output is not None:
        dumper.dump(element, output, **outargs)
    else:
        print(dumper.dumps(element, **outargs))


if __name__ == '__main__':
    cli()



