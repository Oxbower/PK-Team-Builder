

class json_handler():
    def __init__(self, rf, sys):
        self.rf = rf
        self.sys = sys
        self.pokemon = 0
        self.types = 0
        self.moves = 0
        self.abilities = 0

    def json_load(self):
        try:
            self.types, self.pokemon, self.abilities, self.moves = self.rf.load_csv()
            print("Loaded JSON")
        except FileNotFoundError:
            self.sys.exit("No JSON file found")

        return self
