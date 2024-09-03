import os

from customtkinter import CTkImage
from app_io.LoadImage import read_image


types_image_PIL = [
    read_image([os.path.join('assets', 'item-artwork', i)], 'thumbnail', (200, 200))[0]
    for i in os.listdir(os.path.join('assets', 'item-artwork'))]

key_values = [os.path.splitext(os.path.basename(key))[0] for key in os.listdir(os.path.join('assets', 'item-artwork'))]

load_item_ctk_images = {key: CTkImage(light_image=image, size=(30, 30))
                        for key, image in zip(key_values, types_image_PIL)}