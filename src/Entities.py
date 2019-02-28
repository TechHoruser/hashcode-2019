class Coordinate:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def getArray(self):
        returnedArray = []
        for property, value in vars(self).items():
            if value is not None:
                returnedArray.append(value)

        return returnedArray

class Node:
    def __init__(self, id, coordinate):
        self.id = id
        self.coordinate = coordinate


class InputElementsCollection:
    def __init__(self):
        None

class OutputElementCollection:
    def __init__(self):
        None
