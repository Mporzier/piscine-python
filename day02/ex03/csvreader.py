

class CsvReader():
    def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.name = name

    def getData(self):
        content = self.file.read().split('\n')
        array = []
        for i in content:
            array.append(i.split(self.sep))
        return array

    def getHeader(self):
        header = self.file.readline()
        return header

    def printData(self, data):
        for i in data:
            print(i, '\n')

    def __enter__(self):
        self.file = open(self.name, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getData()
        header = file.getHeader()
        file.printData(data)
