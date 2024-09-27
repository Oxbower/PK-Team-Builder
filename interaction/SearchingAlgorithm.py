import gui.Gui
from app_io.LoadJson import load_pokemon_names as load_names

import re


class SearchResult:
    """
    Handles the searching algorithm and building the list to return
    """
    def __init__(self):
        self.names = load_names()

    def build_search_list(self, search_string):
        """
        Builds the search list and passes it to ModalUpdate to build the search query
        :param search_string:
        :return:
        """
        print(f"Search String: \"{search_string}\", Building search list...")

        # find the matching string and return it to modalInteraction to build the UI
        return self.search_string_algo(search_string)

    def search_string_algo(self, string):
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

        # Change to a dictionary later
        for i in self.names:
            # regex looking for strings that match the start
            str_builder = "^" + new_case

            x = i.split('-')
            y = " ".join(x)

            try:
                if re.search(str_builder, y):
                    names.append(y)
            except re.error:
                print("Invalid Regex")
                return

        print(f"Matching Substring: {names}")

        return names
