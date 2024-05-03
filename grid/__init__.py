"""
Two functions that is essential in generate hyper-parameter
grid:
1. unravel: generate a list of config dictionaries from
    a given dictionary of config grid.
2. update: recursively update a given dictionary with
    new values.
"""

from itertools import product
import yaml



def load_yaml(filename):
    """
    load a yaml file with given filename
    """
    with open(filename, 'r', encoding='UTF-8') as handle:
        return yaml.safe_load(handle)


def save_yaml(filename, mydict):
    """
    load a yaml file with given filename
    """
    with open(filename, 'w', encoding='UTF-8') as handle:
        return yaml.dump(mydict, handle)


def unravel(obj):
    """
    Generate a list of config dictionary from a config grid
    """
    if not isinstance(obj, dict):
        if isinstance(obj, list) or isinstance(obj, tuple):
            return list(obj)
        return [obj]

    keys = obj.keys()
    temp = [unravel(value) for value in obj.values()]

    return [dict(zip(keys, params)) for params in product(*temp)]


def update(config, updates):
    """
    Inplace update of the config
    """
    for key in config:
        if key in updates:
            if isinstance(config[key], dict):
                update(config[key], updates[key])
            else:
                config[key] = updates[key]
