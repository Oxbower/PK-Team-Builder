class ModalInteraction:
    def __init__(self, stringVar):
        self.string_var = stringVar
        pass

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: None
        :return: None
        """

        print(self.string_var.get())
        pass

    def __call_back(self, *args):
        # Remove focus add to selector
        # self.root.focus_set()

        # build result bar
        # self.__focus(name_plate, parent_frame, True)

        # grep all strings w/ same substring
        self.query_result = self.app.search_string(self.string_var.get())

        # handle search
        self.searchHandler.search(query_result=self.query_result)

        # for testing
        # var = self.__display_img()
        # if var:
        #     self.__update_stats(self.query_result[0])
