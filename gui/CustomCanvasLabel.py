import customtkinter as ctk


class CustomCanvasLabel(ctk.CTkFrame):
    def __init__(self, master=None, text='', height=0, width=0, **kwargs):
        super().__init__(master, height, width, **kwargs)

        self.draw(height=height, width=width, text='')

    def draw(self, height=0, width=0, text=''):
        canvas = ctk.CTkCanvas(master=self, height=height, width=width)
        canvas.grid(column=0, row=0)

        canvas.create_text(__x=0, __y=0, text=text, angle=90)
