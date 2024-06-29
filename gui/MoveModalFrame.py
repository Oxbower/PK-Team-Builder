import os.path
import json
import customtkinter as ctk

from app_io.LoadJson import json_load


class MoveModalFrame():
    # build the search modal frame
    def __init__(self, current_window):
        self.root = current_window.root
        self.active_window = False
        self.active_modal = None

        self.data = None

    def start_search_build(self, modal, dir_folder_name, current_name):
        path = os.path.join('pokemon-pokedex', dir_folder_name, 'moves.json')

        try:
            self.data = json_load(path)
            print(json.dumps(self.data, indent=4))
        except FileNotFoundError as e:
            print(e)
            return None

        self.active_modal = modal

        self.build_search_container(current_name)

    def build_search_container(self, current_name):
        # Don't destroy, grid remove for performance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.build_search_scrollbar(frame, current_name)

    def build_search_scrollbar(self, parentFrame, current_name):
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                     corner_radius=0,
                                     width=300,
                                     height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.insert_modals(frame, current_name)

    def insert_modals(self, parentFrame, current_name):
        if current_name in self.data:
            new_data = self.data[current_name]
        else:
            new_data = []

        # Turn into set to remove redundancy
        new_container = set(self.data['non-specific'] + new_data)

        for index, text in enumerate(new_container):
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
        # Change active modal text
        self.active_modal.configure(text=text)
