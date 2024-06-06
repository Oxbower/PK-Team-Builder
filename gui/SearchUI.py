class SearchUI:
    def __init__(self, gui, ctk, mainWindow, Frame, modalInteract):
        self.gui = gui
        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = Frame
        self.modalInteract = modalInteract

        self.result_frame = None

    def build_frame(self, query_result, parentFrame, frame_width):
        """
        Build a result bar for given result string
        :param frame_width: width of parentFrame
        :param parentFrame: frame to build in
        :param query_result: list containing strings to put into search bar
        :return: None
        """
        # destroy frame
        if self.result_frame is not None:
            self.result_frame.destroy()

        # Build the scrollable frame
        self.result_frame = self.ctk.CTkScrollableFrame(master=parentFrame,
                                                        fg_color="#3b3b3b",
                                                        width=frame_width - 70,
                                                        height=150,
                                                        corner_radius=self.gui.flat_corner)

        # there's a bug with scrollable frames in CTK this just deals with it
        self.result_frame._scrollbar.configure(height=0)
        self.result_frame.pack()

        #self.searchHandler = SearchR.SearchResult(self.Frame, self.ctk, self.result)
        self.__build_result_frame(query_result, frame_width)

    def __destroy_frame(self, widget):
        widget.destroy()

    def __build_result_frame(self, query_result, frame_width):
        """
        Build query output
        :return: null
        """

        # Make the string display look nicer
        for index, value in enumerate(query_result):
            capitalized = value.title()
            query_result[index] = capitalized

        # Flush the Frame
        if self.result_frame is not None:
            for value in self.result_frame.winfo_children():
                self.__destroy_frame(value)

        # Insert query result into frame
        for index, value in enumerate(query_result):
            label = self.ctk.CTkButton(master=self.result_frame,
                                       text=value,
                                       fg_color="#2b2b2b",
                                       hover_color="#353535",
                                       width=frame_width-80,
                                       height=50,
                                       command=lambda string=value: self.modalInteract.clicked_search_query(string),
                                       corner_radius=self.gui.rounded_corner)
            label.grid(row=index,
                       column=0,
                       pady=5,
                       padx=(10, 0),
                       sticky="ew")
