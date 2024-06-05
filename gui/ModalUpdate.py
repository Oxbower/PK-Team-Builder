import gui.SearchUI as SearchUI
import os

from interaction.StatColorUpdate import stat_color_update
from interaction.AnimateStatBars import start_animation
from interaction.VariationFrameAnimation import open_variation_frame, close_variation_frame
from interaction.ReadFiles import build_img_ref, json_load
from app_io.LoadImage import read_image


class ModalUpdate:
    """
    Updates the modals when interaction occurs
    """
    def __init__(self, gui, ctk, mainWindow, Frame, modalInteract):
        self.variation_frame = False
        self.gui = gui
        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = Frame

        self.SearchUI = SearchUI.SearchUI(self.gui, self.ctk, self.mainWindow, self.Frame, modalInteract)

        self.container_frame = None
        self.img_holder = None
        self.var_frame = None
        self.stringvar = None
        self.stats_widget = None

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

    def set_variation_frame(self, Frame, stringvar):
        """
        pass in the variation frame to display current pokemons different forms
        :param Frame: frame to put the forms in
        :param stringvar: passed in function to update name display
        :return: None
        """
        self.var_frame = Frame
        self.stringvar = stringvar

    def build_search_result(self, result_list, parentFrame):
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
            print("Destroyed frame...")
        except Exception as E:
            print(E)

    def build_dynamic_variation_button(self, parentFrame, parentButton, image_ref):
        """
        Build the different form modals inside variation frame
        :param parentFrame: parentFrame to put the modal variations into
        :param parentButton: parentButton change arrow direction
        :param image_ref: references change arrow direction
        :return: None
        """
        if self.variation_frame:    # Close the variation frame
            # Remove remaining children inside var_frame
            for i in self.var_frame.winfo_children():
                i.grid_remove()

            image = self.ctk.CTkImage(light_image=image_ref[0],
                                      size=(image_ref[1].width, image_ref[1].height))
            parentButton.configure(image=image)

            close_variation_frame(parentFrame, self.delta_width)

            self.variation_frame = False

        elif not self.variation_frame:  # Open the variation frame
            image = self.ctk.CTkImage(light_image=image_ref[1],
                                      size=(image_ref[1].width, image_ref[1].height))
            parentButton.configure(image=image)

            open_variation_frame(parentFrame, self.delta_width, self.frame_width, self.var_frame)

            self.variation_frame = True

    def build_dynamic_variation_modal(self, ref_path: str):
        """
        Builds a dynamic modal for the number of variations this pokemon has, this only runs once on query
        :param ref_path: reference path to pokemon passed in by the clicked result
        :return: None
        """

        # On query select run this once to get rid of stuff currently in the image
        for widget in self.var_frame.winfo_children():
            widget.destroy()

        for index, value in enumerate(ref_path):
            # Check if theres only 1 variation of this pokemon, if so then escape
            if len(ref_path) == 1:
                break
            name = os.path.split(value)[-1]
            if name.endswith(".png"):
                name = name.split(".png")[0]
            else:
                name = name.split(".jpg")[0]

            variation_button = self.ctk.CTkButton(master=self.var_frame, # Change to self.var_frame
                                                  height=30,
                                                  fg_color='#232323',
                                                  hover_color='#3a3a3a',
                                                  width=self.frames * self.delta_width - 10,
                                                  text=name,
                                                  command=lambda string=value: self.update_display(string))

            if self.variation_frame:
                variation_button.grid(sticky="news", pady=5, padx=5, column=0)

        # Runs on query to show base form of pokemon (redo)
        variant = ["Mega", "Alolan", "Galarian", "Hisuian", "Paldean"]

        for value in ref_path:
            name = os.path.split(value)[-1]
            if name.endswith(".png"):
                name = name.split(".png")[0]
            else:
                name = name.split(".jpg")[0]

            if not any(s in name for s in variant):
                self.update_display(value)
                self.stringvar(name)
                break

    def build_path_ref(self, string):
        """
        Builds the image frame
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

        name = os.path.split(image_path)[-1]
        if name.endswith(".png"):
            name = name.split(".png")[0]
        else:
            name = name.split(".jpg")[0]

        self.stringvar(name)

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
        stats_folder = 'pokemon-pokedex'

        path = os.path.split(string)
        head_path = os.path.split(path[0])[1]
        tail_path = path[1].split('.')[0]

        self.build_image(string)
        self.update_stats_widget(os.path.join(stats_folder, head_path, tail_path + '.json'))

    def update_stats_widget(self, json_path):
        """
        Updates the displayed stats for the appropriate pokemon
        :param json_path: path to open json stats
        :return: None
        """
        data = json_load(json_path)

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
                                     width=0)
            inner_frame.grid()

            start_animation((inner_frame, display_width))

        self.stats_widget["Total"][0].configure(text=total)
