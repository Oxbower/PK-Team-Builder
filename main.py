import os
import sys

from customtkinter import CTkFrame as Frame


import window as wd


def main():
    # Switch to customTKinter
    if os.name == "nt" or os.name == "posix":
        import customtkinter as ctk
    else:
        sys.exit("Unsupported operating system")

    new_window = wd.Window(ctk, Frame, os)
    new_window.create_window()
    window = new_window.root

    window.mainloop()


if __name__ == '__main__':
    main()
