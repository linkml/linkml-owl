import csv
from typing import Type, List

from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.utils.yamlutils import YAMLRoot


def csv_to_objects(csv_file: str, schemaview: SchemaView, target_class: Type[YAMLRoot] = None, delimiter='\t') -> List[YAMLRoot]:
    #if target_class is None:
    if isinstance(csv_file, str):
        instream = open(csv_file)
    else:
        instream = csv_file
    reader = csv.DictReader(instream, delimiter=delimiter, quoting=csv.QUOTE_NONE, escapechar="\\")
    objs = []
    for row in reader:
        print(f'ROW={row}')
        obj = target_class(**row)
        objs.append(obj)
    return objs


