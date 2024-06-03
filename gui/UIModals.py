import gui.ModalInteraction as ModalInteraction
from PIL import Image


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

        # instantiate modal_interact class can only be accessed by UIModals
        self.modal_interact = ModalInteraction.ModalInteraction(self.string_var, gui, ctk, mainWindow, Frame)

        self.types = [0, 0]

        self.types_adv = [0, 0]

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
        :param parentFrame: which frame to draw modals on
        :return: None
        """

        modals = ['File', 'Options']

        # build buttons for file bar
        for index, _ in enumerate(modals):
            file = self.ctk.CTkButton(master=parentFrame,
                                      text=modals[index],
                                      width=50,
                                      corner_radius=0,
                                      fg_color=self.gui.dark_grey,
                                      font=self.gui.font)
            file.grid(row=0, column=index)

    def build_img_modal(self, parentFrame):
        self.modal_interact.set_img_frame(parentFrame)

    def build_search_bar_modal(self, parentFrame):
        """
        Build the search bar modal
        :param parentFrame: which frame to draw modals on
        :return: None
        """
        name_plate = self.ctk.CTkEntry(master=parentFrame,
                                       textvariable=self.string_var,
                                       corner_radius=50,
                                       width=self.gui.img_width,
                                       height=50,
                                       fg_color="#2e2e2e",
                                       border_width=0,
                                       justify='center',
                                       font=("Helvetica", 20, "bold"))

        name_plate.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky=self.gui.expand_all,
                        )

        self.modal_interact.set_search_modal_frame(parentFrame)

        self.string_var.trace('w', self.modal_interact.search_bar_callback)

    def build_variation_modal(self, parentFrame):
        """
        Needs information about diff variation handled by modal update (dynamic)
        :param parentFrame: parentFrame to hold modal
        :return: None
        """
        image_ref = []
        path = ["./assets/rightarrowhead.png", "./assets/leftarrowhead.png"]

        frame = self.Frame(master=parentFrame,
                           width=parentFrame.cget("width"),
                           height=parentFrame.cget("height"))
        frame.grid()
        frame.grid_propagate(False)

        for i in path:
            image = Image.open(i)
            image.thumbnail(size=(10, 10))
            image_ref.append(image)

        image = self.ctk.CTkImage(light_image=image_ref[0],
                                  size=(image_ref[1].width, image_ref[1].height))
        self.modal_interact.set_variation_frame(parentFrame)

        button = self.ctk.CTkButton(master=self.gui.root,
                                    image=image,
                                    text=None,
                                    width=25,
                                    height=80,
                                    fg_color='#999999',
                                    corner_radius=0,
                                    hover_color=self.gui.hover_color,
                                    cursor="hand2",
                                    command=lambda: self.modal_interact.clicked_variation_button(parentFrame,
                                                                                                 button,
                                                                                                 image_ref)
                                    )

        button.place(in_=parentFrame,
                     bordermode="outside",
                     anchor="nw",
                     x=-5,
                     relx=1.0,
                     rely=0.2)

        return frame

    def build_item_ability_modal(self, parentFrame):
        """
        build selection modal for possible abilities and all items
        :param parentFrame: parentFrame to hold modal
        :return: None
        """
        max_width = parentFrame.cget("width")

        # build ability modal (open separate window for selection)
        ability = self.ctk.CTkButton(master=parentFrame,
                                     text="Abilities",
                                     fg_color="#2a2a2a",
                                     hover_color=self.gui.hover_color,
                                     cursor="hand2",
                                     height=45,
                                     width=max_width-10)

        ability.grid(row=0,
                     pady=5,
                     padx=5)

        # build item modal (open separate window for selection)
        items = self.ctk.CTkButton(master=parentFrame,
                                   text="Items",
                                   fg_color="#2a2a2a",
                                   hover_color=self.gui.hover_color,
                                   cursor="hand2",
                                   height=45,
                                   width=max_width-10)
        items.grid(row=1,
                   pady=(0, 5),
                   padx=5)

    def build_type_modal(self, parentFrame):
        """
        builds modal holding this pokemons diff types
        :param parentFrame: parent frame to hold modal
        :return: None
        """
        max_height = parentFrame.cget("height")

        # build type frame, store frame inside types to allow modalUpdate to access on change

        for index, value in enumerate(self.types):
            frame = self.Frame(master=parentFrame,
                               height=max_height - 10,
                               width=(self.gui.img_width / 2) - 10
                               )

            frame.grid(row=0,
                       column=index,
                       padx=5,
                       pady=5,
                       sticky="nsew")

            self.types[index] = frame

    def build_type_adv_modal(self, parentFrame):
        """
        builds modal which shows current pokemon's defensive strength and weaknesses
        :param parentFrame: parent frame to hold modals
        :return: None
        """

        # get the dimensions of this parent frame
        max_height = parentFrame.cget("height")
        max_width = parentFrame.cget("width")

        for index, value in enumerate(self.types_adv):
            frame = self.Frame(master=parentFrame,
                               height=max_height - 10,
                               width=(max_width / 2) - 10,
                               fg_color="#2a2a2a"
                               )

            frame.grid(row=0,
                       column=index,
                       padx=5,
                       pady=5)

            self.types_adv[index] = frame

        # for index in range(10):
        #     frame = self.Frame(master=self.types_adv[0],
        #                        height=(max_height / 10) - 5,
        #                        fg_color="white"
        #                        )
        #
        #     frame.grid(row=index,
        #                column=0,
        #                pady=2,
        #                padx=2)

    def build_move_modal(self, parentFrame):
        """
        build move modals limited to things that only this pokemon can learn in gen-9
        :param parentFrame: parent frame to hold modals
        :return: None
        """
        label = self.ctk.CTkLabel(master=parentFrame,
                                  text="Moves",
                                  font=("Helvetica", 20, "bold")
                                  )
        label.grid(row=0,
                   column=0,
                   sticky="w",
                   padx=10,
                   pady=7)

        for row in range(2):
            for col in range(2):
                modal = self.ctk.CTkButton(master=parentFrame,
                                           text="Move " + str((row + (col + row)) + 1),
                                           cursor="hand2",
                                           corner_radius=50,
                                           hover_color=self.gui.hover_color,
                                           width=200,
                                           height=90,
                                           # border_width=2,
                                           # border_color="#5a5a5a",
                                           fg_color="#2e2e2e")

                modal.grid(row=int(row + 1),
                           column=col,
                           padx=5,
                           pady=(0, 10),
                           sticky="nsew")

    def build_stat_modal(self, parentFrame):
        """
        Builds the stats frame up
        :param parentFrame: master frame of the stats modals
        :return: None
        """
        row_label = ["", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Total"]
        column_label = ["Base", "", "", ""]

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
                frame.grid_propagate(False)

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
                    # store frame to allow updates into stats_modal array
                    self.stats_widget[row_label[row_key]][col - 1] = frame
                else:
                    # store label to allow updates into stats_modal array
                    self.stats_widget[row_label[row_key]][col - 1] = label

        # Build column Labels
        for col in range(len(column_label)):
            if col != 1:
                self.stats_widget[""][col].configure(text=column_label[col])

        self.stats_widget["Total"][2].configure(text="Min")
        self.stats_widget["Total"][3].configure(text="Max")

        for i in row_label[1:-1]:
            outer_frame = self.Frame(master=self.stats_widget[i][1],
                                     height=self.stats_widget[i][1].cget("height") - 20,
                                     width=self.stats_widget[i][1].cget("width"))
            outer_frame.grid(pady=10)
            outer_frame.grid_propagate(False)

            self.stats_widget[i][1] = outer_frame

        self.modal_interact.set_stats_widget(self.stats_widget)


