# front facing func

class Ui_MainWindow(object):
    def __init__(self, mainWindow, FrameObj):
        # Root Object
        self.root = mainWindow.root
        # Window Object
        self.mainWindow = mainWindow
        # customTkinter object
        self.ctk = self.mainWindow.ctk
        # frame object
        self.Frame = FrameObj

        # ui padding
        self.pad_y = 30
        self.pad_x = 50

        #button recolor
        self.color = '#222222'

        self.img_width = 256
        self.img_height = 256

    def setupUi(self):
        self.__build_gui()

    # function to call all gui building function
    def __build_gui(self):
        # Build
        self.__build_file_bar()

        # Build image frame
        img_frame = self.__build_img_frame()
        self.__name_stat_frame()
        self.__type_frame()

    # 'file' bar on top of app
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

    # Build frame for window
    def __build_img_frame(self):
        img_frame = self.Frame(master=self.root, height=self.img_height, width=self.img_width)
        img_frame.grid(row=1, column=0, pady=self.pad_y, padx=self.pad_x)

        label = self.ctk.CTkLabel(master=img_frame, text='Image File', height=self.img_height, width=self.img_width)
        label.pack()

        return img_frame

    def __name_stat_frame(self):
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height)
        frame.grid(row=1, column=1, sticky="n", pady=self.pad_y)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.__name_plate(frame)
        self.__stat_frame(frame)


    def __name_plate(self, parentFrame):
        name_plate = self.ctk.CTkButton(master=parentFrame, text="Name Plate", height=30, fg_color=self.color,
                                        corner_radius=0, font=('Arial Bold', 18))
        name_plate.grid(row=0, column=0, pady=5)


    def __stat_frame(self, parentFrame):
        stat = ['Base', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed']
        for i in range(1, 8):
            stat_frame = self.Frame(master=parentFrame, corner_radius=0, height=30)
            stat_frame.grid(row=i, column=0, sticky="se", pady=0)

            frame_1 = self.Frame(master=stat_frame, corner_radius=0, height=30)
            frame_1.grid(row=i, column=1, sticky="")

            stat_name = self.ctk.CTkLabel(master=frame_1, text=stat[int(i - 1)] + ": ")
            stat_name.grid()

            frame_2 = self.Frame(master=stat_frame, corner_radius=0, height=30, width=300, border_width=1)
            frame_2.grid(row=i, column=2, sticky="")

    def __type_frame(self):
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.5)
        frame.grid(row=1, column=2, sticky="e", pady=self.pad_y, padx=self.pad_x)

        frame.columnconfigure(0, weight=1)