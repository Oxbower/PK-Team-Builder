import customtkinter as ctk
import sys


class TypeAdvantageFrames:
    def __init__(self, parent_frame: ctk.CTkFrame = None):
        self.parent_frame = parent_frame
        self.Frame = ctk.CTkFrame
        self.max_width = 0
        self.max_height = 0

        self.types_adv = [0, 0]

    def set_parent_frame(self, parent_frame: ctk.CTkFrame, color: str = '#242424') -> None:
        if parent_frame is None:
            sys.exit('Error creating window frame')

        self.max_height = parent_frame.cget("height")
        self.max_width = parent_frame.cget("width")

        self.parent_frame = self.Frame(master=parent_frame,
                                       fg_color=color)

        self.build_widget(self.parent_frame)

    def get_window(self) -> ctk.CTkFrame:
        if self.parent_frame is None:
            sys.exit('Error creating window frame')

        return self.parent_frame

    def build_widget(self, parent: ctk.CTkFrame):
        # get the dimensions of this parent frame

        for index, value in enumerate(self.types_adv):
            frame = self.Frame(master=parent,
                               height=self.max_height - 50,
                               width=int(self.max_width / 2) - 10,
                               fg_color="#2a2a2a")

            frame.grid(row=1,
                       column=index,
                       padx=5,
                       pady=5)

            self.types_adv[index] = frame