import interaction.JsonHandler as json_


class Run:
    def __init__(self):
        self.root = None
        self.info = None

    def load_app(self):
        # load all dependencies to RAM
        json_handler = json_.JSONHandler()
        self.info = json_handler.json_load()

    def get_json(self):
        return self.info()

    def get_id(self, string):
        return self.info.pokemon[string]["pkdex_id"]

    def update_stats(self, string):
        return self.info.pokemon[string]
