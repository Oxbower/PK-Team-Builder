import customtkinter as ctk


class SearchUI:
    """
    Builds the UI for the search function
    """
    def __init__(self, mainWindow, modal_interact):
        """
        Initializes the searchUI class
        :param mainWindow: the ctk window instance
        :param modal_interact: the modal interact instance that called this class
        """

        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = ctk.CTkFrame
        self.modal_interact = modal_interact
        self.which_widget = None

        # keeps track of the variable in the name_plate
        self.string_var = self.ctk.StringVar()

        # set width of result container as an attribute
        self.frame_width = 0
        self.frame_height = 0

        self.search_result_container = None
        self.scrollable_frame = None

    def build_search_frame(self, parentFrame: ctk, which_modal: str, directory: str):
        """
        result_list: list[str]

                        parentFrame
        -----------------------------------------
        |       search_result_container         |
        |   ---------------------------------   |
        |   |        scrollable_frame       |   |
        |   |                               |   |
        |   |                               |   |
        |   |                               |   |
        |   ---------------------------------   |
        -----------------------------------------
        Builds search result
        :param parentFrame: parentFrame for this class so stat_frame
        :param which_modal: which modal is using the search bar
        :param directory: which directory to open
        :return: None
        """

        # destroy container frame to stop filling up heap
        if self.search_result_container is not None:
            self.search_result_container.destroy()

        self.which_widget = which_modal

        self.frame_width = parentFrame.width
        self.frame_height = parentFrame.height

        # Work around to destroy scrollable frame, it's a known issue on Github #2266
        self.search_result_container = self.Frame(master=parentFrame.root,
                                                  width=self.frame_width,
                                                  height=self.frame_height)
        # place the container in the stat frame at fixed location
        self.search_result_container.place(relx=0, rely=0)

        self.__build_search_bar(self.search_result_container, directory)
        # build result frame
        self.__build_scrollable_frame(self.search_result_container)

    def __build_search_bar(self, parentFrame, directory: str) -> None:
        """
        Builds the search bar inside the search result container frame
        :param parentFrame: container to put the search bar in
        :param directory: which directory to open
        :return: None
        """
        self.string_var = self.ctk.StringVar()
        self.string_var.trace('w', lambda *_,_dir=directory: self.modal_interact.search_bar_callback(*_,directory=_dir))

        name_plate = self.ctk.CTkEntry(master=parentFrame,
                                       textvariable=self.string_var,
                                       corner_radius=50,
                                       width=self.frame_width - 30,
                                       height=50,
                                       fg_color="#2e2e2e",
                                       border_width=0,
                                       justify='center',
                                       font=("Helvetica", 20, "bold"))
        name_plate.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky="nesw")

        name_plate.focus_set()

    def destroy_result_frame(self) -> None:
        """
        Destroys search_result_container after user has chosen a result
        :return: None
        """
        try:
            self.which_widget = None
            self.search_result_container.destroy()
            print("Destroying result frame...")
        except Exception as E:
            print(E)

    def __build_scrollable_frame(self, parentFrame: ctk.CTkFrame) -> None:
        """
        Build a result bar for given result string
        :param parentFrame: frame to build in
        :return: None
        """
        # destroy frame
        if self.scrollable_frame is not None:
            self.scrollable_frame.forget()

        # Build the scrollable frame
        self.scrollable_frame = self.ctk.CTkScrollableFrame(master=parentFrame,
                                                            fg_color="#3b3b3b",
                                                            width=self.frame_width - 20,
                                                            height=self.frame_height - 80,
                                                            corner_radius=0)

        # there's a bug with scrollable frames in CTK this just deals with it
        self.scrollable_frame._scrollbar.configure(height=0)
        self.scrollable_frame.grid(row=1,
                                   column=0)

    def build_result_frame(self, query_result: list[str]) -> None:
        """
        Populate the search list
        :param query_result: output of SearchingAlgorithm
        :return: None
        """

        # Make the string display look nicer
        for index, value in enumerate(query_result):
            name_capitalized = []
            for i in value.split(" "):
                name_capitalized.append(i.capitalize())
            query_result[index] = " ".join(name_capitalized)

        # Flush the items in the scrollable frame
        if self.scrollable_frame is not None:
            for value in self.scrollable_frame.winfo_children():
                value.destroy()

        # Insert query result into frame
        for index, value in enumerate(query_result):
            label = self.ctk.CTkButton(master=self.scrollable_frame,
                                       text=value,
                                       fg_color="#2b2b2b",
                                       hover_color="#353535",
                                       width=self.frame_width - 30,
                                       height=50,
                                       command=lambda string=value: self.modal_interact.clicked_search_query(string, self.which_widget),
                                       corner_radius=10)
            label.grid(row=index,
                       column=0,
                       pady=5,
                       padx=(10, 0),
                       sticky="ew")
