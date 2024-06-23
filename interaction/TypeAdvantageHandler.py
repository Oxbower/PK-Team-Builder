import os

from app_io.LoadJson import json_load
from collections import defaultdict

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


def find_neutral_types(data: list[dict[str, list[str]]]) -> list[str]:
    """
    Finds which are neutral types to current pokemon and excludes them from being displayed

    :param data: dictionary containing this pokemon's types and finds which are neutral
    :return: types that are to be excluded from being displayed
    """

    defensive_typing = {'strengths':    set(),
                        'weaknesses':   set(),
                        'immunity':     set()}

    duplicate_counts = defaultdict(lambda: 0, {})  # count number of occurrences in all 3 defensive areas

    for value in defensive_typing.keys():  # remove duplicates from same key for this pokemon's different types
        for tag in data:
            defensive_typing[value] = defensive_typing[value] | set(tag[value]) # set data struct

    for value in defensive_typing.values():
        for inner_value in value:  # go through all 3 defensive_typing and count how many times each type appears
            duplicate_counts[inner_value] += 1

    return [key for key, value in duplicate_counts.items() if value > 1]
