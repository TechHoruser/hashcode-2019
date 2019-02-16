import numpy

class ManagerFile:
    def __init__(self, fileName):
        self.__fileName = fileName

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
