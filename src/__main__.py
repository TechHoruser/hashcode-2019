from time import sleep
from src.ManagerFile import ManagerFile
from src.Algorithms import BaseAlgorithms, Utils, UtilGraph
from src.Entities import Coordinate,Node

examples = [
    {'fileName': 'a_example', 'algorithm': 'basic', },
    {'fileName': 'b_should_be_easy', 'algorithm': 'basic', },
    {'fileName': 'd_metropolis', 'algorithm': 'basic', },
    {'fileName': 'e_high_bonus', 'algorithm': 'basic', },
]

for indx, example in enumerate(examples):
    print('Processing file:',example['fileName'],'('+str(indx+1)+'/'+str(len(examples))+')', flush=False)
    mf = ManagerFile(example['fileName'])
    inputArray = mf.loadFile()

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