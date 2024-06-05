import threading


def start_animation(argument):
    animation_thread = threading.Thread(target=animate_stat_bar, args=argument)
    animation_thread.start()


def animate_stat_bar(Frame, max_value, loop_value: int = 0) -> None:
    if loop_value < max_value:
        Frame.configure(width=loop_value)
        Frame.after(6, animate_stat_bar, Frame, max_value, loop_value + 1)
