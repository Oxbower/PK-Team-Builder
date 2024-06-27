import os.path
from app_io.LoadJson import json_load
import json

def build_move_frame(modal, folder_dir):
    path = os.path.join('pokemon-pokedex', folder_dir, 'moves.json')

    try:
        data = json_load(path)

        print(json.dumps(data, indent=4))
    except FileNotFoundError as e:
        print(e)
        return None