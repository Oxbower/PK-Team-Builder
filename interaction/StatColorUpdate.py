def stat_color_update(currentBase):
    """
    Update the color of the stat_bar depending on value
    :param currentBase: base value of this pokemons given stat
    :return: returns the hexcode color to use
    """
    # red, orange, yellow, lightgreen, green, teal
    color = ["#FFA500", "#FFFF00", "#FFFF00", "#86DC3D", "#008000", "#008080"]

    cutoff = [25, 60, 80, 90, 120, 150]

    current_color = "#8B0000"

    for index, value in enumerate(cutoff):
        if currentBase >= value:
            current_color = color[index]

        if currentBase < cutoff[0]:
            return current_color

    return current_color
