import os

from PIL import Image
from customtkinter import CTkImage

def read_image(reference_list: list[str], str_option: str, size: tuple[int, int]) -> [Image]:
    loaded_image = []

    for value in reference_list:
        image = Image.open(value)
        if str_option == "thumbnail":
            image.thumbnail(size)
        loaded_image.append(image)

    return loaded_image


types_image_PIL = [
    read_image([os.path.join('assets', 'type-icon', i)], 'thumbnail', (200, 200))[0]
    for i in os.listdir(os.path.join('assets', 'type-icon'))]

key_values = [os.path.splitext(os.path.basename(key))[0] for key in os.listdir(os.path.join('assets', 'type-icon'))]

load_type_ctk_images = {key: CTkImage(light_image=image, size=(30, 30))
                        for key, image in zip(key_values, types_image_PIL)}
