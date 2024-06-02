import os
import sys
import customtkinter as ctk

from gui import Window as wd
from interaction import Update as run_app


def main():
    """
    Main function to run app
    """

    # initial OS check
    if os.name == "nt" or os.name == "posix":
        print("Supported OS")
    else:
        sys.exit("Unsupported operating system")

    # initialize
    app = run_app.Run()

    # create window object
    new_window = wd.Window(ctk, os, app)
    new_window.create_window()
    window = new_window.root

    # app.load_app()

    # run window main loop
    window.mainloop()


if __name__ == '__main__':
    main()
