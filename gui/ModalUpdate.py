import gui.SearchUI as SearchUI
import os
import json
from interaction.StatColorUpdate import stat_color_update
from interaction.ReadFiles import build_img_ref, json_load
from PIL import Image


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
        self.frames = 25

    def set_img_frame(self, Frame):
        self.img_holder = self.ctk.CTkLabel(master=Frame,
                                            image=None,
                                            text=None,
                                            fg_color='#ffffff',
                                            height=self.gui.img_height,
                                            width=self.gui.img_width,
                                            corner_radius=self.gui.rounded_corner)

    def set_stats_widget(self, stats_widget):
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
        if self.variation_frame:
            for i in self.var_frame.winfo_children():
                i.grid_remove()

            for i in range(self.frames):
                parentFrame.configure(width=parentFrame.cget('width') - self.delta_width)
                parentFrame.update()
            self.variation_frame = False

            image = self.ctk.CTkImage(light_image=image_ref[0],
                                      size=(image_ref[1].width, image_ref[1].height))
            parentButton.configure(image=image)

        elif not self.variation_frame:
            for i in range(self.frames):
                parentFrame.configure(width=parentFrame.cget('width') + self.delta_width)
                parentFrame.update()
            self.variation_frame = True

            for i in self.var_frame.winfo_children():
                i.grid(sticky="news",
                       pady=5,
                       padx=5,
                       column=0)

            image = self.ctk.CTkImage(light_image=image_ref[1],
                                      size=(image_ref[1].width, image_ref[1].height))
            parentButton.configure(image=image)

    def build_dynamic_variation_modal(self, ref_path, folder_name):
        """
        Builds a dynamic modal for the number of variations this pokemon has, this only runs once on query
        :return: None
        """
        for widget in self.var_frame.winfo_children():
            widget.destroy()

        for index, value in enumerate(ref_path):
            if len(ref_path) == 1:
                break
            name = os.path.split(value)[-1]
            if name.endswith(".png"):
                name = name.split(".png")[0]
            else:
                name = name.split(".jpg")[0]

            # Change this in the future
            image = Image.open(value)
            image.thumbnail(size=(30, 30))

            image_container = self.ctk.CTkImage(light_image=image,
                                                size=(image.width, image.height))

            variation_button = self.ctk.CTkButton(master=self.var_frame,
                                                  height=50,
                                                  # fg_color='#ffffff',
                                                  # hover_color='#ffffff',
                                                  # text_color='#000000',
                                                  width=self.frames * self.delta_width,
                                                  # image=image_container,
                                                  text=name,
                                                  command=lambda string=value: self.update_display(string))

            if self.variation_frame:
                variation_button.grid(sticky="news", pady=5, padx=5, column=0)

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
        self.build_dynamic_variation_modal(ref_path, name)

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

        image = Image.open(image_path)
        image.thumbnail(size=(self.gui.img_height - self.gui.rounded_corner,
                              self.gui.img_width - self.gui.rounded_corner))

        image_container = self.ctk.CTkImage(light_image=image,
                                            size=(image.width - self.gui.rounded_corner,
                                                  image.height - self.gui.rounded_corner))

        self.img_holder.configure(image=image_container)

        self.img_holder.pack()

    def update_display(self, string):
        stats_folder = 'pokemon-pokedex'

        path = os.path.split(string)
        head_path = os.path.split(path[0])[1]
        tail_path = path[1].split('.')[0]

        self.build_image(string)
        self.update_stats_widget(os.path.join(stats_folder, head_path, tail_path + '.json'))

    def update_stats_widget(self, json_path):
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

            percentile = (data['stats'][i]['base'] / max_val)
            total = total + data['stats'][i]['base']
            for widget in self.stats_widget[i][1].winfo_children():
                widget.destroy()

            display_width = max_width * percentile
            if max_width * percentile < 5:
                display_width += 5

            inner_frame = self.Frame(master=self.stats_widget[i][1],
                                     fg_color=stat_color_update(data['stats'][i]['base']),
                                     height=max_height,
                                     width=display_width)
            inner_frame.grid()

        self.stats_widget["Total"][0].configure(text=total)
