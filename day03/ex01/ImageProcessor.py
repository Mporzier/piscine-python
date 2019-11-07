import numpy
from PIL import Image


class ImageProcessor():
    def load(self, path):
        with Image.open(path) as img:
            w, h = img.size
            print("Loading image of dimensions", w, 'x', h, "pixels.")
            return numpy.array(img)

    def display(self, array):
        data = Image.fromarray(array, 'RGB')
        data.show()
