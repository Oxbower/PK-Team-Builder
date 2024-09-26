from PIL import Image


def read_image(reference_list: list[str], str_option: str, size: tuple[int, int]) -> [Image]:
    """
    read images into RAM to display
    :param reference_list: list containing paths to images
    :param str_option: display options for image
    :param size: size of the image
    :return: list of images
    """
    loaded_image = []

    for value in reference_list:
        image = Image.open(value)
        if str_option == "thumbnail":
            image.thumbnail(size)
        loaded_image.append(image)

    return loaded_image
