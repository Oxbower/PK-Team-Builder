import json
from os import listdir


def json_load(path):
    """
    Load JSON files into ram
    """
    with open(path, "r") as ref:
        data = json.load(ref)

    return data


def load_pokemon_names() -> list[str]:
    """
    Load pokemon names
    :return: list of names
    """
    return listdir("pokemon-artwork")
