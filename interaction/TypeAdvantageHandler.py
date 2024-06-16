import threading
import os

from app_io.LoadJson import json_load

type_defensive = json_load(os.path.join('data', 'type-defensive.json'))
type_offensive = json_load(os.path.join('data', 'type-offensive.json'))


def type_advantage_defensive_handler(data):
    types_defensive_adv = []
    type = [i for i in data['type'].values()]

    for value in type:
        for types in type_defensive:
            if value == types['name']:
                types_defensive_adv.append(types)

    return types_defensive_adv