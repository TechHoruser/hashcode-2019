from time import sleep
from src.ManagerFile import ManagerFile
from src.Algorithms import BaseAlgorithms, Utils, UtilGraph
from src.Entities import *

examples = [
    {'fileName': 'busy_day', 'algorithm': 'basic', },
    {'fileName': 'mother_of_all_warehouses', 'algorithm': 'basic', },
    {'fileName': 'redundancy', 'algorithm': 'basic', },
]

def transformInputArray(lines):
    warehouseFounded = False
    orderFounded = False

    linesByWarehouse = 2
    linesByOrder = 3

    dronesList = {}
    productsList = {}
    warehouseList = {}
    orderList = {}

    for idx, val in enumerate(lines):
        if idx == 0:
            dronesNumber = int(val[2])
            maxTime = int(val[3])
            maxWeight = int(val[4])
            continue

        if idx == 1:
            continue

        if idx == 2:
            for productIndex, weight in enumerate(val):
                productsList[productIndex] = Product(productIndex, weight)
            continue

        if warehouseFounded is False:
            numberWarehouse = int(val[0])
            idxWarehouse = 0
            lineWarehouse = 0
            warehouseFounded = True
            continue

        if idxWarehouse < numberWarehouse:
            if lineWarehouse == 0:
                coordinate = Coordinate(val[0], val[1])
            elif lineWarehouse == 1:
                warehouse = Warehouse(idxWarehouse, coordinate)
                for idxProduct, productCount in enumerate(val):
                    warehouse.addProducts([productsList[idxProduct] for x in range(int(productCount))])
                warehouseList[idxWarehouse] = warehouse

            lineWarehouse += 1
            if lineWarehouse == linesByWarehouse:
                idxWarehouse += 1
            lineWarehouse = lineWarehouse % linesByWarehouse
            continue

        if orderFounded is False:
            numberOrder = int(val[0])
            idxOrder = 0
            lineOrder = 0
            orderFounded = True
            continue

        if idxOrder < numberOrder:
            if lineOrder == 0:
                coordinate = Coordinate(val[0], val[1])
            elif lineOrder == 2:
                order = Order(idxOrder, coordinate)
                for idxProduct, productCount in enumerate(val):
                    order.addProducts([productsList[idxProduct]])
                orderList[idxOrder] = order

            lineOrder += 1
            if lineOrder == linesByOrder:
                idxOrder += 1
            lineOrder = lineOrder % linesByOrder
            continue

    for x in range(dronesNumber):
        dronesList[x] = Drone(id, maxWeight, warehouseList[0].coordinate)

    return Stage(maxTime, productsList, dronesList, warehouseList, orderList)


for indx, example in enumerate(examples):
    print('Processing file:',example['fileName'],'('+str(indx+1)+'/'+str(len(examples))+')', flush=False)
    mf = ManagerFile(example['fileName'])
    inputArray = mf.simpleLoadFile()

    stage = transformInputArray(inputArray)

    solution = eval('BaseAlgorithms.'+example['algorithm']+'(inputArray)')

    outputArray = solution

    mf.saveFile(outputArray)

    sleep(0.5)

nodes = [
    Node(1, Coordinate(1, 1)),
    Node(2, Coordinate(4, 5)),
    Node(3, Coordinate(2, 1)),
    Node(4, Coordinate(9, 2)),
    Node(5, Coordinate(4, 8))
]

edges = []
for nodeOrigin in nodes:
    for nodeDestination in nodes:
        if nodeOrigin.id != nodeDestination.id:  # no se tiene en cuenta camnios a si mismo, si se tienen en cuenta camino de ida y vuelta
            edges.append((nodeOrigin.id, nodeDestination.id, Utils.calculateDistance(nodeOrigin.coordinate, nodeDestination.coordinate, "euclidean")))

graph1 = UtilGraph(nodes, edges)
graph2 = UtilGraph.createFullConnected(nodes)
print(graph1.dijkstra(1, 2))
print(graph2.dijkstra(1, 2))
print(graph1.caminosMinimos())
print(graph2.caminosMinimos())