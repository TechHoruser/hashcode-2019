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

class Stage:
    def __init__(self):
        self.drones = []
        self.warehouses = []
        self.orders = []

class Product:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

class Drone:
    MAX_WEIGHT = 1

    def __init__(self, id, coordinate):
        self.id = id
        self.coordinate = coordinate
        self.actualWeight = 0
        self.products = []
        self.working = 0

    def addProducts(self, products):
        weightOfProducts = sum([product.weight for product in products])
        if self.actualWeight + weightOfProducts > Drone.MAX_WEIGHT:
            raise Exception('Peso maximo del dron '+str(self.id)+' superado')

        self.products.extend(products)
        self.actualWeight += weightOfProducts

class Warehouse:
    def __init__(self, id, coordinate, products = []):
        self.id = id
        self.coordinate = coordinate
        self.products = products

    def addProducts(self, products):
        self.products.extend(products)

    def rmProducts(self, products):
        self.products = [product for product in self.products if product.id not in products]

class Order:
    def __init__(self, id, coordinate, products = []):
        self.id = id
        self.coordinate = coordinate
        self.products = products
        self.done = False