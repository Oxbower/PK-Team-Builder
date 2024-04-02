import re
import sys

from PIL import ImageTk

import interaction.ReadFiles as read_file
import interaction.JsonHandler as json_


class Run:
    def __init__(self):
        self.root = None
        self.info = None

    def load_app(self):
        # load all dependencies to RAM
        json_handler = json_.JSONHandler(read_file, sys)

        self.info = json_handler.json_load()

    def get_id(self, string):
        return self.info.pokemon[string]["pkdex_id"]

    def search_string(self, string):
        """
        Adds searching functionality to name_plate
        :param string: searching substring
        :return names: array containing all names with substring
        """
        names = []
        if string == "":
            return names

        # Search string
        new_case = str.lower(string)

        for i in self.info.pokemon:
            str_builder = "^" + new_case
            if re.search(str_builder, i):
                names.append(i)

        return names

    def update_stats(self, string):
        return self.info.pokemon[string]
