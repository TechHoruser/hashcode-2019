from time import sleep
from src.ManagerFile import ManagerFile
from src.Entities import *
from src.Algorithms import BaseAlgorithms


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

    productsList = []
    warehouseList = []
    orderList = []

    for idx, val in enumerate(lines):
        if idx == 0:
            dronesNumber = val[2]
            maxTime = val[3]
            maxWeight = val[4]
            continue

        if idx == 1:
            continue

        if idx == 2:
            for productIndex, weight in enumerate(val):
                productsList[productIndex] = Product(productIndex, weight)
            continue

        if warehouseFounded is False:
            numberWarehouse = val[0]
            idxWarehouse = 0
            lineWarehouse = 0
            warehouseFounded = True
            continue

        if idxWarehouse < numberWarehouse:
            if lineWarehouse == 0:
                coordinate = Coordinate(val[0], val[1])
            elif lineWarehouse == 1:
                warehouse = Warehouse(idxWarehouse, coordinate)
                for idxProduct, productCount in val:
                    warehouse.addProducts([productsList[idxProduct] for x in range(productCount)])
                warehouseList[idxWarehouse] = warehouse

            lineWarehouse += 1
            if lineWarehouse == linesByWarehouse:
                idxWarehouse += 1
            lineWarehouse = lineWarehouse % linesByWarehouse
            continue

        if orderFounded is False:
            numberOrder = val[0]
            idxOrder = 0
            lineOrder = 0
            orderFounded = True
            continue

        if idxOrder < numberOrder:
            if lineOrder == 0:
                coordinate = Coordinate(val[0], val[1])
            elif lineOrder == 2:
                order = Order(idxOrder, coordinate)
                for idxProduct, productCount in val:
                    order.addProducts([productsList[idxProduct]])
                orderList[idxOrder] = order

            lineOrder += 1
            if lineOrder == linesByOrder:
                idxOrder += 1
            lineOrder = lineOrder % linesByOrder
            continue



for indx, example in enumerate(examples):
    print('Processing file:',example['fileName'],'('+str(indx+1)+'/'+str(len(examples))+')', flush=False)
    mf = ManagerFile(example['fileName'])
    inputArray = mf.simpleLoadFile()

    stage = transformInputArray(inputArray)

    solution = eval('BaseAlgorithms.'+example['algorithm']+'(inputArray)')

    outputArray = solution

    mf.saveFile(outputArray)

    sleep(0.5)

