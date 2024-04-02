import gui.ModalInteraction as ModalInteraction


class UIModals:
    def __init__(self, gui, ctk, mainWindow, Frame):
        """
        Initialize UI modals this is the stuff inside the
        frames.
        """

        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = Frame
        self.gui = gui

        self.string_var = self.ctk.StringVar()
        self.modal_interact = ModalInteraction.ModalInteraction(self.string_var)

        '''
        Holds modal references for update
        
        [0] = Base, [1] = Graph, [2] = Min, [3] = Max
        '''
        self.stats_widget = {
            "":         [0, 0, 0, 0],
            "HP":       [0, 0, 0, 0],
            "Attack":   [0, 0, 0, 0],
            "Defense":  [0, 0, 0, 0],
            "Sp. Atk":  [0, 0, 0, 0],
            "Sp. Def":  [0, 0, 0, 0],
            "Speed":    [0, 0, 0, 0],
            "Total":    [0, 0, 0, 0]
        }

    def build_file_modals(self, parentFrame):
        """
        Build file modals
        :return: None
        """

        modals = ['File', 'Options']

        # build buttons for file bar
        for i in range(len(modals)):
            file = self.ctk.CTkButton(master=parentFrame,
                                      text=modals[i],
                                      width=50,
                                      corner_radius=0,
                                      fg_color=self.gui.dark_grey,
                                      font=self.gui.font)
            file.grid(row=0, column=i)

    def build_search_bar_modal(self, parentFrame):
        """
        Build the search bar modal
        :param parentFrame:
        :return: None
        """
        name_plate = self.ctk.CTkEntry(master=parentFrame,
                                       textvariable=self.string_var,
                                       corner_radius=0,
                                       width=self.gui.img_width,
                                       height=50,
                                       fg_color=self.gui.light_grey,
                                       border_width=0,
                                       justify='center',
                                       font=("Helvetica", 20, "bold"))

        name_plate.grid(row=0, column=0, sticky=self.gui.expand_all)

        self.string_var.trace('w', self.modal_interact.search_bar_callback)

        # bind focus to name_plate
        #name_plate.bind("<FocusIn>", lambda event: self.__focus(name_plate, parentFrame, True))
        #name_plate.bind("<FocusOut>", lambda event: self.__focus(name_plate, parentFrame, False))

    def build_stat_modal(self, parentFrame):
        """
        Builds the stats frame up
        :param parentFrame: master frame of the stats modals
        :return: None
        """
        row_label = ["", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]
        column_label = ["Base", "", "Min", "Max"]

        # Build Row
        for row in range(1, 9):  # hard-coded range(), update if they add new stats
            row_key = int(row - 1)
            # Builds outer frame to hold the stuff that will get updated frequently
            stat_frame = self.Frame(master=parentFrame,
                                    corner_radius=self.gui.flat_corner,
                                    height=self.gui.stat_subcategory_height)
            stat_frame.grid(row=row, column=0, sticky="se", padx=10)

            # Build Col
            for col in range(5):
                width = 50

                if col == 2:
                    width = 300

                # Creates the inner frame to hold the actual numbers and bar graph
                frame = self.Frame(master=stat_frame,
                                   corner_radius=self.gui.flat_corner,
                                   height=self.gui.stat_subcategory_height,
                                   width=width,
                                   # border_width=2,
                                   # border_color="#ff0000"
                                   )
                frame.grid(row=row, column=col, sticky=self.gui.expand_all)

                if col != 2:
                    label = self.ctk.CTkLabel(master=frame,
                                              corner_radius=self.gui.flat_corner,
                                              height=self.gui.stat_subcategory_height,
                                              width=width,
                                              text="0",
                                              font=self.gui.font)
                    label.grid(sticky=self.gui.expand_all)

                if col == 0:
                    label.configure(text=row_label[row - 1])
                elif col == 2:
                    # store frame for updates into stats_modal
                    self.stats_widget[row_label[row_key]][col - 1] = frame
                else:
                    # store label for updates into stats_modal
                    self.stats_widget[row_label[row_key]][col - 1] = label

        # Build column Labels
        for col in range(len(column_label)):
            if col != 1:
                self.stats_widget[""][col].configure(text=column_label[col])

        # test = [1,2,3,4,5,6,7]
        #
        # for i in range(1,8):
        #     self.stats_widget[row_label[i]][3].configure(text=test[i-1])
