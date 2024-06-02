import json
import os

from PIL import Image


def build_img_ref(inner_path):
    """
    Build os dependent path for image loader
    """
    path = []
    build_href = os.path.join('pokemon-artwork', inner_path)
    for i in os.listdir(build_href):
        path.append(os.path.join(build_href, i))

    return path


def build_path(file_name):
    """
    Build os dependent path for json
    """
    ref_path = os.path.join('data', file_name) + '.json'
    try:
        open(ref_path, 'r').close()
        print(ref_path, 'successfully loaded')
    except FileNotFoundError:
        print('can\'t find', ref_path)

    return ref_path


def unwrap_json(json_data):
    """
    Fix json gen
    """
    text = {}
    for i in json_data:
        key = [str.lower(j) for j in i.keys()]
        text[key[0]] = dict(ele for sub in i.values() for ele in sub.items())

    return text


def json_load(path):
    """
    Load JSON files into ram
    """
    with open(path, "r") as ref:
        data = json.load(ref)

    return data
