import os


def build_img_ref(directory: str, inner_path: str) -> str:
    """
    Build os dependent path for image loader
    :param directory: the directory to be accessed
    :param inner_path: image path
    """
    path = []
    build_href = os.path.join(directory, inner_path)
    for i in os.listdir(build_href):
        path.append(os.path.join(build_href, i))

    return path
