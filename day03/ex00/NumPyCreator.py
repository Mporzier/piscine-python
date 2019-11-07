import numpy


class NumPyCreator():
    def from_list(self, lst):
        return numpy.asarray(lst)

    def from_tuple(self, tpl):
        return numpy.asarray(tpl)

    def from_iterable(self, itr):
        return numpy.asarray(itr)

    def from_shape(self, shape, value=0):
        return numpy.full(shape, value)

    def random(self, shape):
        return numpy.random.random_sample(shape)

    def identity(self, n):
        return numpy.identity(n)
