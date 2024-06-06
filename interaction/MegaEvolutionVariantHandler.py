import os


def variant_handler(ref_path: list[str]) -> dict[str, list[str]]:
    """
    Handles variants and splits them into mega-evolution and base variants

    :param ref_path: list containing strings that are references to pokemon data
    :return: dictionary containing normal variants and mega-evos
    """

    variant_dict = {'mega': [], 'standard': []}

    for value in ref_path:

        file_name = os.path.splitext(os.path.basename(value))[0]

        if 'Mega' in file_name.split(' '):
            variant_dict['mega'].append(value)
        else:
            variant_dict['standard'].append(value)

    return variant_dict

