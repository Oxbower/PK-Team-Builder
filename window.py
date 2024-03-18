from tkinter import Frame, Label, Button
from PIL import ImageTk

class Window:
    def __init__(self, tk):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)

    def create_window(self):
        self.root.title("pktb")
        self.root.minsize(width=800, height=600)
        self.build_gen_frame()

    def build_gen_frame(self):
        container_frame = Frame(self.root, bg="red", height=1080, width=1920)
        container_frame.pack()

        but = Button(container_frame, text="Test")
        but.pack()

    # Build frame for window
    def build_img_frame(self):
        img_frame = Frame(self.root)
        img_frame.pack()


    # Bind to frame
    def display_img(self, image):
        ImageTk.PhotoImage(image)
