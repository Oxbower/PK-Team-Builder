import sys

from PIL import ImageTk

import interaction.read_f as rf


class Run:
    def __init__(self):
        self.types = {}
        self.pkmn = {}
        self.abilities = {}
        self.moves = {}

    def load_app(self):
        # load all dependencies to RAM
        try:
            # move to a new class
            self.types, self.pkmn, self.abilities, self.moves = rf.load_csv()
            print("Loaded CSV")
        except FileNotFoundError:
            sys.exit("No CSV file found")


    # Bind image to frame
    def display_img(self, image):
        ImageTk.PhotoImage(image)


    # k-tree search
    def search_string(self, string):
        print(self.pkmn[string])
