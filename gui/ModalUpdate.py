import gui.SearchUI as SearchUI

class ModalUpdate:
    """
    Updates the modals when interaction occurs
    """
    def __init__(self, gui, ctk, mainWindow, Frame):
        self.gui = gui
        self.ctk = ctk
        self.mainWindow = mainWindow
        self.Frame = Frame

        self.SearchUI = SearchUI.SearchUI(self.gui, self.ctk, self.mainWindow, self.Frame)

    def build_search_result(self, result_list, parentFrame):
        """
        Builds search result
        """

        # build result frame
        self.SearchUI.build_frame(result_list, parentFrame)
