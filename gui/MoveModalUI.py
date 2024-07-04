import customtkinter as ctk


class MoveModal(ctk.CTkFrame):
    """
    This is a custom button for the MoveModalUI, it supers the CTkFrame class
    """
    def __init__(self, master, hover_color=None, **kwargs):
        self.move_name = None
        self.category = None
        self.pp = None
        self.type = None

        self.command = None
        self.num_width_elements = 2
        self.num_height_elements = 2
        self.hover_color = hover_color
        self.kwargs = kwargs

        super().__init__(master, **kwargs)

        self.create_frame()

    def configure_(self, command, **kwargs):
        self.command = command
        self.configure(**kwargs)

    def create_frame(self):
        def hover_enter():
            if self.hover_color is not None:
                self.configure(fg_color=self.hover_color)
            else:
                self.configure(fg_color=self.kwargs['fg_color'])
            self.configure(cursor='hand2')

        def hover_leave():
            self.configure(fg_color=self.kwargs['fg_color'])

        try:
            self.add_move_name()
            self.add_category()
            self.add_pp()
            self.add_type()

            for widget in self.winfo_children():
                # hover bind
                widget.bind('<Enter>', lambda _: hover_enter())
                widget.bind('<Leave>', lambda _: hover_leave())

                try:
                    widget.bind('<Button-1>', lambda _: self.command())
                except AttributeError:
                    print('no command found')

            self.bind('<Enter>', lambda _: hover_enter())
            self.bind('<Leave>', lambda _: hover_leave())

            try:
                self.bind('<Button-1>', lambda _: self.command())
            except AttributeError:
                print('no command found')

        except Exception as e:
            print('Error in MoveModal.py:', e)

    def add_move_name(self):
        self.move_name = ctk.CTkLabel(master=self,
                                      text="None",
                                      corner_radius=0,
                                      font=('Helvetica', 18, 'bold'),
                                      width=int(self.cget('width') / self.num_width_elements),
                                      height=int(self.cget('height') / self.num_height_elements))

        self.move_name.grid(row=0,
                            column=0,)

    def add_type(self):
        self.type = ctk.CTkLabel(master=self,
                                 text="Type: None",
                                 width=int(self.cget('width') / self.num_width_elements),
                                 height=int(self.cget('height') / self.num_height_elements))

        self.type.grid(row=1,
                       column=1,)

    def add_pp(self):
        self.pp = ctk.CTkLabel(master=self,
                               text="PP: 0",
                               width=int(self.cget('width') / self.num_width_elements),
                               height=int(self.cget('height') / self.num_height_elements))

        self.pp.grid(row=0,
                     column=1,)

    def add_category(self):
        self.category = ctk.CTkLabel(master=self,
                                     text='Category: None',
                                     width=int(self.cget('width') / self.num_width_elements),
                                     height=int(self.cget('height') / self.num_height_elements))

        self.category.grid(row=1,
                           column=0,)
