from PIL import Image


def read_image(reference_list: list[str], str_option: str, size: tuple[int, int]) -> [Image]:
    loaded_image = []

    for value in reference_list:
        image = Image.open(value)
        if str_option == "thumbnail":
            image.thumbnail(size)
        loaded_image.append(image)

    return loaded_image


def read_json():
    pass

