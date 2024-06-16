import json


def json_load(path):
    """
    Load JSON files into ram
    """
    with open(path, "r") as ref:
        data = json.load(ref)

    return data
