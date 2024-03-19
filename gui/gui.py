# front facing func

"""
    Builds the public facing interface
"""
class Ui_MainWindow(object):
    def __init__(self, mainWindow, FrameObj, app):
        # Root Object
        self.root = mainWindow.root
        # Window Object
        self.mainWindow = mainWindow
        # customTkinter object
        self.ctk = self.mainWindow.ctk
        # frame object
        self.Frame = FrameObj

        self.app = app

        # ui padding
        self.pad_y = 30
        self.pad_x = 50

        #button recolor
        self.color = '#222222'

        self.img_width = 256
        self.img_height = 256

        # variable string
        self.string_var = self.ctk.StringVar()

    '''
        public setup call
    '''
    def setupUi(self):
        self.__build_gui()

    # function to call all gui building function
    '''
        private call for inner funcs
    '''
    def __build_gui(self):
        # Build
        self.__build_file_bar()

        # Build image frame
        img_frame = self.__build_img_frame()
        self.__name_stat_frame()
        self.__type_frame()


    '''
        builds the 'file' bar
    '''
    def __build_file_bar(self):
        file_bar = self.Frame(master=self.root, width=self.mainWindow.width, corner_radius=0)
        file_bar.grid(row=0, sticky="nwes", columnspan=3)

        file_bar.columnconfigure(0, weight=0)
        file_bar.rowconfigure(0, weight=1)

        file = self.ctk.CTkButton(master=file_bar, text='File', width=50, command=self, corner_radius=0,
                                  fg_color=self.color, font=('Arial Bold', 15))
        file.grid(row=0)

        file = self.ctk.CTkButton(master=file_bar, text='Options', width=60, command=self, corner_radius=0,
                                  fg_color=self.color, font=('Arial Bold', 15))
        file.grid(row=0, column=1)

        # Add floating frame for options

    '''
        Build the img_frame for image container
    '''
    def __build_img_frame(self):
        img_frame = self.Frame(master=self.root, height=self.img_height, width=self.img_width)
        img_frame.grid(row=1, column=0, pady=self.pad_y, padx=self.pad_x)

        label = self.ctk.CTkLabel(master=img_frame, text='Image File', height=self.img_height, width=self.img_width)
        label.pack()

        return img_frame

    '''
        init call for name and stat block
    '''
    def __name_stat_frame(self):
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height)
        frame.grid(row=1, column=1, sticky="n", pady=self.pad_y)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.__name_plate(frame)
        self.__stat_frame(frame)

    '''
        builds the interactable name plate
    '''
    def __name_plate(self, parentFrame):
        self.string_var.trace('w', self.__call_back)

        # name_label = self.ctk.CTkLabel(master=parentFrame, text="Name:")
        # name_label.grid(row=0, column=0, sticky="e")

        name_plate = self.ctk.CTkEntry(master=parentFrame, textvariable=self.string_var, corner_radius=0,
                                       width=self.img_width, fg_color="#3b3b3b", border_width=0, justify='center')
        name_plate.grid(row=0, column=0, pady=5, sticky="wesn", padx=5)

    def __call_back(self, *args):
        self.app.search_string(self.string_var.get())

    '''
        builds the stat frame
    '''
    def __stat_frame(self, parentFrame):
        stat = ['Base', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed']
        for i in range(1, 8):
            stat_frame = self.Frame(master=parentFrame, corner_radius=0, height=30)
            stat_frame.grid(row=i, column=0, sticky="se", pady=0)

            frame_1 = self.Frame(master=stat_frame, corner_radius=0, height=30)
            frame_1.grid(row=i, column=1, sticky="")

            stat_name = self.ctk.CTkLabel(master=frame_1, text=stat[int(i - 1)] + ": ")
            stat_name.grid()

            frame_2 = self.Frame(master=stat_frame, corner_radius=0, height=30, width=300)
            frame_2.grid(row=i, column=2, sticky="")

    '''
        builds the type frame
    '''
    def __type_frame(self):
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.5)
        frame.grid(row=1, column=2, sticky="e", pady=self.pad_y, padx=self.pad_x)

        frame.columnconfigure(0, weight=1)