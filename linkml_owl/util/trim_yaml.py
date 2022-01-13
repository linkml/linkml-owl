

def trim_yaml(obj):
    """
    tidies the schema yaml removing redundant info

    TODO: move to schema_as_dict
    """
    if isinstance(obj, dict):
        if 'owl' in obj:
            obj['owl'] = obj['owl']['value']
        for k in ['from_schema', 'owner']:
            if k in obj:
                del obj[k]
        for k, v in obj.items():
            trim_yaml(v)
    elif isinstance(obj, list):
        for v in obj:
            trim_yaml(v)