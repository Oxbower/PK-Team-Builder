import interaction.SearchingAlgorithm as SearchResult
import gui.ModalUpdate as ModalUpdate
import gui.SearchUI as SearchUI


class ModalInteraction:
    def __init__(self, string_var, gui, current_window):
        # Updated String (need to keep track of)
        self.string_var = string_var

        self.searchFrame = None
        self.name_plate_focused = False

        self.mainWindow = current_window

        self.searchAlgorithm = SearchResult.SearchResult()

        self.modalUpdate = ModalUpdate.ModalUpdate(gui, current_window, self)
        self.SearchUI = SearchUI.SearchUI(self.mainWindow, self)


    def set_stats_widget(self, stats_widget, type_frame):
        """
        Passes the statistics widget to ModalUpdate
        :param type_frame:
        :param stats_widget: the statistics widget dictionary
        :return: None
        """
        self.modalUpdate.set_stats_widget(stats_widget)
        self.modalUpdate.set_variation_frame(type_frame, self.set_string_var, self.name_plate_focus)

    def set_type_widget(self, pokedex_no, type_frame):
        self.modalUpdate.set_type_widget(pokedex_no, type_frame)

    def set_sidebar_widget(self, sidebar_widget):
        self.modalUpdate.set_sidebar_widget(sidebar_widget)

    def set_search_modal_frame(self, Frame):
        """
        Sets the search frame after it was built
        :param Frame: search frame widget
        :return: None
        """
        self.searchFrame = Frame

    def set_img_frame(self, Frame):
        """
        Set Image frame
        :param Frame: parentFrame for image container
        :param imgFrame: Frame to manipulate when displaying new image
        :return: None
        """
        self.modalUpdate.set_img_frame(Frame)

    def set_string_var(self, string: str) -> None:
        """
        Sets the string_var which is the callback function for the
        :param string: String being passed into the search bar callback
        :return: None
        """
        self.string_var.set(string)

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: Necessary arguments for the call back function
        :return: None
        """
        search_string = self.string_var.get()

        if search_string == "":
            print("Empty String")
            self.SearchUI.destroy_result_frame()
        else:
            if self.name_plate_focused:
                # build the list containing all matches of string
                search_string = self.searchAlgorithm.build_search_list(search_string)

                # pass in the list to build result frame from
                self.SearchUI.build_search_result(search_string, self.searchFrame)

    def name_plate_focus(self, boolean: bool) -> None:
        self.name_plate_focused = boolean

    def clicked_search_query(self, string: str) -> None:
        """
        Detect when any of the search results are clicked
        :param string: name of the clicked result
        :return: null
        """
        self.string_var.set(string)
        self.modalUpdate.build_path_ref(string)

        self.mainWindow.root.focus_set()
        # destroy result frame
        self.SearchUI.destroy_result_frame()
