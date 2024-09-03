import os.path
import customtkinter as ctk

from app_io.LoadItemsAsImages import load_item_ctk_images as items_image


class ItemModalFrame:
    def __init__(self, current_window):
        self.root = current_window.root

    def start_search_build(self):
        print('inside itemModalFrame')
        #self.build_search_container()

    def build_search_container(self, current_name):
        # Don't destroy grid, remove for performance
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

        self.insert_modals(frame)



