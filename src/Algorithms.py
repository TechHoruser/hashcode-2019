from scipy import spatial
from src.Entities import *

class BaseAlgorithms:

    @classmethod
    def basic(cls, input:InputElementsCollection) -> OutputElementCollection:
        # TODO
        output = ... # type: OutputElementCollection

        return output


class Utils:

    @classmethod
    def selectBranch(cls, inputArray):
        return None

    @classmethod
    def calculateCost(cls, inputArray):
        return None

    @classmethod
    def calculateDistance(cls, coordinate1:Coordinate, coordinate2:Coordinate, distanceType:str='euclidean'):
        if distanceType == 'euclidean':
            return spatial.distance.euclidean(coordinate1.getArray(), coordinate2.getArray())
        elif distanceType == 'manhattan':
            return spatial.distance.cityblock(coordinate1.getArray(), coordinate2.getArray())
        else:
            raise ValueError('Type of distance not allowed')


