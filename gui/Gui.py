import customtkinter as ctk
import gui.UIModals as modals


class UI:
    """
    Builds the containers for the widgets to make up the UI
    """

    def __init__(self, current_window):
        """
        Initialize the UI, sets default attributes for
        the UI
        :param current_window: window object
        """

        # Root Object
        self.root = current_window.root
        # Window Object
        self.current_window = current_window
        # customTkinter object
        self.ctk = ctk
        # frame object
        self.Frame = ctk.CTkFrame

        # modal class
        self.modals = modals.UIModals(self, self.current_window)

        # ui settings
        self.pad_y = 30
        self.pad_x = 50
        self.flat_corner = 0
        self.rounded_corner = 10
        self.expand_all = "nswe"

        # sys font
        self.font = ("Arial Bold", 15)

        # widget recolor
        self.light_grey = '#3b3b3b'
        self.dark_grey = '#2a2a2a'

        # hover color
        self.hover_color = '#3f3f3f'

        # img width
        self.img_width = 230
        self.img_height = 230

        self.name_stat_frame_height = 500
        self.stat_subcategory_height = 40

    def setup_ui(self):
        """
        Public facing setup call for gui
        :return: None
        """

        # call gui builder
        self.__build_gui()

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

        # build type frame
        type_frame = self.__build_type_frame()

        # build moves frame
        move_frame = self.__build_moves_frame()

        # build this pokemon type frame
        type_adv_frame = self.__build_type_adv_frame()

        side_frame = self.__build_side_img_frame()

        item_ability_frame = self.__build_ability_item_bar()

        '''
        Builds the modals using the parentFrames created by the build_[name]_frame methods
        '''

        # build modals for the file bar
        self.modals.build_file_modals(file_bar_frame)

        # build modal for the image
        self.modals.build_img_modal(image_frame)

        # build the 'stats' inside the info_stat frame
        self.modals.build_stat_modal(search_stat_frame)

        # build the items inside the type container i.e. pokedex-no and type display
        self.modals.build_type_modal(type_frame)

        self.modals.build_side_container(side_frame)

        # build search bar inside the info_stat frame block
        self.modals.build_search_bar_modal(search_stat_frame)

        # build the move picker inside the move frame
        self.modals.build_move_modal(move_frame)

        # build the picker for the pokemon's held item and their ability
        self.modals.build_item_ability_modal(item_ability_frame)

        self.modals.build_type_adv_modal(type_adv_frame)

    def __build_file_bar(self):
        """
        Builds the 'file' bar i.e. the strip on top with file, options, etc
        :return: created frame
        """

        # Builds frame for 'file' area
        file_bar = self.Frame(master=self.root,
                              width=self.current_window.width,
                              corner_radius=self.flat_corner,
                              fg_color=self.dark_grey)
        # position file_bar
        file_bar.grid(row=0,
                      sticky=self.expand_all,
                      columnspan=4)

        return file_bar

    def __build_img_frame(self):
        """
        Build the img_frame for image container
        :return: created frame
        """

        img_frame = self.Frame(master=self.root,
                               height=self.img_height,
                               width=self.img_width,
                               fg_color='#ffffff',
                               bg_color='#232323',
                               corner_radius=self.rounded_corner)
        img_frame.grid(row=1,
                       column=0,
                       pady=(self.pad_y, 0),
                       padx=(self.pad_x, 0))

        return img_frame

    def __build_side_img_frame(self):
        """
        Builds the frame that display battle transformations i.e mega evolutions and stuff
        :return: None
        """
        frame = self.Frame(master=self.root,
                           height=self.img_height,
                           fg_color='#242424',
                           width=50)
        frame.grid(row=1,
                   column=1,
                   sticky='w',
                   pady=(self.pad_y, 0))

        inner_frame = self.Frame(master=frame,
                                 height=self.img_height-20,
                                 fg_color='#242424',
                                 width=50)
        inner_frame.place(anchor='ne', relx=1, rely=.1, relheight=.9)

        return inner_frame

    def __build_type_frame(self):
        """
        Builds the chosen pokemon's type
        :return: created frame
        """
        # type frame
        frame = self.Frame(master=self.root,
                           fg_color='#242424',
                           corner_radius=0,
                           width=self.img_width)

        frame.grid(row=2,
                   column=0,
                   padx=(self.pad_x, 0),
                   sticky="nsew")

        frame.columnconfigure(0, weight=1)

        return frame

    def __build_moves_frame(self):
        """
        Builds the frame for move modals
        :return: created frame
        """

        frame = self.Frame(master=self.root,
                           height=405,
                           width=340)
        frame.grid(row=3,
                   column=0,
                   rowspan=3,
                   columnspan=3,
                   pady=(5, 0),
                   padx=(self.pad_x, 0),
                   sticky="nw")

        return frame

    def __build_type_adv_frame(self):
        """
        Builds the frame for a pokemon weakness and strengths
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           width=530,
                           height=300,
                           fg_color='#242424')
        frame.grid(row=4,
                   column=3,
                   pady=10,
                   padx=(0, self.pad_x),
                   sticky='e')

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

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
                   column=3,
                   rowspan=3,
                   sticky="ne",
                   pady=(self.pad_y, 0),
                   padx=(0, self.pad_x))

        # allow stat block to overlap other rows and columns
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        return frame

    def __build_ability_item_bar(self):
        """
        builds a container to hold the ability and items
        :return: created frame
        """
        frame = self.Frame(master=self.root,
                           fg_color='#242424',
                           height=350,
                           width=50)

        frame.grid(row=1,
                   rowspan=3,
                   column=2,
                   pady=(self.pad_y, 0),
                   sticky='e')

        return frame
