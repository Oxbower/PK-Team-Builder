import gui.SearchUI as SearchUI
import os

from interaction.StatColorUpdate import stat_color_update
from interaction.AnimateStatBars import start_animation
from interaction.ReadFiles import build_img_ref
from interaction.MegaEvolutionVariantHandler import variant_handler, mega_variant_folder_handler
from app_io.LoadJson import json_load
from app_io.LoadImage import read_image
from gui.TypeBackgroundColor import type_color


class ModalUpdate:
    """
    Updates the modals when interaction occurs
    """
    def __init__(self, gui, ctk, mainWindow, Frame, modalInteract):
        self.gui = gui
        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = Frame

        self.SearchUI = SearchUI.SearchUI(self.gui, self.ctk, self.mainWindow, self.Frame, modalInteract)

        self.container_frame = None
        self.img_holder = None
        self.var_frame = None
        self.string_var = None
        self.stats_widget = None
        self.pokedex_no = None
        self.name_plate_focused = None
        self.type_frame = None
        self.sidebar_widget = None

        self.delta_width = 10
        self.frame_width = 250
        self.frames = 25

    def set_img_frame(self, Frame):
        """
        Sets image frame to display creature art

        :param Frame: Parent frame
        :return: None
        """
        self.img_holder = self.ctk.CTkLabel(master=Frame,
                                            image=None,
                                            text=None,
                                            fg_color='#ffffff',
                                            bg_color='#212121',
                                            height=self.gui.img_height,
                                            width=self.gui.img_width,
                                            corner_radius=self.gui.rounded_corner)

    def set_stats_widget(self, stats_widget):
        """
        Sets the stats widget

        :param stats_widget: dictionary to update the stats widget
        :return: None
        """
        self.stats_widget = stats_widget

    def set_sidebar_widget(self, sidebar_widget):
        self.sidebar_widget = sidebar_widget

    def set_type_widget(self, pokedex_no, type_frame):
        self.pokedex_no = pokedex_no
        self.type_frame = type_frame

    def set_variation_frame(self, Frame, string_var, name_plate_focused):
        """
        pass in the variation frame to display current pokemons different forms

        :param name_plate_focused: passed in function to update the name_plate_focus
        :param Frame: frame to put the forms in
        :param string_var: passed in function to update name display
        :return: None
        """
        self.var_frame = Frame
        self.string_var = string_var
        self.name_plate_focused = name_plate_focused

    def build_search_result(self, result_list: list[str], parentFrame):
        """
        Builds search result

        :param result_list: list to build search result for
        :param parentFrame: parentFrame for this class so stat_frame
        :return: None
        """

        # destroy container frame to stop filling up heap
        if self.container_frame is not None:
            self.container_frame.destroy()

        frame_width = parentFrame.winfo_width()

        # Work around to destroy scrollable frame, it's a known issue on Github #2266
        self.container_frame = self.Frame(master=parentFrame, width=0)
        # place the container in the stat frame at fixed location
        self.container_frame.place(y=70, x=25)

        # build result frame
        self.SearchUI.build_frame(result_list, self.container_frame, frame_width)

    def destroy_result_frame(self):
        """
        Destroy frame after user has chosen a result

        :return: None
        """
        try:
            self.container_frame.destroy()
            print("Destroying result frame...")
        except Exception as E:
            print(E)

    def build_dynamic_variation_modal(self, ref_path: list[str]):
        """
        Builds a dynamic modal for the number of variations this pokemon has, this only runs once on query

        :param ref_path: reference path to pokemon passed in by the clicked result
        :return: None
        """

        # On query select run this once to get rid of stuff currently in the image
        for widget in self.var_frame.winfo_children():
            widget.destroy()

        for widget in self.sidebar_widget.winfo_children():
            widget.destroy()

        split_ref = variant_handler(ref_path)

        for index, value in enumerate(split_ref['standard']):
            image = read_image([value], "thumbnail", size=(20, 50))[0]
            image = self.ctk.CTkImage(light_image=image, size=(image.width, image.height))

            variation_button = self.ctk.CTkButton(master=self.var_frame,  # Change to self.var_frame
                                                  height=50,
                                                  fg_color='#ffffff',
                                                  hover_color='#ffffff',
                                                  width=30,
                                                  text=None,
                                                  image=image,
                                                  command=lambda string=value: self.update_display(string))

            variation_button.grid(row=0, column=index, padx=5)

        if len(split_ref['mega']) != 0:
            image = mega_variant_folder_handler(split_ref['mega'][0])

            for index, value in enumerate(image):
                image = read_image([value], "thumbnail", size=(30, 30))[0]

                image = self.ctk.CTkImage(light_image=image, size=(image.width, image.height))
                variation_button = self.ctk.CTkButton(master=self.sidebar_widget,  # Change to self.var_frame
                                                      height=40,
                                                      fg_color='#aa0066',
                                                      hover_color='#770033',
                                                      width=50,
                                                      text=None,
                                                      image=image,
                                                      command=lambda string=split_ref['mega'][index]:
                                                      self.update_display(string))

                variation_button.grid(row=index, column=0, padx=5, pady=(5, 5))

        # Runs on query to show base form of pokemon (redo)
        variant = ["Mega ", "Alolan ", "Galarian ", "Hisuian ", "Paldean "]

        for value in ref_path:
            name = os.path.splitext(os.path.basename(value))[0]

            if not any(s in name for s in variant):
                self.update_display(value)
                self.string_var(name)
                break

    def build_path_ref(self, string):
        """
        Builds the image frame

        :param string:
        :return: None
        """
        name = string.lower()
        name = name.split(' ')
        name = '-'.join(name)

        print("Clicked Result: " + name)
        ref_path = build_img_ref(name)
        self.build_dynamic_variation_modal(ref_path)

    def build_image(self, image_path):  # Modular do not mess with this anymore
        """
        Opens and updates the frame to hold the image

        :param image_path: image_path given by variation_model
        :return: None
        """
        self.gui.root.focus_set()

        name = os.path.splitext(os.path.basename(image_path))[0]

        self.string_var(name)

        # Only returns a single image
        image = read_image([image_path], "thumbnail",
                           (self.gui.img_height - self.gui.rounded_corner,
                            self.gui.img_width - self.gui.rounded_corner))[0]

        image_container = self.ctk.CTkImage(light_image=image,
                                            size=(image.width - self.gui.rounded_corner,
                                                  image.height - self.gui.rounded_corner))

        self.img_holder.configure(image=image_container)

        self.img_holder.pack()

    def update_display(self, string):
        """
        Updates the entire frame with new data

        :param string: name of the pokemon currently displayed
        :return: None
        """
        self.name_plate_focused(False)

        stats_folder = 'pokemon-pokedex'

        inner_folder = os.path.split(os.path.split(string)[0])[-1]
        path = os.path.splitext(os.path.basename(string))[0]

        json_path = os.path.join(stats_folder, inner_folder, path + '.json')
        data = json_load(json_path)

        self.build_image(string)

        # Update the stats widget
        self.update_stats_widget(data)
        self.update_pokemon_id(data)
        self.update_type_displayed(data)

    def update_pokemon_id(self, data):
        # Left pad 0's until there are 4 figures
        pokedex_no = str(data['pokedex-no']).zfill(4)

        label = self.ctk.CTkLabel(master=self.pokedex_no,
                                  text='#' + pokedex_no,
                                  font=('Helvetica', 20, 'bold'),
                                  width=100,
                                  height=40)
        label.grid(row=0, column=0)

        label.grid_propagate(False)

    def update_type_displayed(self, data):
        for value in self.type_frame.winfo_children():
            value.destroy()

        type_data = data['type']

        for index, value in enumerate(type_data):
            image = read_image(
                [os.path.join('.', 'assets', 'type-icon', type_data[value].lower()) + '.png'],
                'thumbnail', size=(200, 200))[0]
            image = self.ctk.CTkImage(light_image=image, size=(30, 30))

            color = type_color(type_data[value])

            types = self.Frame(master=self.type_frame,
                               fg_color=color,
                               width=40,
                               height=46)

            types.grid(row=0, column=index, padx=5, sticky='en')
            types.grid_propagate(False)

            label = self.ctk.CTkLabel(master=types, image=image, text=None)
            label.place(anchor="center", relx=.5, rely=.55)

    def update_stats_widget(self, data):
        """
        Updates the displayed stats for the appropriate pokemon

        :param json_path: path to open json stats
        :return: None
        """
        row_label = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

        total = 0
        max_val = 255

        max_height = self.stats_widget["HP"][1].cget("height")
        max_width = self.stats_widget["HP"][1].cget("width")

        for i in row_label:
            self.stats_widget[i][0].configure(text=data['stats'][i]['base'])
            self.stats_widget[i][2].configure(text=data['stats'][i]['min'])
            self.stats_widget[i][3].configure(text=data['stats'][i]['max'])

            # How much of the bar should be visible
            percentile = (data['stats'][i]['base'] / max_val)

            # Accumulate value of base stat (Generally not useful in actual play)
            total = total + data['stats'][i]['base']

            # Destroy the current bar in display
            for widget in self.stats_widget[i][1].winfo_children():
                widget.destroy()

            display_width = max_width * percentile

            # Minimum bar fill
            if max_width * percentile < 5:
                display_width = 5

            inner_frame = self.Frame(master=self.stats_widget[i][1],
                                     fg_color=stat_color_update(data['stats'][i]['base']),
                                     height=max_height,
                                     width=2)
            inner_frame.grid()

            start_animation(inner_frame, display_width)

        self.stats_widget["Total"][0].configure(text=total)
