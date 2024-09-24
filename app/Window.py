import customtkinter as ctk
import os


class Window:

    def __init__(self, window_size: tuple[int, int]):
        """
        Initializes window class
        :param window_size: Argument for window size (window_width, window_height)
        :return: None
        """

        # window dimensions
        self.width = window_size[0]
        self.height = window_size[1]

        self.root = ctk.CTk()

    def create_window(self) -> ctk:
        """
        Create window object
        :return: the window object
        """

        # window theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # window title
        self.root.title("Pokemon Team-Builder")

        # min window Size
        self.root.minsize(width=self.width, height=self.height)

        self.root.iconbitmap(os.path.join("assets", "icon.ico"))

        # Disable Resize
        self.root.resizable(width=False, height=False)

        return self
