import os
import sys

import window as wd
import read_f as rf


def widget_func():
    pass

def main():
    # path = input("path to file")
    # with open(path, newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    # jr.read_in() # Read JSON file

    # load data set
    (types, pkmn, abilities, moves) = rf.load_csv()

    if os.name == "nt" or os.name == "posix":
        import tkinter as tk
    else:
        sys.exit("Unsupported operating system")

    new_window = wd.Window(tk)
    new_window.create_window()
    window = new_window.root

    window.mainloop()


if __name__ == '__main__':
    main()
