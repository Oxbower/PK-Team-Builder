import sys
import customtkinter as ctk

from gui import Gui
from app.Window import Window


class App:
    def __init__(self):
        """
        Initialize the app with window_size=(width=1000, height=800)
        """
        self.width = 1000
        self.height = 800

        self.ctk = ctk

        # This is the window to draw stuff into initially None
        self.window = None

    def run(self):
        """
        Calls the window and setups the app
        :return: None
        """
        # initialize window
        new_window = Window(window_size=(self.width, self.height))
        self.window = new_window.create_window()

        # check if there is no window to draw stuff on
        if self.window is None:
            sys.exit("Could not create window, exiting now")

        # start drawing gui
        self.__build_gen_frame()

        # run window main loop
        self.window.root.mainloop()

    def __build_gen_frame(self):
        """
        Build general layout of window object
        :return: None
        """

        # configure grid system
        self.window.root.columnconfigure(1, weight=1)
        self.window.root.columnconfigure(0, weight=0)
        self.window.root.columnconfigure(2, weight=1)
        self.window.root.rowconfigure(1, weight=0)

        # initialize UI class
        __build_gui = Gui.UI(self.window)

        # build sys UI
        __build_gui.setup_ui()
