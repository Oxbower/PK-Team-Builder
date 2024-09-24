from typing import Callable

import customtkinter as ctk


class MoveModal(ctk.CTkFrame):
    """
    Creates a custom widget that displays moves information
    """

    def __init__(self, hover_color=None, **kwargs):
        """
        initialize the widget which supers the ctk.CTkFrame class
        :param hover_color: change the hover color of the widget
        :param kwargs: keyword arguements to pass to ctk.CTkFrame class
        """
        self.command = None

        self.num_width_elements = 2
        self.num_height_elements = 3
        self.hover_color = hover_color
        self.kwargs = kwargs

        super().__init__(**kwargs)

        self.__move_name = self.__add_move_name()
        self.__category = self.__add_category()
        self.__pp = self.__add_pp()
        self.__type = self.__add_type()
        self.__power = self.__add_power()
        self.__accuracy = self.__add_accuracy()

        self.columnconfigure(1, weight=1)
        self.__create_frame()

    def configure(self,
                  command: Callable = None,
                  move_name: str = '',
                  category: str = '',
                  pp: str = '',
                  type: tuple[str, ctk.CTkImage, str] = None,
                  power: str = '',
                  accuracy: str = '',
                  **kwargs):
        """
        Configure the MoveModal class
        :param command: what to open when this widget is clicked
        :param move_name: name of the move
        :param category: name of the category
        :param pp: base # of pp available for this move
        :param type: what type this move is
        :param power: power of the move, i.e., base dmg
        :param accuracy: accuracy of the move
        :param kwargs: keyword arguments to pass to ctk.CTkFrame class
        :return: None
        """
        if command is not None:
            self.command = command
        if move_name != '':
            self.__move_name.configure(text=move_name)
        if category != '':
            self.__category.configure(text=category)
        if pp != '':
            self.__pp.configure(text=pp)
        if type is not None:
            self.__type.configure(text=type[0], image=type[1], fg_color=type[2])
        if power != '':
            self.__power.configure(text=power)
        if accuracy != '':
            self.__accuracy.configure(text=accuracy)

        super().configure(**kwargs)

    @staticmethod
    def __hover_enter(widget):
        """
        change color of the widget on mouse enter
        :param widget: the widget to modify
        :return: None
        """
        if widget.hover_color is not None:
            widget.configure(fg_color=widget.hover_color)
        else:
            widget.configure(fg_color=widget.kwargs['fg_color'])
        widget.configure(cursor='hand2')

    @staticmethod
    def __hover_leave(widget):
        """
        change color of the widget on mouse leave
        :param widget: the widget to modify
        :return: None
        """
        widget.configure(fg_color=widget.kwargs['fg_color'])

    def __create_frame(self):
        """
        Create container frame for sub frames
        :return: None
        """
        # bind a hover event for all widget inside THIS frame
        for widget in self.winfo_children():
            # bind a hover and click event to the widgets
            widget.bind('<Enter>', lambda _: self.__hover_enter(self))
            widget.bind('<Leave>', lambda _: self.__hover_leave(self))
            widget.bind('<Button-1>', lambda _: self.command())

        # bind a hover and click event for the main frame
        self.bind('<Enter>', lambda _: self.__hover_enter(self))
        self.bind('<Leave>', lambda _: self.__hover_leave(self))
        self.bind('<Button-1>', lambda _: self.command())

    def __add_move_name(self) -> ctk.CTkLabel:
        """
        adds frame to hold label for move_name
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             text="None",
                             corner_radius=0,
                             font=('Helvetica', 18, 'bold'),
                             width=int(self.cget('width') / self.num_width_elements),
                             height=int(self.cget('height') / self.num_height_elements))

        label.grid(row=0,
                   column=0)

        return label

    def __add_type(self) -> ctk.CTkLabel:
        """
        adds frame to hold label for type
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             text=None,
                             corner_radius=10,
                             fg_color='#212121',
                             width=int(self.cget('width') / self.num_width_elements) - 40,
                             height=int(self.cget('height') / self.num_height_elements) - 2)

        label.grid(row=1,
                   column=1,
                   padx=(0, 2),
                   pady=(1, 1),
                   sticky='e')

        return label

    def __add_pp(self) -> ctk.CTkLabel:
        """
        adds container to hold label for pp
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             text="PP: 0",
                             corner_radius=10,
                             fg_color='#777777',
                             width=int(self.cget('width') / self.num_width_elements) - 40,
                             height=int(self.cget('height') / self.num_height_elements) - 2)

        label.grid(row=0,
                   column=1,
                   padx=(0, 2),
                   pady=(2, 1),
                   sticky='e')

        return label

    def __add_category(self) -> ctk.CTkLabel:
        """
        add container to hold label for category
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             text='None',
                             fg_color='#454545',
                             corner_radius=10,
                             width=int(self.cget('width') / self.num_width_elements) - 40,
                             height=int(self.cget('height') / self.num_height_elements) - 2)

        label.grid(row=2,
                   column=1,
                   padx=(0, 2),
                   pady=(1, 2),
                   sticky='e')

        return label

    def __add_accuracy(self) -> ctk.CTkLabel:
        """
        add container to hold label for accuracy
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             font=('Helvetica', 13, 'bold'),
                             text='Accuracy: 0')
        label.grid(row=2,
                   column=0)

        return label

    def __add_power(self) -> ctk.CTkLabel:
        """
        add container to hold label for power
        :return: the container created
        """
        label = ctk.CTkLabel(master=self,
                             font=('Helvetica', 13, 'bold'),
                             text='Power: 0')
        label.grid(row=1,
                   column=0)

        return label
