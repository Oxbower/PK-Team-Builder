import os.path
import customtkinter as ctk

# imports items as dictionary tags with items as ctk labels
from app_io.LoadItemsAsImages import load_item_ctk_images as items_image


class ItemModalFrame:
    def __init__(self, current_window):
        self.root = current_window.root
        self.active_modal = None
        self.active_frame = None

    def start_search_build(self, current_name, modal):
        self.active_modal = modal

        self.build_search_container(current_name)

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

        self.insert_modals(frame, current_name)

    def insert_modals(self, parentFrame, current_name):

        item_name_list = list(items_image.keys())
        item_name_list.sort()

        for index, text in enumerate(item_name_list):
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
        self.active_modal.configure(text='',
                                    image=items_image[text])

        self.active_frame.destroy()