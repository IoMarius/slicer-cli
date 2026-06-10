from slicer.utils.image import load_image, resize, normalize


def preprocess(path: str):
    img = load_image(path)
    img = resize(img)
    img = normalize(img)
    return img
