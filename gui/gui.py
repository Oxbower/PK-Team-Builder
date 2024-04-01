import interaction.read_f as read_file
import gui.search_result as search_result
import interaction.keyHandler

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

        self.flat_corner = 0

        # button recolor
        self.color = '#222222'

        self.img_width = 256
        self.img_height = 256

        self.name_stat_frame_height = 500
        self.stat_subcategory_height = 40

        # variable string
        self.string_var = self.ctk.StringVar()

        self.image_disp = 0

        self.font = ("Arial Bold", 15)

        self.expand_all = "nswe"

    def setup_ui(self):
        """
        public setup call
        """
        self.__build_gui()
        self.root.bind_all("<Button-1>", lambda event: event.widget.focus_set())

    def __build_gui(self):
        """
        private call for inner funcs
        """
        # Build
        self.__build_file_bar()

        # Build image frame
        self.img_frame = self.__build_img_frame()
        self.__name_stat_frame()
        self.__subframe()
        #self.__type_frame()

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

    def __update_stats(self, string):
        dict = self.app.update_stats(string)

        # self.frame_dict = {
        #     "":           [0, 0, 0, 0],
        #     "HP":         [0, 0, 0, 0],
        #     "Attack":     [0, 0, 0, 0],
        #     "Defense":    [0, 0, 0, 0],
        #     "Sp. Atk":    [0, 0, 0, 0],
        #     "Sp. Def":    [0, 0, 0, 0],
        #     "Speed":      [0, 0, 0, 0]
        # }

        self.frame_dict["HP"][0].configure(text=dict["hp"])
        self.frame_dict["Attack"][0].configure(text=dict["atk"])
        self.frame_dict["Defense"][0].configure(text=dict["def"])
        self.frame_dict["Sp. Atk"][0].configure(text=dict["sp_atk"])
        self.frame_dict["Sp. Def"][0].configure(text=dict["sp_def"])
        self.frame_dict["Speed"][0].configure(text=dict["speed"])
        self.frame_dict["Total"][0].configure(text=dict["base_total"])

    def __display_img(self):
        """
        display collected img
        :return: null
        """
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
            return True
        return False

    def __build_img_frame(self):
        """
        Build the img_frame for image container
        """
        img_frame = self.Frame(master=self.root, height=self.img_height, width=self.img_width)
        img_frame.grid(row=1, column=0, pady=(self.pad_y,0), padx=(self.pad_x, 0))

        # label = self.ctk.CTkLabel(master=img_frame, text='Image File', height=self.img_height, width=self.img_width)
        # label.pack()

        #red frame
        extend_frame = self.Frame(master=self.root, height=self.img_height, width=50, fg_color="red")
        extend_frame.grid(row=1, column=1, pady=(self.pad_y, 0), padx=(0, self.pad_x), sticky="w")

        #blue frame
        type_frame = self.Frame(master=self.root, height=50, width=self.img_width, fg_color="blue")
        type_frame.grid(row=2, column=0, padx=(self.pad_x, 0), sticky="n")

        return img_frame

    def __subframe(self):
        frame = self.Frame(master=self.root, height=100, width=self.img_width, fg_color="pink")
        frame.grid(row=3, column=0, pady=self.pad_y, padx=(self.pad_x, 0), sticky="n")

    def __name_stat_frame(self):
        """
        init call for name and stat block
        """
        frame = self.Frame(master=self.root, corner_radius=15, height=self.name_stat_frame_height)
        frame.grid(row=1, column=2, rowspan=3, sticky="n", pady=(self.pad_y, 0))

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.__search_bar(frame)
        self.__stat_frame(frame)

    def __search_bar(self, parent_frame):
        """
        builds search bar
        """

        # name_label = self.ctk.CTkLabel(master=parentFrame, text="Name:")
        # name_label.grid(row=0, column=0, sticky="e")

        name_plate = self.ctk.CTkEntry(master=parent_frame, textvariable=self.string_var,
                                       corner_radius=0, width=self.img_width,
                                       height=40, fg_color="#3b3b3b",
                                       border_width=0, justify='center')
        name_plate.grid(row=0, column=0, sticky=self.expand_all)

        self.string_var.trace('w', self.__call_back)

        # bind focus to name_plate
        name_plate.bind("<FocusIn>", lambda event: self.__focus(name_plate, parent_frame, True))
        name_plate.bind("<FocusOut>", lambda event: self.__focus(name_plate, parent_frame, False))

    def __focus(self, _widget, parentFrame, isFocused):
        if isFocused:
            self.__search_frame(parent_frame=parentFrame, inst="build")
        else:
            self.__search_frame(parent_frame=parentFrame, inst="destroy")

    def __search_frame(self, parent_frame, inst):
        """
        builds result of search box
        :param parent_frame: __name_stat_frame parentFrame
        :return: null
        """
        if inst == "build":
            # build result frame
            # pass result frame to searchHandler
            self.result = self.ctk.CTkScrollableFrame(master=parent_frame,
                                                      fg_color="#3b3b3b",
                                                      width=parent_frame.winfo_width() - 25,
                                                      height=150)
            self.result._scrollbar.configure(height=0)
            self.result.place(y=50)
            self.searchHandler = search_result.SearchResult(self.Frame, self.ctk, self.result)
        else:
            self.result.place_forget()

    def __call_back(self, var, index, mode):
        # Remove focus add to selector
        # self.root.focus_set()

        # build result bar
        #self.__focus(name_plate, parent_frame, True)

        # grep all strings w/ same substring
        self.query_result = self.app.search_string(self.string_var.get())

        # handle search
        self.searchHandler.search(query_result=self.query_result)

        # for testing
        # var = self.__display_img()
        # if var:
        #     self.__update_stats(self.query_result[0])

    def __stat_frame(self, parentFrame):
        """
        builds the stat frame
        """

        '''
        Base, Graph, Min, Max
        '''
        self.frame_dict = {
            "":         [0, 0, 0, 0],
            "HP":       [0, 0, 0, 0],
            "Attack":   [0, 0, 0, 0],
            "Defense":  [0, 0, 0, 0],
            "Sp. Atk":  [0, 0, 0, 0],
            "Sp. Def":  [0, 0, 0, 0],
            "Speed":    [0, 0, 0, 0],
            "Total":    [0, 0, 0, 0]
        }
        key_list = ["", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]
        label = ["Base", "", "Min", "Max"]

        # Build Row
        for i in range(1, 9):
            key = int(i - 1)
            # Builds outer frame
            stat_frame = self.Frame(master=parentFrame, corner_radius=self.flat_corner, height=self.stat_subcategory_height)
            stat_frame.grid(row=i, column=0, sticky="se", padx=10)

            # build inner frame_1 col 0
            frame_1 = self.Frame(master=stat_frame, corner_radius=0, height=self.stat_subcategory_height)
            frame_1.grid(row=i, column=1, sticky=self.expand_all)

            stat_name = self.ctk.CTkLabel(master=frame_1, text=key_list[key] + " ", font=self.font)
            stat_name.grid(sticky=self.expand_all)

            # Base Num
            base_frame = self.Frame(master=stat_frame, corner_radius=self.flat_corner, height=self.stat_subcategory_height)
            base_frame.grid(row=i, column=2, sticky=self.expand_all)

            base_num = self.ctk.CTkLabel(master=base_frame, text="", width=50, font=self.font)
            base_num.grid(sticky=self.expand_all)

            self.frame_dict[key_list[key]][0] = base_num

            # Build inner frame_2 col 1
            bar_frame = self.Frame(master=stat_frame, corner_radius=self.flat_corner, height=self.stat_subcategory_height, width=300)
            bar_frame.grid(row=i, column=3, sticky="")

            self.frame_dict[key_list[key]][1] = bar_frame

            # Min Num
            min_frame = self.Frame(master=stat_frame, corner_radius=self.flat_corner, height=self.stat_subcategory_height)
            min_frame.grid(row=i, column=4, sticky=self.expand_all)

            min_num = self.ctk.CTkLabel(master=min_frame, text="", width=50, font=self.font)
            min_num.grid(sticky=self.expand_all, padx=5)

            self.frame_dict[key_list[key]][2] = min_num

            # Max Num
            max_frame = self.Frame(master=stat_frame, corner_radius=self.flat_corner, height=self.stat_subcategory_height)
            max_frame.grid(row=i, column=5, sticky=self.expand_all)

            max_num = self.ctk.CTkLabel(master=max_frame, text="", width=50, font=self.font)
            max_num.grid(sticky=self.expand_all, padx=5)

            self.frame_dict[key_list[key]][3] = max_num

        # Build column Labels
        for i in range(len(label)):
            if i != 1:
                self.frame_dict[""][i].configure(text=label[i])

    def __type_frame(self):
        """
        builds the type frame
        """
        frame = self.Frame(master=self.root, corner_radius=0, height=self.img_height, width=self.img_width * 1.5)
        frame.grid(row=1, column=2, sticky="e", pady=self.pad_y, padx=self.pad_x)

        frame.columnconfigure(0, weight=1)
