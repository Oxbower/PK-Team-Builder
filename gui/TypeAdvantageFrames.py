import customtkinter as ctk
import app_io.LoadImage as LoadImage
import os
import sys

from math import floor
from app_io.LoadImage import load_type_ctk_images as types_image

class TypeAdvantageFrames:
    def __init__(self, parent_frame: ctk.CTkFrame = None):
        self.parent_frame = parent_frame
        self.Frame = ctk.CTkFrame
        self.max_width = 0
        self.max_height = 0

        self.types_defensive = [0, 0, 0]
        self.types_offensive = [0, 0]
        self.active_window = None

    def set_parent_frame(self, parent_frame: ctk.CTkFrame, active_window: str, color: str = '#242424') -> None:
        if parent_frame is None:
            sys.exit('Error creating window frame')

        self.max_height = parent_frame.cget("height")
        self.max_width = parent_frame.cget("width")

        self.parent_frame = self.Frame(master=parent_frame,
                                       fg_color=color)

        self.active_window = active_window

        self.build_widget(self.parent_frame)

    def get_window(self) -> ctk.CTkFrame:
        if self.parent_frame is None:
            sys.exit('Error creating window frame')

        return self.parent_frame

    def get_types_container(self) -> (ctk.CTkFrame, ctk.CTkFrame):
        return self.types_offensive, self.types_defensive

    def build_widget(self, parent: ctk.CTkFrame):
        label_frame_def = ['Strength', 'Weakness', 'Immunity']
        label_frame_off = ['Types covered', 'Types not covered']

        if self.active_window == 'Defensive':
            frame_to_use = self.types_defensive
            label_to_use = label_frame_def
        else:
            frame_to_use = self.types_offensive
            label_to_use = label_frame_off

        for index, value in enumerate(frame_to_use):

            frame = self.Frame(master=parent,
                               height=self.max_height - 50,
                               corner_radius=0,
                               width=int(self.max_width / len(frame_to_use)) - 10,
                               fg_color="#2a2a2a")

            frame.grid(row=1,
                       column=index,
                       padx=5,
                       pady=5)
            frame.grid_propagate(False)

            frame_to_use[index] = frame

            label = ctk.CTkLabel(master=frame,
                                 text=label_to_use[index],
                                 font=("Helvetica", 15, "bold"),
                                 corner_radius=0,
                                 height=30,
                                 width=frame.cget('width'))
            label.grid(row=0, column=0, columnspan=2, sticky='nsew')

    def populate_frame(self, data):
        if self.active_window == 'Defensive':
            for i in self.types_defensive:
                for j in i.winfo_children():
                    j.destroy()

            set_list = []
            for value in data:
                set_list += [i for i in value['strengths']]
            set_list = set(set_list)

            for index, value in enumerate(set_list):
                image = ctk.CTkLabel(master=self.types_defensive[0],
                                     text=None,
                                     image=types_image[value.lower()],
                                     height=30,
                                     width=30)
                image.grid(row=floor(index/2) + 1, column=index % 2, sticky='nsew', pady=5)

            set_list = []
            for value in data:
                set_list += [i for i in value['weaknesses']]
            set_list = set(set_list)
