import numpy

class ManagerFile:
    def __init__(self, fileName):
        self.__fileName = fileName

    def simpleLoadFile(self, separator = ' '):
        with open('../data/in/'+self.__fileName + '.txt') as f:
            content = f.readlines()

        return [(line.replace("\n",'')).split(separator) for line in content]



    def loadStringFile(self):
        return numpy.genfromtxt(
            '../data/in/'+self.__fileName + '.in',
            delimiter=1,
            skip_header=1,
            dtype=str,
        )

    def loadFile(self):
        return numpy.loadtxt(
            '../data/in/'+self.__fileName + '.in',
            # comments="#",
            # delimiter=",",
            skiprows=0,
            dtype=int,
        )

    def saveFile(self, data):
        return numpy.savetxt(
            '../data/out/'+self.__fileName + '.out',
            X=data,
            delimiter=" ",
            fmt="%s",
        )

    def saveStringFile(self, outputString):
        text_file = open('../data/out/'+self.__fileName + '.out', "w")
        text_file.write(outputString)
        text_file.close()
