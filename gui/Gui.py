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

        # hovver color
        self.hover_color = '#3f3f3f'

        # img width
        self.img_width = 230
        self.img_height = 230

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

        # build this pokemons type frame
        type_adv_frame = self.__build_type_adv_frame()

        '''
        Builds the modals using the parentFrames created by the build_[name]_frame methods
        '''

        # build modals for the file bar
        self.modals.build_file_modals(file_bar_frame)

        # build modal for the image
        self.modals.build_img_modal(image_frame)

        # build search bar inside the info_stat frame block
        self.modals.build_search_bar_modal(search_stat_frame)

        # build the 'stats' inside the info_stat frame
        self.modals.build_stat_modal(search_stat_frame)

        # build the move picker inside the move frame
        self.modals.build_move_modal(move_frame)

        # build the modal to show the variations of this pokemon (variations should still be searchable)
        self.modals.build_variation_modal(variation_frame)

        self.modals.build_type_modal(type_frame)

        self.modals.build_item_ability_modal(item_ability_frame)

        self.modals.build_type_adv_modal(type_adv_frame)

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
                               width=self.img_width,
                               corner_radius=self.rounded_corner)
        img_frame.grid(row=1,
                       column=0,
                       pady=(self.pad_y, 0),
                       padx=(self.pad_x, 0))

        return img_frame

    def __build_variation_frame(self):
        # variations frame
        extend_frame = self.Frame(master=self.root,
                                  height=self.img_height - 20,
                                  width=0,
                                  fg_color='#232323',
                                  corner_radius=0)

        extend_frame.place(x=self.img_width + self.pad_x,
                           y=self.pad_y * 2 + 10)

        return extend_frame

    def __build_type_frame(self):
        """
        the chosen pokemon's type
        :return: created frame
        """
        # type frame
        type_frame = self.Frame(master=self.root,
                                height=50,
                                width=self.img_width)

        type_frame.grid(row=2,
                        column=0,
                        padx=(self.pad_x, 0),
                        sticky="nsew")

        return type_frame

    def __build_moves_frame(self):
        """
        Build container for move modals
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           width=400)
        frame.grid(row=4,
                   column=2,
                   padx=(0, self.pad_x),
                   sticky="ne")

        return frame

    def __build_type_adv_frame(self):
        """
        This pokemons weakness and strengths
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           width=460,
                           height=300)
        frame.grid(row=4,
                   column=0,
                   padx=(self.pad_x, 0),
                   sticky='w',
                   columnspan=3)
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
                   sticky="ne",
                   pady=(self.pad_y, 0),
                   padx=(0, self.pad_x))

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
                           width=self.img_width + 50)
        frame.grid(row=3,
                   column=0,
                   columnspan=2,
                   pady=10,
                   padx=(self.pad_x, 0),
                   sticky="nw")

        return frame
