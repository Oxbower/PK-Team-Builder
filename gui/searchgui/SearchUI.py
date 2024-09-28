import customtkinter as ctk


class SearchUI:
    """
    Builds the UI for the search function
    """
    def __init__(self, mainWindow, modalInteract):
        """
        Initializes the searchUI class
        :param mainWindow: the ctk window instance
        :param modalInteract: the modal interact instance that called this class
        """

        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = ctk.CTkFrame
        self.modalInteract = modalInteract

        # set width of result container as an attribute
        self.frame_width = 0
        self.frame_height = 0

        self.search_result_container = None
        self.scrollable_frame = None

    def build_search_result(self, result_list: list[str], parentFrame: ctk):
        """
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
        :param result_list: list to build search result for
        :param parentFrame: parentFrame for this class so stat_frame
        :return: None
        """

        # destroy container frame to stop filling up heap
        if self.search_result_container is not None:
            self.search_result_container.destroy()

        self.frame_width = parentFrame.width
        self.frame_height = parentFrame.height

        # TODO: create a search bar on top of this

        # Work around to destroy scrollable frame, it's a known issue on Github #2266
        self.search_result_container = self.Frame(master=parentFrame.root,
                                                  width=self.frame_width,
                                                  height=self.frame_height)
        # place the container in the stat frame at fixed location
        self.search_result_container.place(relx=0, rely=0.05)

        self.build_search_bar(self.search_result_container)
        # build result frame
        self.__build_scrollable_frame(result_list, self.search_result_container)

    def build_search_bar(self, parentFrame) -> None:
        """
        Builds the search bar inside the search result container frame
        :param parentFrame: container to put the search bar in
        :return: None
        """
        string_var = self.ctk.StringVar()

        name_plate = self.ctk.CTkEntry(master=parentFrame,
                                       textvariable=string_var,
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

    def destroy_result_frame(self):
        """
        Destroys search_result_container after user has chosen a result
        :return: None
        """
        try:
            self.search_result_container.destroy()
            print("Destroying result frame...")
        except Exception as E:
            print(E)

    def __build_scrollable_frame(self, query_result, parentFrame):
        """
        Build a result bar for given result string
        :param parentFrame: frame to build in
        :param query_result: list containing strings to put into search bar
        :return: None
        """
        # destroy frame
        if self.scrollable_frame is not None:
            self.scrollable_frame.destroy()

        # Build the scrollable frame
        self.scrollable_frame = self.ctk.CTkScrollableFrame(master=parentFrame,
                                                            fg_color="#3b3b3b",
                                                            width=self.frame_width - 20,
                                                            height=self.frame_height - 130,
                                                            corner_radius=0)

        # there's a bug with scrollable frames in CTK this just deals with it
        self.scrollable_frame._scrollbar.configure(height=0)
        self.scrollable_frame.grid(row=1,
                                   column=0)

        self.__build_result_frame(query_result)

    def __build_result_frame(self, query_result):
        """
        Build query output
        :param query_result: output of SearchingAlgorithm
        :return: None
        """

        # Make the string display look nicer
        for index, value in enumerate(query_result):
            capitalized = value.title()
            query_result[index] = capitalized

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
                                       command=lambda string=value: self.modalInteract.clicked_search_query(string),
                                       corner_radius=10)
            label.grid(row=index,
                       column=0,
                       pady=5,
                       padx=(10, 0),
                       sticky="ew")
