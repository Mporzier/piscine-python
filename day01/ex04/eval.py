import sys


class Evaluator:
    def __init__(self, coefs, words):
        self.coefs = coefs
        self.words = words

    def zip_evaluate(self, coefs, words):
        if len(coefs) != len(words):
            return -1

    def enumerate_evaluate(self, coefs, words):
        if len(coefs) != len(words):
            return -1


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
e = Evaluator(words, coefs)
print(e.zip_evaluate(coefs, words))
