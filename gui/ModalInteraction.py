from tkinter import StringVar

import interaction.SearchResult as SearchResult
import gui.ModalUpdate as ModalUpdate

import time


class ModalInteraction:
    def __init__(self, stringVar, gui, ctk, mainWindow, Frame):
        # Updated String (need to keep track of)
        self.string_var = stringVar

        self.searchFrame = None

        self.mainWindow = mainWindow

        self.searchAlgorithm = SearchResult.SearchResult()
        self.modalUpdate = ModalUpdate.ModalUpdate(gui, ctk, mainWindow, Frame, self)

    def set_stats_widget(self, stats_widget):
        self.modalUpdate.set_stats_widget(stats_widget)

    def set_search_modal_frame(self, Frame):
        """
        Set search frame after it was built
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

    def set_variation_frame(self, Frame):
        """
        Sets the variation frame to be dynamic depending on how many variations a pokemon has
        :param Frame: the frame container
        :return: None
        """
        self.modalUpdate.set_variation_frame(Frame, self.set_string_var)

    def set_string_var(self, string):
        self.string_var.set(string)
        # destroy result frame
        self.modalUpdate.destroy_result_frame()

    def search_bar_callback(self, *args):
        """
        Handles search bar inputs to do string searches
        :param args: None
        :return: None
        """
        search_string = self.string_var.get()

        if search_string == "":
            print("Empty String")
            self.modalUpdate.destroy_result_frame()
        else:
            # build the list containing all matches of string
            search_string = self.searchAlgorithm.build_search_list(search_string)

            # pass in the list to build result frame from
            self.modalUpdate.build_search_result(search_string, self.searchFrame)

    def clicked_search_query(self, string):
        """
        Detect when any of the search results are clicked
        :param string: name of the clicked result
        :return: null
        """
        self.string_var.set(string)
        self.modalUpdate.build_path_ref(string)

        self.mainWindow.root.focus_set()
        # destroy result frame
        self.modalUpdate.destroy_result_frame()

    def clicked_variation_button(self, parentFrame, parentButton, image_ref):
        """
        Buttons in the sliding frame to change which variation is active
        :param parentFrame: parent frame of the variation button
        :param parentButton: parent button of the variation button
        :param image_ref: reference for the arrow image for the button to open the variation menu
        :return: None
        """
        self.mainWindow.root.focus_set()

        self.modalUpdate.build_dynamic_variation_button(parentFrame, parentButton, image_ref)
