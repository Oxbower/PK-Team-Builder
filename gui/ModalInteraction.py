import interaction.SearchingAlgorithm as SearchResult
import gui.ModalUpdate as ModalUpdate
import gui.SearchUI as SearchUI


class ModalInteraction:
    def __init__(self, string_var, gui, current_window):

        self.current_window = current_window

        # Updated String (need to keep track of)
        self.string_var = string_var

        self.parent_search_frame = None
        self.name_plate_focused = False

        self.type_adv_active_window = None
        self.button_config = None

        self.searchAlgorithm = SearchResult.SearchResult()

        self.ModalUpdate = ModalUpdate.ModalUpdate(gui, current_window)
        self.SearchUI = SearchUI.SearchUI(self.current_window, self)


    def set_stats_widget(self, stats_widget, type_frame):
        """
        Passes the statistics widget to ModalUpdate
        :param type_frame:
        :param stats_widget: the statistics widget dictionary
        :return: None
        """
        self.ModalUpdate.set_stats_widget(stats_widget)
        self.ModalUpdate.set_variation_frame(type_frame, self.set_string_var, self.name_plate_focus)

    def set_type_widget(self, pokedex_no, type_frame):
        self.ModalUpdate.set_type_widget(pokedex_no, type_frame)

    def set_sidebar_widget(self, sidebar_widget):
        self.ModalUpdate.set_sidebar_widget(sidebar_widget)

    def set_search_modal_frame(self, Frame):
        """
        Sets the search frame after it was built
        :param Frame: search frame widget
        :return: None
        """
        self.parent_search_frame = Frame

    def set_img_frame(self, Frame):
        """
        Set Image frame
        :param Frame: parentFrame for image container
        :param imgFrame: Frame to manipulate when displaying new image
        :return: None
        """
        self.ModalUpdate.set_img_frame(Frame)

    def set_type_advantage_frame(self, frame):
        self.ModalUpdate.set_type_advantage_frame(frame)

    def set_string_var(self, string: str) -> None:
        """
        Sets the string_var for search_bar_callback
        :param string: String being passed into the search bar callback
        :return: None
        """
        self.string_var.set(string)

    def set_move_modal(self, move_modal):
        self.ModalUpdate.set_move_modal(move_modal)

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
            # Check if search bar focused before triggering
            if self.name_plate_focused:
                # build the list containing all matches of string
                search_string = self.searchAlgorithm.build_search_list(search_string)

                # pass in the list to build result frame from
                self.SearchUI.build_search_result(search_string, self.parent_search_frame)

    def move_callback(self, modal_name):
        """
        handles the move_frame modal
        :param modal_name:
        :return:
        """

        # Only update the button pressed
        self.ModalUpdate.update_moves(modal_name)

    def name_plate_focus(self, boolean: bool) -> None:
        """
        Boolean var to detect if focus is on search_bar
        :param boolean: true if focused else
        :return: None
        """
        self.name_plate_focused = boolean

    def clicked_search_query(self, string: str) -> None:
        """
        Detect when any of the search results are clicked
        :param string: name of the clicked result
        :return: None
        """
        self.string_var.set(string)
        self.ModalUpdate.build_path_ref(string)

        self.current_window.root.focus_set()
        # destroy result frame
        self.SearchUI.destroy_result_frame()

    def clicked_item_modal(self, self_modal) -> None:
        """

        :param self_modal:
        :return:
        """
        # open a new window and populate on a new thread, update using modalUpdate
        self.ModalUpdate.update_item_modal(self_modal)

    def clicked_ability_modal(self, self_modal) -> None:
        """

        :param self_modal:
        :return:
        """
        self.ModalUpdate.update_ability_modal(self_modal)

    def type_adv_change_window(self, string: str, new_window, button_config) -> None:
        """
        handles the type advantage window button callback
        :param button_config: button config change color when active
        :param string: which button was pressed
        :param new_window: the window to display
        :return: None
        """
        if self.type_adv_active_window is not None:
            self.button_config.configure(fg_color="#2e2e2e", hover_color='#3f3f3f')
            self.type_adv_active_window.grid_remove()

        self.type_adv_active_window = new_window.get_window()
        self.button_config = button_config

        self.button_config.configure(fg_color='#202020', hover_color='#202020')
        self.type_adv_active_window.grid(row=1, column=0)
