import os

from app_io.LoadJson import json_load
from collections import defaultdict

type_defensive = json_load(os.path.join('data', 'type-defensive.json'))
type_offensive = json_load(os.path.join('data', 'type-offensive.json'))


def type_advantage_defensive_handler(data):
    """
    finds the types current pokemon has defensive advantage to
    :param data: type fo this pokemon
    :return: None
    """
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


def find_type_defense(types: list[str]):
    """

    :param types:
    :return:
    """
    defensive_types = []

    for value in type_defensive:
        for tag in types:
            if value['name'] == tag:
                defensive_types.append(value)

    return defensive_types


def find_defensive_type_multiplier(data: list[dict[str, str, str, str]], type_check: str) -> (str, int):
    """
    finds the multiplier for this defensive typing
    :param data: this pokemons types and their defensive qualities
    :param type_check: type to check against this pokemons type data
    :return: string and size of the type icon
    """
    base = 1
    size = 10
    dict_tags = ['strengths', 'weaknesses', 'immunity']

    for value in data:
        for tag in dict_tags:
            if type_check in value[tag]:
                if tag == 'strengths':
                    base *= .5
                elif tag == 'weaknesses':
                    base *= 2
                else:
                    base *= 0

    if base == .5:
        size = 9
    elif base == .25:
        size = 8

    if base != 0:
        string = str(base).lstrip('0') + 'x'
    else:
        string = str(int(base)) + 'x'

    return string, size
