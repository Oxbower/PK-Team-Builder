import os.path
import customtkinter as ctk
import gui.customcanvaslabel.CustomCanvasLabel as CustomCanvasLabel

from app_io.LoadJson import json_load


class CanvasLabelUpdate:
    # build the search modal frame
    def __init__(self, current_window: ctk):
        """
        initialize the canvas label update class, call
        this to update the canvas label
        :param current_window: ctk root instance
        """
        self.root = current_window.root
        self.all_moves = json_load(os.path.join('data', 'abilities.json'))
        self.active_modal = None

        self.data = None
        self.active_frame = None

    def start_search_build(self, modal: CustomCanvasLabel, dir_folder_name: str, current_name: str):
        """
        public call for the search container
        :param modal: modal to update
        :param dir_folder_name: folder name of this pokemon to grap abilities from
        :param current_name: pokemon name
        :return: None
        """
        if current_name is None:
            return None

        path = os.path.join('pokemon-pokedex', dir_folder_name, f'{current_name}.json')

        try:
            self.data = json_load(path)
            self.data = self.data['abilities']
        except FileNotFoundError as e:
            print(e)
            return None

        self.active_modal = modal

        self.build_search_container()

    def build_search_container(self):
        """

        :return:
        """
        # Don't destroy, grid remove for performance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.active_frame = frame

        self.build_search_scrollbar(frame)

    def build_search_scrollbar(self, parentFrame):
        """

        :param parentFrame:
        :return:
        """
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                       corner_radius=0,
                                       width=300,
                                       height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.insert_modals(frame)

    def insert_modals(self, parentFrame):
        """

        :param parentFrame:
        :return:
        """
        for index, text in enumerate(list(self.data.values())):
            frame = ctk.CTkButton(master=parentFrame,
                                  text=text,
                                  fg_color='#333333',
                                  width=250,
                                  height=50,
                                  command=lambda _text=text: self.active_modal_callback(_text))

            frame.grid(row=index,
                       column=0,
                       padx=5,
                       pady=5,
                       sticky='nesw')

    def active_modal_callback(self, text):
        """

        :param text:
        :return:
        """
        # Change active modal text
        self.active_modal.configure(text)

        self.active_frame.destroy()
