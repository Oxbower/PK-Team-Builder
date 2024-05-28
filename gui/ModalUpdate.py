import gui.SearchUI as SearchUI
import os
from interaction.ReadFiles import build_img_ref
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

        self.delta_width = 4
        self.frames = 50

    def set_img_frame(self, Frame):
        self.img_holder = self.ctk.CTkLabel(master=Frame,
                                            image=None,
                                            text=None,
                                            fg_color='#ffffff',
                                            height=self.gui.img_height,
                                            width=self.gui.img_width,
                                            corner_radius=self.gui.rounded_corner)

    def set_variation_frame(self, Frame, stringvar):
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

    def build_dynamic_variation_modal(self, ref_path):
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
                                                  height=(self.var_frame.cget('height') / len(ref_path)) - 10,
                                                  fg_color='#ffffff',
                                                  hover_color='#ffffff',
                                                  text_color='#000000',
                                                  width=self.frames * self.delta_width,
                                                  image=image_container,
                                                  text=name,
                                                  command=lambda string=value: self.build_image(string))

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
                self.build_image(value)
                self.stringvar(name)
                break

    def build_path_ref(self, string):
        """
        Builds the image frame
        :return:
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

        image = Image.open(image_path)
        image.thumbnail(size=(self.gui.img_height - self.gui.rounded_corner,
                              self.gui.img_width - self.gui.rounded_corner))

        image_container = self.ctk.CTkImage(light_image=image,
                                            size=(image.width - self.gui.rounded_corner,
                                                  image.height - self.gui.rounded_corner))

        self.img_holder.configure(image=image_container)

        self.img_holder.pack()
