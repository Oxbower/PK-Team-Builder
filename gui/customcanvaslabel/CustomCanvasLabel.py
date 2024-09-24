import customtkinter as ctk

from typing import Callable


class CustomCanvasLabel(ctk.CTkFrame):
    """
    Supers the ctkFrame class with a canvas on top to allow
    for rotated labels to be drawn
    """
    def __init__(self, master=None, text='', fg_color='#fffff', height=0, width=0, **kwargs):
        """
        Initializes the CustomCanvas class
        :param master: parent for this class
        :param text: text to display
        :param fg_color: color of widget
        :param height: height of the widget
        :param width: width of the widget
        :param kwargs: other args for CTkFrame
        """
        super().__init__(master, height=height, width=width, fg_color=fg_color, **kwargs)
        self.grid_propagate(False)

        self.canvas = None
        self.canvas_text = None
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

        # Store the canvas text as attribute to configure
        self.canvas_text = canvas.create_text(width/2-2,
                                              height/2 - len(text)/2,
                                              text=text,
                                              fill='#ffffff',
                                              angle=90,
                                              font=('Helvetica', 13, 'bold'))
        self.canvas = canvas

    def bind(self, sequence: str = None, command: Callable = None, **kwargs):
        """
        Bind mouse event to this modal
        :param sequence: type of mouse event to bind
        :param command: callback method
        :param kwargs: other args for ctkFrame
        :return: None
        """
        if command is not None:
            super().bind(sequence=sequence, command=command, **kwargs)
            self.canvas.bind(sequence=sequence, func=command)

    def configure(self, text='', **kwargs):
        """
        Override the configure method of ctkFrame
        :param text: text to display
        :param kwargs: other args for ctkFrame
        :return: None
        """
        super().configure(**kwargs)

        if text != '':
            self.canvas.itemconfigure(self.canvas_text, text=text)
        else:
            self.canvas.configure(bg=kwargs['fg_color'])