import os

from customtkinter import CTkImage
from app_io.LoadImage import read_image


class LoadImageDictionary:
    """
    Load specified image directory as a dictionary
    {'filename': 'filepath'}
    """
    def __init__(self, parent_directory: str = '', sub_directory: str = '', size: tuple[int, int] = (40, 40)):
        self.parent_directory = parent_directory
        self.sub_directory = sub_directory
        self.size = size

    def load_image(self):
        """
        public call to load given image directory
        :param directory: directory to pull images from
        :return: None
        """

        """
        TODO: move to seperate thread
        """

        # open images as PIL object
        images_PIL = []
        key_values = []

        for images in os.listdir(os.path.join(self.parent_directory, self.sub_directory)):
            # append images inside directory to a list
            images_PIL.append(os.path.join(self.parent_directory, self.sub_directory, images))
            key_values.append(os.path.splitext(os.path.basename(images))[0])

        # read_image returns a list of PIL images
        images_PIL = read_image(images_PIL,'thumbnail', (40, 40))

        dict_CTkImages = dict()

        for key, image in zip(key_values, images_PIL):
            dict_CTkImages[key] = CTkImage(light_image=image, size=self.size)

        return dict_CTkImages
