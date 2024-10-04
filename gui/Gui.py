import customtkinter as ctk
import gui.BuildWidget as widgets


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

        # widget class
        self.widgets = widgets.Widgets(self, self.current_window)

        # ui settings
        self.PAD_Y = 30
        self.PAD_X = 50
        self.ROUNDED_CORNER = 10
        # sys font
        self.DEFAULT_FONT = ("Arial Bold", 15)
        # hover color
        self.HOVER_COLOR = '#3f3f3f'
        # img width
        self.IMG_WIDTH = 230
        self.IMG_HEIGHT = 230

    def setup_ui(self):
        """
        Public facing setup call for gui
        :return: None
        """
        # call gui builder
        self._build_gui()

    def _build_gui(self):
        """
        Builds the frame to put stuff in
        :return: None
        """

        # Build top bar
        file_bar_frame = self._build_file_bar()
        # Build image frame
        image_frame = self._build_img_frame()
        # build search & stat frame
        search_stat_frame = self._build_info_frame()
        # build type frame
        type_frame = self._build_type_frame()
        # build moves frame
        move_frame = self._build_moves_frame()
        # build this pokemon type frame
        type_adv_frame = self._build_type_adv_frame()

        side_frame = self._build_side_img_frame()

        item_ability_frame = self._build_ability_item_bar()

        '''
        Builds the modals using the parentFrames created by the build_[name]_frame methods
        '''

        # build widgets for the file bar
        self.widgets.build_file_widget(file_bar_frame)
        # build widgets for the image
        self.widgets.build_img_widget(image_frame)
        # build the 'stats' inside the info_stat frame
        self.widgets.build_stat_widget(search_stat_frame)
        # build the items inside the type container i.e. pokedex-no and type display
        self.widgets.build_type_widget(type_frame)

        self.widgets.build_side_container(side_frame)
        # build search bar inside the info_stat frame block
        self.widgets.build_search_bar_widget(search_stat_frame)
        # build the move picker inside the move frame
        self.widgets.build_move_widget(move_frame)
        # build the picker for the pokemon's held item and their ability
        self.widgets.build_item_ability_widget(item_ability_frame)

        self.widgets.build_type_adv_widget(type_adv_frame)

    def _build_file_bar(self):
        """
        Builds the 'file' bar i.e. the strip on top with file, options, etc
        :return: created frame
        """

        # Builds frame for 'file' area
        file_bar = self.Frame(master=self.root,
                              width=self.current_window.width,
                              corner_radius=0,
                              fg_color='#2a2a2a')
        # position file_bar
        file_bar.grid(row=0,
                      sticky="nswe",
                      columnspan=4)

        return file_bar

    def _build_img_frame(self):
        """
        Build the img_frame for image container
        :return: created frame
        """

        img_frame = self.Frame(master=self.root,
                               height=self.IMG_HEIGHT,
                               width=self.IMG_WIDTH,
                               fg_color='#ffffff',
                               bg_color='#232323',
                               corner_radius=self.ROUNDED_CORNER)
        img_frame.grid(row=1,
                       column=0,
                       pady=(self.PAD_Y, 0),
                       padx=(self.PAD_X, 0))

        return img_frame

    def _build_side_img_frame(self):
        """
        Builds the frame that display battle transformations i.e mega evolutions and stuff
        :return: None
        """
        frame = self.Frame(master=self.root,
                           height=self.IMG_HEIGHT,
                           fg_color='#242424',
                           width=50)
        frame.grid(row=1,
                   column=1,
                   sticky='w',
                   pady=(self.PAD_Y, 0))

        inner_frame = self.Frame(master=frame,
                                 height=self.IMG_HEIGHT - 20,
                                 fg_color='#242424',
                                 width=50)
        inner_frame.place(anchor='ne', relx=1, rely=.1, relheight=.9)

        return inner_frame

    def _build_type_frame(self):
        """
        Builds the chosen pokemon's type
        :return: created frame
        """
        # type frame
        frame = self.Frame(master=self.root,
                           fg_color='#242424',
                           corner_radius=0,
                           width=self.IMG_WIDTH)

        frame.grid(row=2,
                   column=0,
                   padx=(self.PAD_X, 0),
                   sticky="nsew")

        frame.columnconfigure(0, weight=1)

        return frame

    def _build_moves_frame(self):
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
                   padx=(self.PAD_X, 0),
                   sticky="nw")

        return frame

    def _build_type_adv_frame(self):
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
                   padx=(0, self.PAD_X),
                   sticky='e')

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        return frame

    def _build_info_frame(self):
        """
        Builds the frame that will hold the stats and search bar
        :return: created frame
        """

        frame = self.Frame(master=self.root,
                           corner_radius=self.ROUNDED_CORNER,
                           height=500)
        frame.grid(row=1,
                   column=3,
                   rowspan=3,
                   sticky="ne",
                   pady=(self.PAD_Y, 0),
                   padx=(0, self.PAD_X))

        # allow stat block to overlap other rows and columns
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        return frame

    def _build_ability_item_bar(self):
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
                   pady=(self.PAD_Y, 0),
                   sticky='e')

        return frame
