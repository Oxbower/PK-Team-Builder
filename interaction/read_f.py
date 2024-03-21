import json
import os

from PIL import Image, ImageTk


def build_img_ref(index):
    """
        Build os dependent path for image loader
    """
    build_href = os.path.join('pkdex-imgs', 'images' + index.lstrip('0') + '.jpg')
    image = Image.open(build_href)
    return image


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


def load_csv():
    """
        Load JSON files into ram
    """
    d_ref = ['types', 'pokemon', 'abilities', 'moves']

    for i in range(len(d_ref)):
        with open(build_path(d_ref[i])) as ref:
            val = json.load(ref)
            d_ref[i] = val

    unwrapped_data = unwrap_json(d_ref[1])

    return d_ref[0], unwrapped_data, d_ref[2], d_ref[3]
