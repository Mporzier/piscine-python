import pandas


class FileLoader():
    def load(self, path):
        data = pandas.read_csv(path)
        print("Loading dataset of dimensions",
              data.shape[0], 'x', data.shape[1])
        return data

    def display(self, df, n):
        if n < 0:
            print(df.tail(-n))
        else:
            print(df.head(n))
