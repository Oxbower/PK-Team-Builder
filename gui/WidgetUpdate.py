import customtkinter as ctk
import threading
import os
import gui.custommovewidget.MoveWidgetUpdate as MoveWidgetUpdate
import gui.ItemWidgetFrame as ItemModalFrame
import gui.customcanvaslabel.CanvasLabelUpdate as CanvasLabelUpdate

from interaction.StatColorUpdate import stat_color_update
from interaction.AnimateStatBars import start_animation
from interaction.BuildDirectoryReference import build_img_ref
from interaction.MegaEvolutionVariantHandler import variant_handler, mega_variant_folder_handler
from app_io.LoadJson import json_load
from app_io.LoadImage import read_image
from interaction.GetTypeBackgroundColor import type_color
from interaction.TypeAdvantageHandler import type_advantage_defensive_handler


class WidgetUpdate:
    """
    Updates the modals when interaction occurs
    """
    def __init__(self, gui, current_window):
        """
        Initializes the class to update widgets
        :param gui: the gui class that called started this instance
        :param current_window: the ctk window root instance
        """
        self.gui = gui
        self.ctk = ctk
        self.mainWindow = current_window
        self.Frame = ctk.CTkFrame

        self._pokemon_name_widget = None
        self.img_holder = None
        self._variation_frame = None
        self._stats_widget = None
        self._pokedex_num_widget = None
        self._type_frame = None
        self._sidebar_widget = None
        self.dir_folder = None
        self.current_name = None
        self._move_widget = None
        self._item_widget = None
        # Instantiate move modal class
        self.scrollable_move_frame = MoveWidgetUpdate.MoveWidgetUpdate(current_window)
        self._type_advantage_frame = []  # offensive, defensive

        # Pass in current window to anchor new frame, rework later
        self.scrollable_item_frame = ItemModalFrame.ItemModalFrame()

        self.scrollable_ability_frame = CanvasLabelUpdate.CanvasLabelUpdate(current_window)

    """
    Sets the widgets to be updated
    """
    def set_img_frame(self, img_frame):
        """
        Sets image frame to display creature art
        :param img_frame: Parent frame
        :return: None
        """
        if img_frame is None:
            quit()

        self.img_holder = self.ctk.CTkLabel(master=img_frame,
                                            image=None,
                                            text=None,
                                            fg_color='#ffffff',
                                            bg_color='#212121',
                                            height=self.gui.IMG_HEIGHT,
                                            width=self.gui.IMG_WIDTH,
                                            corner_radius=self.gui.ROUNDED_CORNER)

    def set_move_widget(self, move_widget):
        self._move_widget = move_widget

    def set_stats_widget(self, stats_widget):
        """
        Sets the stats widget
        :param stats_widget: dictionary to update the stats widget
        :return: None
        """
        self._stats_widget = stats_widget

    def set_sidebar_widget(self, sidebar_widget):
        """
        Sets the sidebar
        :param sidebar_widget: stores the sidebar widget to ref in this file
        :return:
        """
        self._sidebar_widget = sidebar_widget

    def set_type_widget(self, pokedex_no, type_frame):
        """
        sets the type widget
        :param pokedex_no: widget that contains label to update
        :param type_frame: holds type_frame
        :return:
        """
        self._pokedex_num_widget = pokedex_no
        self._type_frame = type_frame

    def set_type_advantage_frame(self, frame):
        self._type_advantage_frame.append(frame)

    def set_variation_frame(self, variation_frame):
        """
        pass in the variation frame to display current pokemons different forms
        :param variation_frame: frame to put the forms in
        :return: None
        """
        self._variation_frame = variation_frame

    def set_item_modal(self, item_widget):
        self._item_widget = item_widget

    def set_name_plate(self, name_plate: ctk.CTkButton):
        self._pokemon_name_widget = name_plate

    """
    below are the functions to update the widgets
    """

    def build_pokemon_variant_widgets(self, ref_path: list[str]) -> None:
        """
        builds widgets that show the variations this pokemon has, this only runs once every query
        :param ref_path: reference path to pokemon passed in by the clicked result
        :return: None
        """

        # On query select run this once to get rid of stuff currently in the image
        for widget in self._variation_frame.winfo_children():
            widget.destroy()

        for widget in self._sidebar_widget.winfo_children():
            widget.destroy()

        split_ref = variant_handler(ref_path)

        for index, value in enumerate(split_ref['standard']):
            image = read_image([value], "thumbnail", size=(20, 50))[0]
            image = self.ctk.CTkImage(light_image=image, size=(image.width, image.height))

            variation_button = self.ctk.CTkButton(master=self._variation_frame,  # Change to self.var_frame
                                                  height=50,
                                                  fg_color='#ffffff',
                                                  hover_color='#ffffff',
                                                  width=30,
                                                  text=None,
                                                  image=image,
                                                  command=lambda string=value: self.update_when_variant_chosen(string))

            variation_button.grid(row=0, column=index, padx=5)

        if len(split_ref['mega']) != 0:
            image = mega_variant_folder_handler(split_ref['mega'][0])

            for index, value in enumerate(image):
                image = read_image([value], "thumbnail", size=(30, 30))[0]

                image = self.ctk.CTkImage(light_image=image, size=(image.width, image.height))
                variation_button = self.ctk.CTkButton(master=self._sidebar_widget,  # Change to self.var_frame
                                                      height=40,
                                                      fg_color='#aa0066',
                                                      hover_color='#770033',
                                                      width=50,
                                                      text=None,
                                                      image=image,
                                                      command=lambda string=split_ref['mega'][index]:
                                                      self.update_when_variant_chosen(string))

                variation_button.grid(row=index, column=0, padx=5, pady=(5, 5))

        # Runs on query to show base form of pokemon (redo)
        variant = ["Mega ", "Alolan ", "Galarian ", "Hisuian ", "Paldean "]

        for value in ref_path:
            name = os.path.splitext(os.path.basename(value))[0]

            if not any(s in name for s in variant):
                self.update_when_variant_chosen(value)
                self.update_pokemon_name_displayed(name)
                break

    def update_widget_related_to_search(self, string: str, which_modal: str) -> None:
        """
        Updates the widget according to user chosen result
        :param which_modal: which modal was this query for
        :param string: the clicked string
        :return: None
        """
        if which_modal == "name_plate":
            name = string.lower().split(' ')
            name = '-'.join(name)

            print("Clicked Result: " + name)
            ref_path = build_img_ref("pokemon-artwork", name)
            self.build_pokemon_variant_widgets(ref_path)
        elif which_modal == "item_modal":
            name_capitalized = []
            for i in string.split(" "):
                name_capitalized.append(i.capitalize())
            self.scrollable_item_frame.active_modal_callback(self._item_widget, " ".join(name_capitalized))

    def update_pokemon_name_displayed(self, pokemon_name: str) -> None:
        """
        Update the pokemon name displayed
        :param pokemon_name: new name
        :return: None
        """
        self._pokemon_name_widget.configure(text=pokemon_name, text_color="white")

    def update_when_variant_chosen(self, variant_name: str) -> None:
        """
        Updates the frame with data related to variant
        :param variant_name: name of the pokemon currently displayed
        :return: None
        """
        stats_folder = 'pokemon-pokedex'

        inner_folder = os.path.split(os.path.split(variant_name)[0])[-1]
        file_name = os.path.splitext(os.path.basename(variant_name))[0]
        self.dir_folder = inner_folder
        self.current_name = file_name

        json_path = os.path.join(stats_folder, inner_folder, file_name + '.json')
        data = json_load(json_path)

        self.update_pokemon_image(variant_name)

        # Update the stats widget
        self.update_stats_widget(data)
        self.update_pokemon_id(data)
        self.update_type_displayed(data)
        self.update_type_advantage(data)

        self.scrollable_move_frame.reset_modal(self._move_widget)

    def update_moves(self, modal) -> None:
        """
        passes in the possible moves to be put in this move modal
        :param modal: which modal to update
        :return: None
        """
        if self.dir_folder is None: # guard clause
            print('Empty selection')
            return

        self.scrollable_move_frame.start_search_build(modal, self.dir_folder, self.current_name)

    def update_pokemon_image(self, image_path) -> None:
        """
        Opens and updates the frame to hold the image
        :param image_path: image_path given by variation_model
        :return: None
        """
        self.gui.root.focus_set()

        name = os.path.splitext(os.path.basename(image_path))[0]

        self.update_pokemon_name_displayed(name)

        # Only returns a single image
        image = read_image([image_path], "thumbnail",
                           (self.gui.IMG_HEIGHT - self.gui.ROUNDED_CORNER,
                            self.gui.IMG_WIDTH - self.gui.ROUNDED_CORNER))[0]

        image_container = self.ctk.CTkImage(light_image=image,
                                            size=(image.width - self.gui.ROUNDED_CORNER,
                                                  image.height - self.gui.ROUNDED_CORNER))

        self.img_holder.configure(image=image_container)

        self.img_holder.pack()

    def update_pokemon_id(self, data) -> None:
        """
        update the pokedex id of the current pokemon
        :param data: pokedex id of pokemon
        :return: None
        """

        # Left pad 0's until there are 4 figures
        pokedex_no = str(data['pokedex-no']).zfill(4)

        label = self.ctk.CTkLabel(master=self._pokedex_num_widget,
                                  text='#' + pokedex_no,
                                  font=('Helvetica', 20, 'bold'),
                                  width=100,
                                  height=40)
        label.grid(row=0, column=0)

        label.grid_propagate(False)

    def update_type_displayed(self, data) -> None:
        """
        Updates the type displayed for the current pokemon
        :param data: type data of pokemon
        :return: None
        """
        for value in self._type_frame.winfo_children():
            value.destroy()

        type_data = data['type']

        for index, value in enumerate(type_data):
            image = read_image(
                [os.path.join('.', 'assets', 'type-icon', type_data[value].lower()) + '.png'],
                'thumbnail', size=(200, 200))[0]
            image = self.ctk.CTkImage(light_image=image, size=(30, 30))

            color = type_color(type_data[value])

            types = self.Frame(master=self._type_frame,
                               fg_color=color,
                               width=40,
                               height=46)

            types.grid(row=0,
                       column=index,
                       padx=5,
                       sticky='en')
            types.grid_propagate(False)

            label = self.ctk.CTkLabel(master=types,
                                      image=image,
                                      text=None)
            label.place(anchor="center", relx=.5, rely=.55)

    def update_type_advantage(self, data) -> None:
        """
        Updates the contents of type advantage button
        :param data: passes the current pokemons type
        :return: None
        """
        type_defense = type_advantage_defensive_handler(data)

        # defensive
        start_thread = threading.Thread(target=self._type_advantage_frame[1].populate_frame, args=(type_defense,))
        start_thread.run()

    def update_ability_widget(self, modal) -> None:
        """
        Updates the ability modal
        :param modal: which modal this update is related to
        :return: None
        """
        self.scrollable_ability_frame.start_search_build(modal, self.dir_folder, self.current_name)

    def update_stats_widget(self, data) -> None:
        """
        Updates the displayed stats for the appropriate pokemon
        :param data: data returned by json
        :return: None
        """
        row_label = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

        total = 0
        max_val = 255   # Max value that all stat can have

        max_width = self.mainWindow.root.nametowidget(self._stats_widget['HP'][1].winfo_parent()).winfo_width()

        for i in row_label:
            self._stats_widget[i][0].configure(text=data['stats'][i]['base'])
            self._stats_widget[i][2].configure(text=data['stats'][i]['min'])
            self._stats_widget[i][3].configure(text=data['stats'][i]['max'])

            # How much of the bar should be visible
            percentile = (data['stats'][i]['base'] / max_val)

            # Accumulate value of base stat
            total = total + data['stats'][i]['base']

            display_width = int(max_width * percentile)

            # Change stat_bar size and color
            if self._stats_widget[i][1].cget('width') != display_width:
                # Minimum bar fill
                if max_width * percentile < 5:
                    self._stats_widget[i][1].configure(fg_color=stat_color_update(data['stats'][i]['base']))
                    self._stats_widget[i][1].configure(width=5)
                else:
                    self._stats_widget[i][1].configure(fg_color=stat_color_update(data['stats'][i]['base']))

                    # Use a queue
                    start_animation(self._stats_widget[i][1], display_width)

        self._stats_widget["Total"][0].configure(text=total)
