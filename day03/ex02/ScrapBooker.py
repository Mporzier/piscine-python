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


class ScrapBooker():
    def crop(self, arr, dim, pos=(0, 0)):
        img = Image.fromarray(arr)
        w, h = img.size
        if dim[0] < 1 or dim[1] < 1:
            print("Cropping failed: dimensions cannot be less than 1.")
            return arr
        if dim[0] > w or dim[1] > h:
            print(
                "Cropping failed: dimensions cannot be greater than the dimensions of the image.")
            return arr
        if pos[0] < 0 or pos[1] < 0 or pos[0] > w or pos[1] > h:
            print("Cropping failed: position cannot be outside of the image.")
            return arr
        area = (pos[0], pos[1], dim[0], dim[1])
        cropped = img.crop(area)
        w, h = cropped.size
        print("Image has been cropped to a size of", w, 'x', h, "pixels.")
        return numpy.array(cropped)

    def thin(self, array, n, axis):
        pass

    def juxtapose(self, arr, n, axis):
        img = Image.fromarray(arr)
        w, h = img.size
        newW = w * n
        newH = h * n
        i = 0
        if axis == 1:
            juxImg = Image.new('RGB', (newW, h))
            while i < n:
                juxImg.paste(img, (w * i, 0))
                i += 1
        else:
            juxImg = Image.new('RGB', (w, newH))
            while i < n:
                juxImg.paste(img, (0, h * i))
                i += 1
        return numpy.array(juxImg)

    def mosaic(self, arr, dim):
        img = Image.fromarray(arr)
        w, h = img.size
        newW = w * dim[0]
        newH = h * dim[1]
        i = 0
        j = 0
        mosaicImg = Image.new(
            'RGB', (newW, newH))
        while j < dim[1]:
            while i < dim[0]:
                mosaicImg.paste(img, (w * j, h * i))
                i += 1
            i = 0
            j += 1
        return numpy.array(mosaicImg)


img = ImageProcessor()
item = ScrapBooker()
array = img.load("../resources/42AI.png")
# array = item.mosaic(array, (10, 10))
# array = item.crop(array, (100, 100))
array = item.juxtapose(array, 8, 1)
img.display(array)
