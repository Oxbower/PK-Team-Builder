from gui import gui


class Window:
    def __init__(self, ctk, FrameObj, os, app):
        self.width = 1200
        self.height = 800
        self.root = ctk.CTk()
        self.ctk = ctk
        self.Frame = FrameObj
        self.os = os
        self.app = app

    def create_window(self):
        self.ctk.set_appearance_mode("dark")
        self.ctk.set_default_color_theme("dark-blue")

        # window title
        self.root.title("PKMN Team Builder")

        # min window Size
        self.root.minsize(width=self.width, height=self.height)

        self.root.iconbitmap(self.os.path.join("assets", "icon.ico"))

        # Disable Resize
        self.root.resizable(width=False, height=False)

        # Build main frame for window
        self.build_gen_frame()

    # Calls all functions to build the window
    def build_gen_frame(self):
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)

        build_gui = gui.UI(self, self.Frame, self.app)
        build_gui.setup_ui()
