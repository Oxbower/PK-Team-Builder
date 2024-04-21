import interaction.ReadFiles as read_file
import sys


class JSONHandler:
    def __init__(self):
        self.rf = read_file
        self.sys = sys
        self.pokemon = 0
        self.types = 0
        self.moves = 0
        self.abilities = 0

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
