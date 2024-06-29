import os.path
import json
import customtkinter as ctk

from app_io.LoadJson import json_load


class MoveModalFrame():
    # build the search modal frame
    def __init__(self, current_window):
        self.root=current_window.root
        self.active_window=False

    def start_search_build(self, modal, folder_dir):
        path = os.path.join('pokemon-pokedex', folder_dir, 'moves.json')

        try:
            data = json_load(path)
            print(json.dumps(data, indent=4))
        except FileNotFoundError as e:
            print(e)
            return None

        self.build_search_container()

    def build_search_container(self):
        # Don't destroy, grid remove for perfrmance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.build_search_scrollbar(frame)

    def build_search_scrollbar(self, parentFrame):
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                     corner_radius=0,
                                     width=300,
                                     height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.insert_modals(frame)

    def insert_modals(self, parentFrame):
        frame = ctk.CTkFrame(master=parentFrame,
                             width=250,
                             height=50)

        frame.grid(row=0,
                   column=0,
                   padx=5,
                   pady=2,
                   sticky='nesw')
