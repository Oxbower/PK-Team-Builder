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
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.3)
        frame.grid(row=1, column=1, sticky="n", pady=self.pad_y)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.__name_plate(frame)
        self.__stat_plate(frame)

    def __name_plate(self, parentFrame):
        name_plate = self.ctk.CTkButton(master=parentFrame, text="Name Plate", fg_color=self.color,
                                        corner_radius=0, font=('Arial Bold', 18))
        name_plate.grid(row=0, column=0, sticky="n", pady=5)

    def __stat_plate(self, parentFrame):
        base = self.ctk.CTkLabel(master=parentFrame, height=20, text='Base', font=('Arial Bold', 15))
        hp = self.ctk.CTkLabel(master=parentFrame, height=20, text='HP', font=('Arial Bold', 15))
        atk = self.ctk.CTkLabel(master=parentFrame, height=20, text='Attack', font=('Arial Bold', 15))
        defense = self.ctk.CTkLabel(master=parentFrame, height=20, text='Defense', font=('Arial Bold', 15))
        sp_atk = self.ctk.CTkLabel(master=parentFrame, height=20, text='Special Attack', font=('Arial Bold', 15))
        sp_def = self.ctk.CTkLabel(master=parentFrame, height=20, text='Special Defense', font=('Arial Bold', 15))
        speed = self.ctk.CTkLabel(master=parentFrame, height=20, text='Speed', font=('Arial Bold', 15))

        base.grid(row=1, column=0, sticky="w", pady=5)
        hp.grid(row=2, column=0, sticky="w", pady=5)
        atk.grid(row=3, column=0, sticky="w", pady=5)
        defense.grid(row=4, column=0, sticky="w", pady=5)
        sp_atk.grid(row=5, column=0, sticky="w", pady=5)
        sp_def.grid(row=6, column=0, sticky="w", pady=5)
        speed.grid(row=7, column=0, sticky="w", pady=5)

    def __type_frame(self):
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.5)
        frame.grid(row=1, column=2, sticky="e", pady=self.pad_y, padx=self.pad_x)

        frame.columnconfigure(0, weight=1)