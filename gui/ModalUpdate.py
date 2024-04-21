import gui.SearchUI as SearchUI

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
        self.container_frame.place(y=55, x=5)

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
