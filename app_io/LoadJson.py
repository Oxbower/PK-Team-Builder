import json
from os import listdir


def json_load(path):
    """
    Load JSON files into ram
    """
    with open(path, "r") as ref:
        data = json.load(ref)

    return data


def load_names(directory: str) -> list[str]:
    """
    Load pokemon names
    :param directory: directory to load names from
    :return: list of names
    """
    return listdir(directory)
