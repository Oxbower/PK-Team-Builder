def type_color(string: str) -> str:
    """
    Chooses the right color for the types background

    :param string: pokemons type
    :return: corresponding color
    """

    match string.lower():
        case 'fire':
            return '#EE8130'
        case 'grass':
            return '#7AC74C'
        case 'bug':
            return '#A6B91A'
        case 'normal':
            return '#aab09f'
        case 'water':
            return '#6390F0'
        case 'electric':
            return '#F7D02C'
        case 'ice':
            return '#96D9D6'
        case 'fighting':
            return '#C22E28'
        case 'poison':
            return '#A33EA1'
        case 'ground':
            return '#cc9f4f'
        case 'flying':
            return '#A98FF3'
        case 'psychic':
            return '#F95587'
        case 'rock':
            return '#B6A136'
        case 'ghost':
            return '#735797'
        case 'dragon':
            return '#6F35FC'
        case 'dark':
            return '#736c75'
        case 'steel':
            return '#B7B7CE'
        case 'fairy':
            return '#D685AD'
        case _:
            return '#aaaaaa'
