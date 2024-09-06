import customtkinter as ctk
import sys
import app_io.LoadImageDictionary as ImageDictionary


from math import floor
from gui.TypeBackgroundColor import type_color
from interaction.TypeAdvantageHandler import find_neutral_types, find_defensive_type_multiplier, find_type_defense


class TypeAdvantageFrames:
    def __init__(self, parent_frame: ctk.CTkFrame = None):
        self.parent_frame = parent_frame
        self.Frame = ctk.CTkFrame
        self.max_width = 0
        self.max_height = 0

        self.types_defensive = [ctk.CTkFrame, ctk.CTkFrame, ctk.CTkFrame]
        self.types_offensive = [ctk.CTkFrame, ctk.CTkFrame]
        self.active_window = None

        self.type_image = ImageDictionary.LoadImageDictionary('assets',
                                                              'type-icon',
                                                              (30, 30)).load_image()

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
            # Destroy all inner widgets inside a frame
            for frame in self.types_defensive:
                for widget in frame.winfo_children():
                    widget.destroy()

            dict_tags = ['strengths', 'weaknesses', 'immunity']
            skip_value = find_neutral_types(data)  # types to exclude on display

            type_defense = find_type_defense([key['name'] for key in data])

            for tag_index, key in enumerate(dict_tags):
                set_list = set()

                for value in data:
                    set_list = set_list | set(value[key])
                sorted(set_list, reverse=True)

                if key != 'immunity':
                    set_list.difference_update(skip_value)

                for index, value in enumerate(set_list):
                    # container to hold image ang multiplier text
                    frame = self.Frame(master=self.types_defensive[tag_index],
                                       fg_color=type_color(value),
                                       height=40,
                                       width=int(self.types_defensive[0].cget('width') / 3))

                    frame.grid(row=floor(index/3) + 1,
                               column=index % 3,
                               sticky='w',
                               pady=(1, 2),
                               padx=.4)

                    frame.grid_propagate(False)

                    # damage multiplier text
                    multiplier_str, size = find_defensive_type_multiplier(type_defense, value)

                    multiplier = ctk.CTkLabel(master=frame,
                                              text=multiplier_str,
                                              text_color='black',
                                              fg_color='white',
                                              corner_radius=5,
                                              font=("Helvetica", size, "bold"),
                                              width=8,
                                              height=8)

                    multiplier.grid(row=0,
                                    column=1,
                                    padx=1)

                    # type image to display
                    image = ctk.CTkLabel(master=frame,
                                         text='',
                                         image=self.type_image[value.lower()])

                    image.grid(row=0,
                               column=0,
                               sticky='nsew',
                               pady=5)
