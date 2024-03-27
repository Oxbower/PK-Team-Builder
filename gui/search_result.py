import gui.gui


class SearchResult:
    def __init__(self, frame_obj, ctk, result_frame):
        self.query_result = None
        self.Frame = frame_obj
        self.ctk = ctk
        self.result_frame = result_frame

    def search(self, query_result):
        """
        calls the search method, tracks the query_result
        :param query_result: array containing all matched entries
        :return: null
        """
        self.query_result = query_result
        self.__build_result_frame()

    def __destroy_frame(self, widget):
        widget.destroy()

    def __build_result_frame(self):
        """
        Build query output
        :return: null
        """

        """
        TODO: Optimize search, (still) too slow
        """

        # Flush the Frame
        for i in self.result_frame.winfo_children():
            self.__destroy_frame(i)

        # Insert query result into frame
        # Slow as fuck
        for i in range(len(self.query_result)):
            frame_search = self.Frame(master=self.result_frame, width=self.result_frame.winfo_width(), corner_radius=0)
            frame_search.grid(row=i, column=0, padx=(10, 0), sticky="ew", pady=3)

            label = self.ctk.CTkLabel(master=frame_search,
                                      text=self.query_result[i],
                                      width=self.result_frame.winfo_width(),
                                      corner_radius=0)
            label.grid(row=i, column=0, sticky="ew")
