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
        self.power = None
        self.accuracy = None

        self.command = None
        self.num_width_elements = 2
        self.num_height_elements = 3
        self.hover_color = hover_color
        self.kwargs = kwargs

        super().__init__(master, **kwargs)

        self.columnconfigure(1, weight=1)

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
            self.add_power()
            self.add_accuracy()

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
                            column=0)

    def add_type(self):
        self.type = ctk.CTkLabel(master=self,
                                 text=None,
                                 corner_radius=10,
                                 fg_color='#212121',
                                 width=int(self.cget('width') / self.num_width_elements) - 40,
                                 height=int(self.cget('height') / self.num_height_elements) - 2)

        self.type.grid(row=1,
                       column=1,
                       padx=(0, 2),
                       pady=(1, 1),
                       sticky='e')

    def add_pp(self):
        self.pp = ctk.CTkLabel(master=self,
                               text="PP: 0",
                               corner_radius=10,
                               fg_color='#777777',
                               width=int(self.cget('width') / self.num_width_elements) - 40,
                               height=int(self.cget('height') / self.num_height_elements) - 2)

        self.pp.grid(row=0,
                     column=1,
                     padx=(0, 2),
                     pady=(2, 1),
                     sticky='e')

    def add_category(self):
        self.category = ctk.CTkLabel(master=self,
                                     text='Category: None',
                                     fg_color='#454545',
                                     corner_radius=10,
                                     width=int(self.cget('width') / self.num_width_elements) - 40,
                                     height=int(self.cget('height') / self.num_height_elements) - 2)

        self.category.grid(row=2,
                           column=1,
                           padx=(0, 2),
                           pady=(1, 2),
                           sticky='e')

    def add_accuracy(self):
        self.accuracy = ctk.CTkLabel(master=self,
                                     font=('Helvetica', 13, 'bold'),
                                     text='Accuracy: 0')
        self.accuracy.grid(row=2,
                           column=0)

    def add_power(self):
        self.power = ctk.CTkLabel(master=self,
                                  font=('Helvetica', 13, 'bold'),
                                  text='Power: 0')
        self.power.grid(row=1,
                        column=0)
