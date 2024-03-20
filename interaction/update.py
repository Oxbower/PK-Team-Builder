import sys

from PIL import ImageTk

import interaction.read_f as rf
import interaction.json_handler as ff


class Run:
    def __init__(self):
        self.types = {}
        self.pkmn = {}
        self.abilities = {}
        self.moves = {}

    def load_app(self):
        # load all dependencies to RAM
        json_handler = ff.json_handler(rf, sys)

        self.info = json_handler.json_load()



    # Bind image to frame
    def display_img(self, image):
        ImageTk.PhotoImage(image)


    def search_string(self, string):
        names = []
        if self.info.pokemon.keys().__contains__(string):
            print(self.info.pokemon[string])
            return
        for i in self.info.pokemon:
            if str(i).find(string) != -1:
                names.append(i)

        print(f"\r {names}")
        # return all matching substring
