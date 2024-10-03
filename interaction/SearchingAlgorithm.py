import os.path

from app_io.LoadJson import load_names as load_names

import re


class SearchResult:
    """
    Handles the searching algorithm and building the list to return
    """
    def __init__(self):
        pass

    def build_search_list(self, search_string: str, directory: str):
        """
        Builds the search list and passes it to ModalUpdate to build the search query
        :param search_string:
        :return:
        """

        print(f"Search String: \"{search_string}\", Searching in directory: {directory}")
        directory_contents = load_names(directory)
        # find the matching string and return it to modalInteraction to build the UI
        return self.search_string_algo(search_string, directory_contents)

    def normalize_list(self, directory: list[str]) -> list[str]:
        """
        Normalizes the contents of the directory so we can actually search it
        :param directory:
        :return:
        """
        normalized_list = []
        for item in directory:
            split = item.split(" ")
            lower_cased = []
            for i in split:
                lower_cased.append(i.lower())
            normalized = " ".join(lower_cased)
            normalized_list.append(os.path.splitext(os.path.basename(normalized))[0])
        return normalized_list

    def search_string_algo(self, string: str, directory_contents: list[str]) -> list[str]:
        """
        Adds searching functionality to name_plate
        :param directory_contents: contents of this directory
        :param string: searching substring
        """
        names = []
        if string == "":
            return names

        # Search string
        new_case = str.lower(string)

        normalized_list = self.normalize_list(directory_contents)

        # Change to a dictionary later
        for i in normalized_list:
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
