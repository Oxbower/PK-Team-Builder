def open_variation_frame(parentFrame, delta_width, frame_width, var_frame) -> None:
    var_frame_width = parentFrame.cget("width")

    if var_frame_width < frame_width:
        parentFrame.configure(width=var_frame_width + delta_width)
        parentFrame.after(10, open_variation_frame, parentFrame, delta_width, frame_width, var_frame)
    else:
        for i in var_frame.winfo_children():
            i.grid(sticky="news",
                   pady=5,
                   padx=5,
                   column=0)


def close_variation_frame(parentFrame, delta_width) -> None:
    var_frame_width = parentFrame.cget("width")

    if var_frame_width > 0:
        parentFrame.configure(width=var_frame_width - delta_width)
        parentFrame.after(10, close_variation_frame, parentFrame, delta_width)
