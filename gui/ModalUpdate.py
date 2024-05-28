import gui.SearchUI as SearchUI
from interaction.ReadFiles import build_img_ref
from PIL import Image


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

    def set_img_frame(self, Frame):
        self.img_holder = self.ctk.CTkLabel(master=Frame,
                                            image=None,
                                            text=None,
                                            fg_color='#ffffff',
                                            height=self.gui.img_height,
                                            width=self.gui.img_width,
                                            corner_radius=self.gui.rounded_corner)

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

    # def __display_img(self):
    #     """
    #     Display Image
    #     :return: null
    #     """
    #     if len(self.query_result) == 1:
    #         print("Found Image")
    #         pkdex_id = self.app.get_id(str(self.query_result[0]))
    #
    #         img = read_file.build_img_ref(pkdex_id)
    #         image_container = self.ctk.CTkImage(light_image=img, size=(256, 256))
    #
    #         if self.contains_img != True:
    #             self.image_disp = self.__img_label_build(image_container)
    #             self.contains_img = True
    #         else:
    #             self.image_disp.configure(image=image_container)
    #
    #         self.image_disp.pack()
    #         return True
    #     return False

    #
    # def __img_label_build(self, img_container):
    #     return self.ctk.CTkLabel(self.img_frame, image=img_container, text=None)
    #
    # def __focus(self, _widget, parentFrame, isFocused):
    #     if isFocused:
    #         self.gui.search_result_frame(parent_frame=parentFrame, inst="build")
    #     else:
    #         self.gui.search_result_frame(parent_frame=parentFrame, inst="destroy")

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

        print(ref_path)

        image = Image.open(ref_path[0])
        image.thumbnail(size=(self.gui.img_height-self.gui.rounded_corner,
                              self.gui.img_width-self.gui.rounded_corner))

        image_container = self.ctk.CTkImage(light_image=image,
                                            size=(image.width-self.gui.rounded_corner,
                                                  image.height-self.gui.rounded_corner))

        self.img_holder.configure(image=image_container)

        self.img_holder.pack()