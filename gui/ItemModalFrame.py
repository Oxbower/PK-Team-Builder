import os.path
import customtkinter as ctk

from app_io.LoadJson import json_load


class ItemModalFrame:
    def __init__(self, current_window):
        self.root = current_window.root
        self.items = json_load()

    def start_search_build(self, modal, dir_folder_name, current_name):
        path = os.path.join('pokemon-pokedex', dir_folder_name, 'moves.json')

        try:
            self.data = json_load(path)
            # print(json.dumps(self.data, indent=4))
        except FileNotFoundError as e:
            print(e)
            return None

        self.active_modal = modal

        self.build_search_container(current_name)

    def build_search_container(self, current_name):
        # Don't destroy, grid remove for performance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.active_frame = frame

        self.build_search_scrollbar(frame, current_name)

    def build_search_scrollbar(self, parentFrame, current_name):
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                       corner_radius=0,
                                       width=300,
                                       height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.insert_modals(frame, current_name)



