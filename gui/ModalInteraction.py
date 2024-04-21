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
        """
        Set search frame after it was built
        :param Frame: search frame widget
        :return: None
        """
        self.searchFrame = Frame

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: None
        :return: None
        """
        search_string = self.string_var.get()

        if search_string is "":
            print("Empty String")
            self.modalUpdate.destroy_result_frame()
        else:
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

        self.string_var.set(string)

        self.mainWindow.root.focus_set()
        # destroy result frame
        self.modalUpdate.destroy_result_frame()
