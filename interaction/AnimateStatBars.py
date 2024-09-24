import threading


def start_animation(stat_bar, max_value):
    """
    Animates the stat_bar under the name plate display
    :param stat_bar: the bar to animate
    :param max_value: maximum value for the bar to reach
    :return: None
    """

    # start thread to improve performance
    thread = threading.Thread(target=animate_stat_bar, args=(stat_bar, max_value, stat_bar.cget('width')))
    thread.run()


def animate_stat_bar(stat_bar, max_value, loop_value: int) -> None:
    """
    Recursively calls itself until max value reached
    :param stat_bar: the bar to animate
    :param max_value: maximum value for the bar to reach
    :param loop_value: the current value of the bar incremented each recursion
    :return:
    """
    if loop_value != max_value:
        stat_bar.configure(width=loop_value)

        if max_value < loop_value:
            loop_value = loop_value - 1
        else:
            loop_value = loop_value + 1

        stat_bar.after(5, animate_stat_bar, stat_bar, max_value, loop_value)
