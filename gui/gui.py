import interaction.read_f as read_file

"""
    Builds the public facing interface
"""


class UI:
    def __init__(self, mainWindow, FrameObj, app):
        # Root Object
        self.contains_img = False
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

        # button recolor
        self.color = '#222222'

        self.img_width = 256
        self.img_height = 256

        # variable string
        self.string_var = self.ctk.StringVar()

        self.image_disp = 0

    def setup_ui(self):
        """
        public setup call
        """
        self.__build_gui()

    def __build_gui(self):
        """
        private call for inner funcs
        """
        # Build
        self.__build_file_bar()

        # Build image frame
        self.img_frame = self.__build_img_frame()
        self.__name_stat_frame()
        self.__type_frame()

    def __build_file_bar(self):
        """
        builds the 'file' bar
        """
        file_bar = self.Frame(master=self.root, width=self.mainWindow.width, corner_radius=0)
        file_bar.grid(row=0, sticky="nwes", columnspan=3)

        file_bar.columnconfigure(0, weight=0)
        file_bar.rowconfigure(0, weight=1)

        file = self.ctk.CTkButton(master=file_bar, text='File', width=50, corner_radius=0,
                                  fg_color=self.color, font=('Arial Bold', 15))
        file.grid(row=0)

        file = self.ctk.CTkButton(master=file_bar, text='Options', width=60, corner_radius=0,
                                  fg_color=self.color, font=('Arial Bold', 15))
        file.grid(row=0, column=1)

        # Add floating frame for options

    def __img_label_build(self, img_container):
        return self.ctk.CTkLabel(self.img_frame, image=img_container, text=None)

    def __display_img(self):
        if len(self.query_result) == 1:
            print("Found Image")
            pkdex_id = self.app.get_id(str(self.query_result[0]))

            img = read_file.build_img_ref(pkdex_id)
            image_container = self.ctk.CTkImage(light_image=img, size=(256, 256))

            if self.contains_img != True:
                self.image_disp = self.__img_label_build(image_container)
                self.contains_img = True
            else:
                self.image_disp.configure(image=image_container)

            self.image_disp.pack()
            return

    def __build_img_frame(self):
        """
        Build the img_frame for image container
        """
        img_frame = self.Frame(master=self.root, height=self.img_height, width=self.img_width)
        img_frame.grid(row=1, column=0, pady=self.pad_y, padx=self.pad_x)

        # label = self.ctk.CTkLabel(master=img_frame, text='Image File', height=self.img_height, width=self.img_width)
        # label.pack()

        return img_frame

    def __name_stat_frame(self):
        """
        init call for name and stat block
        """
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height)
        frame.grid(row=1, column=1, sticky="ns", pady=self.pad_y)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.__name_plate(frame)
        self.__stat_frame(frame)

    def __name_plate(self, parentFrame):
        """
        builds the interactive name plate
        """
        self.string_var.trace('w', self.__call_back)

        # name_label = self.ctk.CTkLabel(master=parentFrame, text="Name:")
        # name_label.grid(row=0, column=0, sticky="e")

        name_plate = self.ctk.CTkEntry(master=parentFrame, textvariable=self.string_var, corner_radius=10,
                                       width=self.img_width, fg_color="#3b3b3b", border_width=0, justify='center')
        name_plate.grid(row=0, column=0, pady=5, sticky="wens")

    def __call_back(self, *args):
        self.query_result = self.app.search_string(self.string_var.get())
        print(self.query_result)


        self.__display_img()

    def __stat_frame(self, parentFrame):
        """
        builds the stat frame
        """
        stat = ['Base', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        for i in range(1, 8):
            # builds outer frame
            stat_frame = self.Frame(master=parentFrame, corner_radius=0, height=30)
            stat_frame.grid(row=i, column=0, sticky="se", padx=10)

            # build inner frame_1 col 0
            frame_1 = self.Frame(master=stat_frame, corner_radius=0, height=30)
            frame_1.grid(row=i, column=1, sticky="ns")

            stat_name = self.ctk.CTkLabel(master=frame_1, text=stat[int(i - 1)] + ": ", font=('Arial Bold', 14))
            stat_name.grid()

            # build inner frame_2 col 1
            frame_2 = self.Frame(master=stat_frame, corner_radius=0, height=30, width=300)
            frame_2.grid(row=i, column=2, sticky="")

    def __type_frame(self):
        """
        builds the type frame
        """
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.5)
        frame.grid(row=1, column=2, sticky="e", pady=self.pad_y, padx=self.pad_x)

        frame.columnconfigure(0, weight=1)
