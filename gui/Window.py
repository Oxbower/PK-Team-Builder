from gui import Gui
from gui import UIModals


class Window:
    """
    Initialize window
    """
    def __init__(self, ctk, os, app):
        # window dimensions
        self.width = 1200
        self.height = 800

        # ctk object
        self.root = ctk.CTk()
        self.ctk = ctk
        self.Frame = ctk.CTkFrame
        self.os = os
        self.app = app

    def create_window(self):
        """
        Create window object
        :return: null
        """

        # window theme
        self.ctk.set_appearance_mode("dark")
        self.ctk.set_default_color_theme("dark-blue")

        # window title
        self.root.title("PKMN Team Builder")

        # min window Size
        self.root.minsize(width=self.width, height=self.height)

        self.root.iconbitmap(self.os.path.join("assets", "icon.ico"))

        # Disable Resize
        self.root.resizable(width=False, height=False)

        # init for window UI
        self.build_gen_frame()

    # Calls all functions to build the window
    def build_gen_frame(self):
        """
        Build general layout of window object
        :return: null
        """

        # configure grid system
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=0)

        # init UI class
        build_gui = Gui.UI(self, self.Frame)

        # build sys UI
        build_gui.setup_ui()
