import customtkinter as ctk


class CustomCanvasLabel(ctk.CTkFrame):
    """
    Supers the ctkFrame class with a canvas on top to allow for rotated texts
    """
    def __init__(self, master=None, text='', fg_color='#fffff', height=0, width=0, **kwargs):
        super().__init__(master, height=height, width=width, fg_color=fg_color, **kwargs)
        self.grid_propagate(False)

        self.canvas = None
        self.draw(height=height, width=width, color=fg_color, text=text)

    def draw(self, height=0, width=0, color='#ffffff', text=''):
        """
        Draw the canvas and text
        :param height: height is based on the param given for the main frame
        :param width: width is based on the param given for the main frame
        :param color: color is based on param given for main frame
        :param text: text to display
        :return: None
        """
        canvas = ctk.CTkCanvas(master=self,
                               height=height-20,
                               width=width-5,
                               bd=0,
                               highlightthickness=0,
                               relief='ridge',
                               bg=color)
        canvas.grid(column=0, row=0, padx=2)

        canvas.create_text(width/2-2, height/2 - len(text)/2, text=text, angle=90)

        self.canvas = canvas

        self.bind_event(canvas)

    def bind_event(self, canvas):
        """
        Bind mouse events on this module
        :param canvas: parent canvas
        :return: None
        """
        self.bind("<Button-1>", lambda: self.click_event()) # bind to self
        self.canvas.bind("<Button-1>", lambda: self.click_event())

    def configure(self, text='', **kwargs):
        """
        Override the configure method of ctkFrame
        :param text:
        :param kwargs:
        :return:
        """
        self.configure(**kwargs)
        self.canvas.configure(text=text)

    def click_event(self):
        """
        Handles all click events for this modal
        :return:
        """
        print(f'ctk tag:{self.canvas}')

