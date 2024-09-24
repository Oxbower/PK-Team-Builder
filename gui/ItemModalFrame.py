import os.path
import customtkinter as ctk

# imports items as dictionary tags with items as ctk labels
import app_io.LoadImageDictionary as ImageDictionary


class ItemModalFrame:
    """
    builds the frame to hold the items
    """
    def __init__(self, current_window):
        """
        Instantiates ItemModalFrame
        :param current_window: the ctk window instance
        """
        self.root = current_window.root
        self.active_modal = None
        self.active_frame = None

        self.items_image = ImageDictionary.LoadImageDictionary('assets',
                                                               'item-artwork',
                                                               (27, 27)).load_image()

    def start_search_build(self, modal):
        """
        public call for the search container
        :param current_name: pokemon name
        :param modal: the current modal
        :return: None
        """
        self.active_modal = modal

        self.__build_search_container()

    def __build_search_container(self):
        """
        builds the frame to hold the results, needed
        due to ctk.scrollableframe destroy() not working properly
        :return: None
        """
        # Don't destroy grid, remove for performance
        frame = ctk.CTkFrame(master=self.root)

        frame.place(relx=0.3, rely=0.1)

        self.active_frame = frame

        self.__build_search_scrollbar(frame)

    def __build_search_scrollbar(self, parentFrame):
        """
        builds the scrollable container called by build_search_container
        :param parentFrame: the frame created by build_search_container
        :return: None
        """
        frame = ctk.CTkScrollableFrame(master=parentFrame,
                                       corner_radius=0,
                                       width=300,
                                       height=400)

        frame.columnconfigure(0, weight=1)

        frame.grid(row=0, column=0, sticky='nesw')

        self.__insert_modals(frame)

    def __insert_modals(self, parentFrame):
        """
        inserts result blocks into the scrollable frame
        :param parentFrame: the frame created by build_search_scrollbar
        :return: None
        """
        item_name_list = list(self.items_image.keys())
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
        """
        when result selected, change the text displayed by the
        canvas label and destroy the frame_container holding the
        results
        :param text: text selected
        :return: None
        """
        self.active_modal.configure(text='',
                                    image=self.items_image[text])

        self.active_frame.destroy()