def stat_color_update(currentBase):
    # red, orange, yellow, lightgreen, green, teal
    color = ["#FFA500", "#FFFF00", "#FFFF00", "#86DC3D", "#008000", "#008080"]

    cutoff = [25, 60, 80, 90, 120, 180]

    current_color = "#8B0000"

    for index, value in enumerate(cutoff):
        if currentBase >= value:
            current_color = color[index]

        if currentBase < cutoff[0]:
            return current_color

    return current_color
