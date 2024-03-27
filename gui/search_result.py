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

    def __build_result_frame(self):
        """
        Build query output
        :return:
        """

        """
        TODO: Flush the result area
        """

        for i in range(len(self.query_result)):
            frame_search = self.Frame(master=self.result_frame)
            frame_search.grid(row=i, column=0, sticky="n")

            label = self.ctk.CTkLabel(frame_search, text=self.query_result[i])
            label.grid(row=i, column=0)