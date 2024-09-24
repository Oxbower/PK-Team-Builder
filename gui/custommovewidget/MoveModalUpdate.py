import os.path

from PIL import Image
import customtkinter as ctk

from app_io.LoadJson import json_load
from gui.TypeBackgroundColor import type_color
from gui.custommovewidget import MoveModal as MoveModal
import app_io.LoadImageDictionary as ImageDicitonary


class MoveModalUpdate:
    """
    Updates the contents of the custom move widget
    to accurately reflect the choices made by user
    """
    def __init__(self, current_window: ctk):
        """
        intializes the move modal update class
        :param current_window: ctk root instance
        """
        self.root = current_window.root
        self.all_moves = json_load(os.path.join('data', 'moves.json'))
        self.active_modal = None
        self.blank_image = ctk.CTkImage(light_image=Image.new("RGBA", (40,40)), size=(30,30))

        self.data = None
        self.active_frame = None

        self.types_image = ImageDicitonary.LoadImageDictionary('assets',
                                                               'type-icon',
                                                               (30, 30)).load_image()

    # use SearchingAlgo class

    def start_search_build(self, modal: MoveModal, dir_folder_name: str, current_name: str):
        """
        public call for the search container
        :param modal: modal to update
        :param dir_folder_name: folder name of this pokemon to grap abilities from
        :param current_name: pokemon name
        :return: None
        """
        path = os.path.join('pokemon-pokedex', dir_folder_name, 'moves.json')

        try:
            self.data = json_load(path)
            # print(json.dumps(self.data, indent=4))
        except FileNotFoundError as e:
            print(e)
            return None

        self.active_modal = modal

        self.__build_search_container(current_name)

    def __build_search_container(self, current_name):
        """
        builds the frame to hold the results, needed
        due to ctk.scrollableframe destroy() not working properly
        :param current_name: name of the current pokemon displayed
        :return: None
        """
        # Don't destroy, grid remove for performance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.active_frame = frame

        self.__build_search_scrollbar(frame, current_name)

    def __build_search_scrollbar(self, parentFrame, current_name):
        """
        builds the scrollable container called by build_search_container
        :param parentFrame: the frame created by build_search_container
        :param current_name: name of current pokemon displayed
        :return: None
        """
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                       corner_radius=0,
                                       width=300,
                                       height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.__insert_modals(frame, current_name)

    def __insert_modals(self, parentFrame, current_name):
        """
        inserts result blocks into the scrollable frame
        :param parentFrame: the frame created by build_search_scrollbar
        :param current_name: name of current pokemon displayed
        :return: None
        """
        if current_name in self.data:
            new_data = self.data[current_name]
        else:
            new_data = []

        # Turn into set to remove redundancy
        new_container = set(self.data['non-specific'] + new_data)

        new_container = sorted(new_container)

        for index, text in enumerate(new_container):
            frame = ctk.CTkButton(master=parentFrame,
                                  text=text,
                                  fg_color='#333333',
                                  width=250,
                                  height=50,
                                  command=lambda _text=text: self.__active_modal_callback(_text))

            frame.grid(row=index,
                       column=0,
                       padx=5,
                       pady=5,
                       sticky='nesw')

    def __active_modal_callback(self, text):
        """
        when result selected, change the text displayed by the
        canvas label and destroy the frame_container holding the
        results
        :param text: text selected
        :return: None
        """
        # Change active modal text
        self.active_modal.configure(move_name=text)

        for value in self.all_moves:
            if value['name'] == text:
                self.active_modal.configure(pp=str('PP: ' + value['pp']))
                self.active_modal.configure(category=value['cat'].title())
                self.active_modal.configure(type=('',
                                                  self.types_image[value['type'].lower()],
                                                  type_color(value['type'])))
                self.active_modal.configure(accuracy=str('Accuracy: ' + value['acc']))
                self.active_modal.configure(power=str('Power: ' + value['power']))

        self.active_frame.destroy()

    def reset_modal(self, modals):
        """
        resets the modal back to base when pokemon changed
        :param modals: the parent container of the modals
        :return: None
        """
        for widget in modals:
            widget.configure(move_name='None')
            widget.configure(pp=str('PP: 0'))
            widget.configure(category='None')
            widget.configure(type=('', self.blank_image, '#212121'))
            widget.configure(accuracy=str('Accuracy: 0'))
            widget.configure(power=str('Power: 0'))
