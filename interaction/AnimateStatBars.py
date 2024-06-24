import threading


def start_animation(stat_bar, max_value):
    # start thread to improve performance
    thread = threading.Thread(target=animate_stat_bar, args=(stat_bar, max_value, stat_bar.cget('width')))
    thread.run()


def animate_stat_bar(stat_bar, max_value, loop_value: int) -> None:
    if loop_value != max_value:
        stat_bar.configure(width=loop_value)

        if max_value < loop_value:
            loop_value = loop_value - 1
        else:
            loop_value = loop_value + 1

        stat_bar.after(5, animate_stat_bar, stat_bar, max_value, loop_value)
