import interaction.ReadFiles as read_file
import sys
import json
from os import listdir


class JSONHandler:
    def __init__(self):
        self.rf = read_file
        self.sys = sys
        self.pokemon = 0
        self.types = 0
        self.moves = 0
        self.abilities = 0
        self.pokemon_names = listdir("pokemon-artwork")

    def json_load(self):
        """
        Loads all json files into this class
        :return: self
        """
        try:
            self.types, self.pokemon, self.abilities, self.moves = self.rf.load_csv()
            print("Loaded JSON")
        except FileNotFoundError:
            self.sys.exit("No JSON file found")

        return self

    def load_image_directory(self):
        """
        Loads image directory from 'pokemon-artwork' folder
        :return: self
        """
        return self.pokemon_names
