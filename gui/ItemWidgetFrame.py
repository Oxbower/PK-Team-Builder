import os.path
import customtkinter as ctk

# imports items as dictionary tags with items as ctk labels
import app_io.LoadImageDictionary as ImageDictionary


class ItemModalFrame:
    """
    builds the frame to hold the items
    """
    def __init__(self):
        """
        Instantiates ItemModalFrame
        """
        self.items_image = ImageDictionary.LoadImageDictionary('assets',
                                                               'item-artwork',
                                                               (27, 27)).load_image()

    def active_modal_callback(self, widget: ctk.CTkButton, item: str) -> None:
        """
        when result selected, change the text displayed by the
        canvas label and destroy the frame_container holding the
        results
        :param widget: the widget to modify
        :param item: item name
        :return: None
        """
        widget.configure(text='', image=self.items_image[item])
