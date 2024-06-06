def start_animation(*args):
    animate_stat_bar(args[0], args[1])


def animate_stat_bar(Frame, max_value, loop_value: int = 0) -> None:
    if loop_value < max_value:
        Frame.configure(width=loop_value)
        Frame.after(6, animate_stat_bar, Frame, max_value, loop_value + 1)