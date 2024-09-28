import interaction.SearchingAlgorithm as SearchResult
import gui.ModalUpdate as ModalUpdate
import gui.searchgui.SearchUI as SearchUI

from customtkinter import CTkButton as CTkButton

class ModalInteraction:
    def __init__(self, gui, current_window):
        """
        initializes the ModalInteraction class
        :param gui: the GUI class instance
        :param current_window: the ctk window instance
        """
        self.current_window = current_window

        self.parent_search_frame = None

        self.type_adv_active_window = None
        self.button_config = None

        self.searchAlgorithm = SearchResult.SearchResult()

        self.ModalUpdate = ModalUpdate.ModalUpdate(gui, current_window)

        # Instantiate the class that builds the UI for the search results
        self.SearchUI = SearchUI.SearchUI(self.current_window, self)

    def set_stats_widget(self, stats_widget, type_frame):
        """
        Passes the statistics widget to ModalUpdate
        :param type_frame:
        :param stats_widget: the statistics widget dictionary
        :return: None
        """
        self.ModalUpdate.set_stats_widget(stats_widget)
        self.ModalUpdate.set_variation_frame(type_frame)

    def set_type_widget(self, pokedex_no, type_frame):
        """
        sets the widget under the pokemon portrait to be updated
        :param pokedex_no: this pokemon's pokedex num
        :param type_frame: the frame where to add this pokemons types
        :return: None
        """
        self.ModalUpdate.set_type_widget(pokedex_no, type_frame)

    def set_sidebar_widget(self, sidebar_widget):
        """
        sets the widget to the right of the pokemon portrait to
        add possible transformations this pokemon is capable of
        :param sidebar_widget: the sidebar widget
        :return: None
        """
        self.ModalUpdate.set_sidebar_widget(sidebar_widget)

    def set_search_modal_frame(self, Frame, name_plate: CTkButton):
        """
        Sets the search frame after it was built
        :param name_plate: the container that holds pokemon name
        :param Frame: search frame widget
        :return: None
        """
        self.parent_search_frame = Frame
        self.ModalUpdate.set_name_plate(name_plate)

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

    def set_move_modal(self, move_modal):
        self.ModalUpdate.set_move_modal(move_modal)

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: Necessary arguments for the call back function
        :return: None
        """
        # Passed in by UIModals at class instantiation
        search_string = self.SearchUI.string_var.get()
        query_result = self.searchAlgorithm.build_search_list(search_string)
        self.SearchUI.build_result_frame(query_result)

    def search_button_callback(self, which_modal: str) -> None:
        self.SearchUI.build_search_result(self.parent_search_frame, which_modal)

    def move_callback(self, modal_name) -> None:
        """
        handles the move_frame modal
        :param modal_name: which modal to change
        :return: None
        """
        # Only update the button pressed
        self.ModalUpdate.update_moves(modal_name)

    def clicked_search_query(self, string: str, which_modal: str) -> None:
        """
        Detect when any of the search results are clicked
        :param which_modal: which modal is accessing this function
        :param string: name of the clicked result
        :return: None
        """
        if which_modal == "name_plate":
            self.ModalUpdate.update_name_plate(string)
            self.ModalUpdate.build_path_ref(string)
            # destroy result frame
            self.SearchUI.destroy_result_frame()

        self.current_window.root.focus_set()

    def clicked_item_modal(self, self_modal) -> None:
        """
        send click events for the item modal to the appropriate function
        :param self_modal: which modal was clicked
        :return: None
        """
        # open a new window and populate on a new thread, update using modalUpdate
        self.ModalUpdate.update_item_modal(self_modal)

    def clicked_ability_modal(self, self_modal) -> None:
        """
        send click event for the ability modal to the appropriate function
        :param self_modal: which modal was clicked
        :return: None
        """
        self.ModalUpdate.update_ability_modal(self_modal)

    def type_adv_change_window(self, new_window, button_config) -> None:
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
