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


    def search(self, query_result):
        """
        calls the search method, tracks the query_result
        :param query_result: array containing all matched entries
        :return: null
        """
        # self.query_result = query_result
        # self.__build_result_frame()
        pass

    def __destroy_frame(self, widget):
        widget.destroy()

    def __build_result_frame(self, query_result, frame_width):
        """
        Build query output
        :return: null
        """

        #---Make the string display look nicer
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

    def search_box_result_modal(self, parentFrame):
        """
        builds result of search box
        :param parentFrame: __name_stat_frame parentFrame
        :return: None
        """
        # build result frame
        # pass result frame to searchHandler

    # def __update_stats(self, string):
    #     dict = self.app.update_stats(string)
    #
    #     # [0] = Base, [1] = Bar Graph, [2] = Min, [3] = Max
    #     #     "":           [0, 0, 0, 0],
    #     #     "HP":         [0, 0, 0, 0],
    #     #     "Attack":     [0, 0, 0, 0],
    #     #     "Defense":    [0, 0, 0, 0],
    #     #     "Sp. Atk":    [0, 0, 0, 0],
    #     #     "Sp. Def":    [0, 0, 0, 0],
    #     #     "Speed":      [0, 0, 0, 0]
    #
    #     self.frame_dict["HP"][0].configure(text=dict["hp"])
    #     self.frame_dict["Attack"][0].configure(text=dict["atk"])
    #     self.frame_dict["Defense"][0].configure(text=dict["def"])
    #     self.frame_dict["Sp. Atk"][0].configure(text=dict["sp_atk"])
    #     self.frame_dict["Sp. Def"][0].configure(text=dict["sp_def"])
    #     self.frame_dict["Speed"][0].configure(text=dict["speed"])
    #     self.frame_dict["Total"][0].configure(text=dict["base_total"])
