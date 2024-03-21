import os
import sys

from customtkinter import CTkFrame as Frame

import window as wd
from interaction import update as run_app


def main():
    """
    Main function to run app
    """
    if os.name == "nt" or os.name == "posix":
        import customtkinter as ctk
    else:
        sys.exit("Unsupported operating system")

    app = run_app.Run()

    new_window = wd.Window(ctk, Frame, os, app)
    new_window.create_window()
    window = new_window.root

    app.load_app()

    window.mainloop()


if __name__ == '__main__':
    main()
