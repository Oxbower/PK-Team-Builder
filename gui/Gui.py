import gui.UIModals as modals


class UI:
    """
        Builds the public facing interface
    """

    def __init__(self, mainWindow, FrameObj):
        """
        Initialize the UI
        :param mainWindow: window object
        :param FrameObj: ctkframe object
        :param app: app class
        """

        # Root Object
        self.root = mainWindow.root
        # Window Object
        self.mainWindow = mainWindow
        # customTkinter object
        self.ctk = self.mainWindow.ctk
        # frame object
        self.Frame = FrameObj

        # modal class
        self.modals = modals.UIModals(self, self.ctk, self.mainWindow, self.Frame)

        # ui settings
        self.pad_y = 30
        self.pad_x = 50
        self.flat_corner = 0
        self.rounded_corner = 10
        self.expand_all = "nswe"
        self.expand_vertical = "ns"
        self.expand_horizontal = "ew"

        # sys font
        self.font = ("Arial Bold", 15)

        # widget recolor
        self.light_grey = '#3b3b3b'
        self.dark_grey = '#2a2a2a'

        # img width
        self.img_width = 256
        self.img_height = 256

        self.name_stat_frame_height = 500
        self.stat_subcategory_height = 40

        self.image_disp = 0

    def setup_ui(self):
        """
        Public facing setup call for gui
        :return: None
        """

        # call gui builder
        self.__build_gui()

        # allow user to focus on all widgets
        #self.root.bind_all("<Button-1>", lambda event: event.widget.focus_set())  # redo later

    def __build_gui(self):
        """
        Builds the frame to put stuff in
        :return: None
        """

        # Build top bar
        file_bar_frame = self.__build_file_bar()

        # Build image frame
        image_frame = self.__build_img_frame()

        # build search & stat frame
        search_stat_frame = self.__build_info_frame()

        # build items and ability frame
        item_ability_frame = self.__item_ability_frame()

        # build variations frame
        variation_frame = self.__build_variation_frame()

        # build type frame
        type_frame = self.__build_type_frame()

        # build moves frame
        move_frame = self.__build_moves_frame()

        '''
        Builds the modals using the parentFrames created by the build_.*_frame methods
        '''
        self.modals.build_file_modals(file_bar_frame)

        self.modals.build_search_bar_modal(search_stat_frame)

        self.modals.build_stat_modal(search_stat_frame)

        self.modals.build_move_modal(move_frame)

    def __build_file_bar(self):
        """
        Builds the 'file' bar i.e. the strip on top with file, options, etc
        :return: None
        """

        # Builds frame for 'file' area
        file_bar = self.Frame(master=self.root,
                              width=self.mainWindow.width,
                              corner_radius=self.flat_corner,
                              fg_color=self.dark_grey)
        # position file_bar
        file_bar.grid(row=0,
                      sticky=self.expand_all,
                      columnspan=3)

        return file_bar

    def __build_img_frame(self):
        """
        Build the img_frame for image container
        :return: None
        """

        img_frame = self.Frame(master=self.root,
                               height=self.img_height,
                               width=self.img_width)
        img_frame.grid(row=1,
                       column=0,
                       pady=(self.pad_y, 0),
                       padx=(self.pad_x, 0))

        return img_frame

    def __build_variation_frame(self):
        # variations frame
        extend_frame = self.Frame(master=self.root,
                                  height=self.img_height,
                                  width=50,
                                  fg_color="red")
        extend_frame.grid(row=1,
                          column=1,
                          pady=(self.pad_y, 0),
                          padx=(0, self.pad_x),
                          sticky="w")

        return extend_frame

    def __build_type_frame(self):
        # type frame
        type_frame = self.Frame(master=self.root,
                                height=50,
                                width=self.img_width,
                                fg_color="blue")
        type_frame.grid(row=2,
                        column=0,
                        padx=(self.pad_x, 0),
                        sticky="n")

        return type_frame

    def __build_moves_frame(self):
        """
        Build container for move modals
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           width=400)
        frame.grid(row=4,
                   column=2)

        return frame

    def __build_type_adv_frame(self):
        frame = self.Frame(master=self.root)
        frame.grid(row=4,
                   column=1,
                   columnspan=2)
        return frame

    def __build_info_frame(self):
        """
        Builds the frame that will hold the stats and search bar
        :return: created frame
        """

        frame = self.Frame(master=self.root,
                           corner_radius=self.rounded_corner,
                           height=self.name_stat_frame_height,
                           )
        frame.grid(row=1,
                   column=2,
                   rowspan=3,
                   sticky="n",
                   pady=(self.pad_y, 0))

        # allow stat block to overlap other rows and columns
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        return frame

    def __item_ability_frame(self):
        """
        Builds the frame that will hold the ability and items
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           height=100,
                           width=self.img_width,
                           fg_color="pink")
        frame.grid(row=3,
                   column=0,
                   pady=self.pad_y,
                   padx=(self.pad_x, 0),
                   sticky="n")

        return frame
