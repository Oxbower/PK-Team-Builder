import json
import os

from PIL import Image

'''
    Build os dependent path for image loader
'''
def build_img_ref(index):
    build_href = os.path.join('pkdex-imgs', 'images') + index.lstrip('0') + '.jpg'
    image = Image.open(build_href)
    return image


'''
    Build os dependent path for json
'''
def build_path(file_name):
    str = os.path.join('data', file_name) + '.json'
    return str


'''
    Load JSON files into ram
'''
def load_csv():
    d_ref = ['types', 'pokemon', 'abilities', 'moves']

    for i in range(len(d_ref)):
        with open(build_path(d_ref[i])) as ref:
            val = json.load(ref)
            d_ref[i] = val

    return d_ref[0], d_ref[1], d_ref[2], d_ref[3]
