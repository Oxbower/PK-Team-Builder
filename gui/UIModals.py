import gui.ModalInteraction as ModalInteraction
import customtkinter as ctk

import gui.TypeAdvantageFrames as taf
import gui.custommovewidget.MoveModal as MoveModal
import gui.customcanvaslabel.CustomCanvasLabel as CanvasLabel


class UIModals:
    """
    Instantiates the widgets for the GUI that called this class
    """
    def __init__(self, gui, current_window):
        """
        Initialize UI modals this is the stuff inside the
        frames.
        passes the interactable Modals to modal_iteract
        """
        self.ctk = ctk
        self.mainWindow = current_window
        self.Frame = ctk.CTkFrame
        self.gui = gui

        self.string_var = self.ctk.StringVar()

        # instantiate modal_interact class can only be accessed by UIModals
        self.modal_interact = ModalInteraction.ModalInteraction(self.string_var, gui, current_window)

        self.pokemon_id = None

        self.move_modal = []

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
        """
        Passes image frame to modalUpdate to allow for this frame to be updated
        :param parentFrame: the parent container
        :return: None
        """
        self.modal_interact.set_img_frame(parentFrame)

    def build_side_container(self, parentFrame):
        self.modal_interact.set_sidebar_widget(parentFrame)

    def build_type_modal(self, parentFrame):
        """
        Builds the pokedex-no container
        :param parentFrame: the parent container
        :return: None
        """

        # holds the pokemon's pokedex num
        frame = self.Frame(master=parentFrame,
                           fg_color='#666666',
                           height=45,
                           width=100)

        frame.grid(row=0, column=0, padx=5, sticky='nw')
        frame.grid_propagate(False)

        label = self.ctk.CTkLabel(master=frame,
                                  text='#0000',
                                  font=('Helvetica', 20, 'bold'),
                                  width=100,
                                  height=40)
        label.grid(row=0, column=0)
        label.grid_propagate(False)

        # holds the pokemon's type
        type_frame = self.Frame(master=parentFrame,
                                fg_color='#242424',
                                height=45,
                                width=100)

        type_frame.place(anchor='ne', rely=-0.1, relx=.96)

        # pass in the frame to write pokedex-num and type frame into
        self.modal_interact.set_type_widget(frame, type_frame)

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
                        sticky=self.gui.expand_all)

        self.modal_interact.set_search_modal_frame(parentFrame)

        name_plate.bind('<FocusIn>', lambda _: self.modal_interact.name_plate_focus(True))
        name_plate.bind('<FocusOut>', lambda _: self.modal_interact.name_plate_focus(False))

        self.string_var.trace('w', self.modal_interact.search_bar_callback)

    def build_item_ability_modal(self, parentFrame):
        """
        build selection modal for possible abilities and all items
        :param parentFrame: parentFrame to hold modal
        :return: None
        """
        max_height = parentFrame.cget("height")

        # build ability modal (open separate window for selection)
        canvas_label = CanvasLabel.CustomCanvasLabel(master=parentFrame,
                                                     text='Ability',
                                                     fg_color="#2a2a2a",
                                                     cursor="hand2",
                                                     width=45,
                                                     height=max_height - 70)

        canvas_label.place(relx=.1, rely=.02)

        # pass custom label object to click handler to pass into modalUpdate
        canvas_label.bind(sequence='<Button-1>', command=lambda _: self.modal_interact.clicked_ability_modal(canvas_label))
        canvas_label.bind(sequence='<Enter>', command=lambda _: canvas_label.configure(fg_color=self.gui.hover_color))
        canvas_label.bind(sequence='<Leave>', command=lambda _: canvas_label.configure(fg_color='#2a2a2a'))

        # build item modal (open separate window for selection)
        items = self.ctk.CTkButton(master=parentFrame,
                                   fg_color="#2a2a2a",
                                   text='',
                                   hover_color=self.gui.hover_color,
                                   cursor="hand2",
                                   height=45,
                                   width=45)
        items.propagate(False)

        items.place(relx=.1, rely=.85)


        items.configure(command=lambda: self.modal_interact.clicked_item_modal(items))

    def build_type_adv_modal(self, parentFrame):
        """
        builds modal which shows current pokemon's defensive strength and weaknesses
        :param parentFrame: parent frame to hold modals
        :return: None
        """
        options = ['Offensive', 'Defensive']
        initial_active_window, initial_active_button = None, None

        button_holder = self.Frame(master=parentFrame,
                                   corner_radius=0,
                                   fg_color='#242424')
        button_holder.grid(row=0,
                           column=0,
                           sticky='e',
                           padx=10)

        for index, value in enumerate(options):
            new_window = taf.TypeAdvantageFrames()

            button = self.ctk.CTkButton(master=button_holder,
                                        width=150,
                                        height=35,
                                        cursor="hand2",
                                        fg_color="#2e2e2e",
                                        font=("Helvetica", 15, "bold"),
                                        hover_color=self.gui.hover_color,
                                        text=value,
                                        command=None)

            button.configure(command=lambda string=value, window=new_window, button_config=button:
            self.modal_interact.type_adv_change_window(string, window, button_config))

            button.grid(row=0,
                        column=index,
                        padx=(5, 0),
                        sticky='w')

            if value == 'Defensive':
                color = 'orange'
                initial_active_window = new_window
                initial_active_button = button
            else:
                color = 'green'

            new_window.set_parent_frame(parentFrame, value)
            self.modal_interact.set_type_advantage_frame(new_window)

        self.modal_interact.type_adv_change_window('initial', initial_active_window, initial_active_button)

    def build_move_modal(self, parentFrame):
        """
        build move modals limited to things that only this pokemon can learn in gen-9
        :param parentFrame: parent frame to hold modals
        :return: None
        """

        for row in range(4):
            size = 0
            if row == 0:
                size = 5

            modal = MoveModal.MoveModal(master=parentFrame,
                                        fg_color='#2e2e2e',
                                        corner_radius=0,
                                        hover_color=self.gui.hover_color,
                                        width=parentFrame.cget('width') - 40,
                                        height=100)

            modal.configure(command=lambda _modal=modal: self.modal_interact.move_callback(_modal))

            modal.grid_propagate(False)

            modal.grid(row=row,
                       column=1,
                       padx=5,
                       pady=(size, 5),
                       sticky='nsew')

            self.move_modal.append(modal)

        self.modal_interact.set_move_modal(move_modal=self.move_modal)

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
            stat_frame.grid(row=row, column=0, sticky="ne", padx=10)

            # Build Col
            for col in range(5):
                width = 50

                if col == 2:
                    width = 300

                # Creates the inner frame to hold the actual numbers and bar graph
                frame = self.Frame(master=stat_frame,
                                   corner_radius=self.gui.flat_corner,
                                   height=self.gui.stat_subcategory_height,
                                   width=width)
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

        """
        Container for the 'stat' bar
        """
        for i in row_label[1:-1]:
            outer_frame = self.Frame(master=self.stats_widget[i][1],
                                     height=self.stats_widget[i][1].cget("height") - 20,
                                     width=self.stats_widget[i][1].cget("width"))
            outer_frame.grid(pady=10)
            outer_frame.grid_propagate(False)

            stat_bar = self.Frame(master=outer_frame,
                                  fg_color="#ff0000",
                                  height=outer_frame.cget('height'),
                                  width=5)
            stat_bar.grid()

            self.stats_widget[i][1] = stat_bar

        """
        Container for pokemon variations
        """
        var_frame = self.Frame(master=parentFrame,
                               height=50,
                               width=360,
                               fg_color='#212121',
                               corner_radius=0)
        var_frame.place(anchor="ne",
                        relx=.93,
                        rely=.143)

        self.modal_interact.set_stats_widget(self.stats_widget, var_frame)
