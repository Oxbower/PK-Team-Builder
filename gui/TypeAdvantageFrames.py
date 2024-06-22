import customtkinter as ctk
import sys

from math import floor
from app_io.LoadTypesAsImages import load_type_ctk_images as types_image
from gui.TypeBackgroundColor import type_color
from interaction.TypeAdvantageHandler import find_neutral_types
from collections import defaultdict


class TypeAdvantageFrames:
    def __init__(self, parent_frame: ctk.CTkFrame = None):
        self.parent_frame = parent_frame
        self.Frame = ctk.CTkFrame
        self.max_width = 0
        self.max_height = 0

        self.types_defensive = [0, 0, 0]
        self.types_offensive = [0, 0]
        self.active_window = None

    def set_parent_frame(self, parent_frame: ctk.CTkFrame, active_window: str, color: str = '#202020') -> None:
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
        label_frame_def = ['Resistant to', 'Weak to', 'Immune to']
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
                               fg_color="#1f1f1f")

            frame.grid(row=0,
                       column=index,
                       padx=3,
                       pady=5)
            frame.grid_propagate(False)
            frame.columnconfigure(0, weight=1)

            label = ctk.CTkLabel(master=frame,
                                 text=label_to_use[index],
                                 font=("Helvetica", 15, "bold"),
                                 fg_color='#1f1f1f',
                                 corner_radius=0,
                                 height=30,
                                 width=frame.cget('width'))
            label.grid(row=0, column=0, sticky='nsew')

            holder_type_frame = self.Frame(master=frame,
                                           corner_radius=0,
                                           fg_color='#2a2a2a',
                                           height=self.max_height - 20,
                                           width=frame.cget('width'))
            holder_type_frame.grid(row=1, column=0)

            holder_type_frame.grid_propagate(False)
            holder_type_frame.columnconfigure(1, weight=1)
            holder_type_frame.columnconfigure(2, weight=1)

            frame_to_use[index] = holder_type_frame

    def populate_frame(self, data):
        if self.active_window == 'Defensive':
            for i in self.types_defensive:
                for j in i.winfo_children():
                    j.destroy()

            dict_tags = ['strengths', 'weaknesses', 'immunity']
            skip_value = find_neutral_types(data)

            for index_d, tag_d in enumerate(dict_tags):
                set_list = []

                for value in data:
                    set_list += [i for i in value[tag_d]]
                set_list.sort(reverse=True)
                set_list = set(set_list)

                if index_d != 2:
                    for i in skip_value:
                        try:
                            set_list.remove(i)
                        except KeyError:
                            pass

                for index, value in enumerate(set_list):
                    frame = self.Frame(master=self.types_defensive[index_d],
                                       fg_color=type_color(value),
                                       height=40,
                                       width=int(self.types_defensive[0].cget('width') / 3) - 8)

                    frame.grid(row=floor(index/3) + 1,
                               column=index % 3,
                               sticky='w',
                               pady=2,
                               padx=4)

                    frame.grid_propagate(False)
                    frame.columnconfigure(0, weight=1)

                    image = ctk.CTkLabel(master=frame,
                                         text=None,
                                         image=types_image[value.lower()])

                    image.grid(row=0,
                               column=0,
                               sticky='nsew',
                               pady=5)
