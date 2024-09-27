import os


def build_img_ref(inner_path):
    """
    Build os dependent path for image loader
    :param inner_path: image path
    """
    path = []
    build_href = os.path.join('pokemon-artwork', inner_path)
    for i in os.listdir(build_href):
        path.append(os.path.join(build_href, i))

    return path
