import numpy
from PIL import Image


class ImageProcessor():
    def load(self, path):
        with Image.open(path) as img:
            w, h = img.size
            print("Loading image of dimensions", w, 'x', h, "pixels.")
            return numpy.array(img)

    def display(self, array):
        img = Image.fromarray(array, 'RGB')
        img.show()
        w, h = img.size
        print("Display image of dimensions", w, 'x', h, "pixels.")


class ColorFilter():
    def invert(self, arr):
        return numpy.invert(arr)

    def to_blue(self, arr):
        arr[:, :, 1] = 0
        arr[:, :, 0] = 0
        return arr

    def to_green(self, arr):
        arr[:, :, 2] = 0
        arr[:, :, 0] = 0
        return arr

    def to_red(self, arr):
        arr[:, :, 2] = 0
        arr[:, :, 1] = 0
        return arr

    def celluloid(self, arr):
        pass

    def to_grayscale(self, arr, filter):

        return arr


img = ImageProcessor()
item = ColorFilter()
array = img.load("../resources/test.png")
array = item.to_grayscale(array, 1)
processedImg = Image.fromarray(array, 'RGB')
processedImg.show()
