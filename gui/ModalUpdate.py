class ModalUpdate:
    def __init__(self):
        pass

    def search_result_frame(self, parentFrame):
        """
        Builds search bar
        """
        # build entry widget

    def search_box_result_modal(self, parentFrame):
        """
        builds result of search box
        :param parentFrame: __name_stat_frame parentFrame
        :return: None
        """
        # build result frame
        # pass result frame to searchHandler
        result = self.ctk.CTkScrollableFrame(master=parentFrame,
                                             fg_color="#3b3b3b",
                                             width=parentFrame.winfo_width() - 25,
                                             height=150, corner_radius=0)
        result._scrollbar.configure(height=0)
        result.place(y=50, x=5)
        self.searchHandler = SearchR.SearchResult(self.Frame, self.ctk, self.result)

    def __update_stats(self, string):
        dict = self.app.update_stats(string)

        # [0] = Base, [1] = Bar Graph, [2] = Min, [3] = Max
        #     "":           [0, 0, 0, 0],
        #     "HP":         [0, 0, 0, 0],
        #     "Attack":     [0, 0, 0, 0],
        #     "Defense":    [0, 0, 0, 0],
        #     "Sp. Atk":    [0, 0, 0, 0],
        #     "Sp. Def":    [0, 0, 0, 0],
        #     "Speed":      [0, 0, 0, 0]

        self.frame_dict["HP"][0].configure(text=dict["hp"])
        self.frame_dict["Attack"][0].configure(text=dict["atk"])
        self.frame_dict["Defense"][0].configure(text=dict["def"])
        self.frame_dict["Sp. Atk"][0].configure(text=dict["sp_atk"])
        self.frame_dict["Sp. Def"][0].configure(text=dict["sp_def"])
        self.frame_dict["Speed"][0].configure(text=dict["speed"])
        self.frame_dict["Total"][0].configure(text=dict["base_total"])

    def __display_img(self):
        """
        display collected img
        :return: null
        """
        if len(self.query_result) == 1:
            print("Found Image")
            pkdex_id = self.app.get_id(str(self.query_result[0]))

            img = read_file.build_img_ref(pkdex_id)
            image_container = self.ctk.CTkImage(light_image=img, size=(256, 256))

            if self.contains_img != True:
                self.image_disp = self.__img_label_build(image_container)
                self.contains_img = True
            else:
                self.image_disp.configure(image=image_container)

            self.image_disp.pack()
            return True
        return False

    def __img_label_build(self, img_container):
        return self.ctk.CTkLabel(self.img_frame, image=img_container, text=None)

    def __focus(self, _widget, parentFrame, isFocused):
        if isFocused:
            self.gui.search_result_frame(parent_frame=parentFrame, inst="build")
        else:
            self.gui.search_result_frame(parent_frame=parentFrame, inst="destroy")