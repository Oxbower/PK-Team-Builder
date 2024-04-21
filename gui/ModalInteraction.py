import interaction.SearchResult as SearchResult
import gui.ModalUpdate as ModalUpdate


class ModalInteraction:
    def __init__(self, stringVar, gui, ctk, mainWindow, Frame):
        # Updated String need to keep track of
        self.string_var = stringVar

        self.searchFrame = None

        self.mainWindow = mainWindow

        self.searchAlgorithm = SearchResult.SearchResult()
        self.modalUpdate = ModalUpdate.ModalUpdate(gui, ctk, mainWindow, Frame, self)

    def set_search_modal_frame(self, Frame):
        self.searchFrame = Frame

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: None
        :return: None
        """
        search_string = self.string_var.get()

        # build the list containing all matches of string
        search_string = self.searchAlgorithm.build_search_list(search_string)

        # pass in the list to build result frame from
        self.modalUpdate.build_search_result(search_string, self.searchFrame)

    def clicked_button(self, string):
        """
        Detect when any of the search results are clicked
        :param string: name of the clicked result
        :return: null
        """
        print(string)

        self.mainWindow.root.focus_set()
        # destroy result frame
        self.modalUpdate.destroy_result_frame()


    #def __call_back(self, *args):
        # Remove focus add to selector
        # self.root.focus_set()

        # build result bar
        # self.__focus(name_plate, parent_fr
        # grep all strings w/ same substring
        #self.query_result = self.app.search_string(self.string_var.get())

        # handle search
        #self.searchHandler.search(query_result=self.query_result)

        # for testing
        # var = self.__display_img()
        # if var:
        #     self.__update_stats(self.query_result[0])
