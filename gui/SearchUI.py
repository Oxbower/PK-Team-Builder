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

        self.frame_width = 0

        self.search_result_container = None
        self.scrollable_frame = None

    def build_search_result(self, result_list: list[str], parentFrame):
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

        self.frame_width = parentFrame.winfo_width()

        # Work around to destroy scrollable frame, it's a known issue on Github #2266
        self.search_result_container = self.Frame(master=parentFrame, width=self.frame_width)
        # place the container in the stat frame at fixed location
        self.search_result_container.place(y=70, x=25)

        # build result frame
        self.__build_scrollable_frame(result_list, self.search_result_container)

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
                                                            width=self.frame_width - 70,
                                                            height=150,
                                                            corner_radius=0)

        # there's a bug with scrollable frames in CTK this just deals with it
        self.scrollable_frame._scrollbar.configure(height=0)
        self.scrollable_frame.pack()

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
                                       width=self.frame_width - 80,
                                       height=50,
                                       command=lambda string=value: self.modalInteract.clicked_search_query(string),
                                       corner_radius=10)
            label.grid(row=index,
                       column=0,
                       pady=5,
                       padx=(10, 0),
                       sticky="ew")
