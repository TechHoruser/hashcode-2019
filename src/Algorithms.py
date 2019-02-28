from scipy import spatial
from src.Entities import *
from collections import deque, namedtuple
import pandas as pd
import numpy as np

class BaseAlgorithms:

    @classmethod
    def basic(cls, input:Stage) -> OutputCollection:
        # TODO
        output = ... # type: OutputCollection

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


class UtilGraph:

    # we'll use infinity as a default distance to nodes.
    inf = float('inf')
    Edge = namedtuple('Edge', 'start, end, cost')

    @classmethod
    def make_edge(cls, start, end, cost=1):
        return cls.Edge(start, end, cost)

    @classmethod
    def createFullConnected(cls, nodes):
        edges = []
        for nodeOrigin in nodes:
            for nodeDestination in nodes:
                if nodeOrigin.id != nodeDestination.id:  # no se tiene en cuenta camnios a si mismo, si se tienen en cuenta camino de ida y vuelta
                    edges.append((nodeOrigin.id, nodeDestination.id, Utils.calculateDistance(nodeOrigin.coordinate, nodeDestination.coordinate, "euclidean")))
        return UtilGraph(nodes, edges)

    def __init__(self, nodes, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [self.make_edge(*edge) for edge in edges]
        self.nodes = nodes

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(self.Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(self.Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: self.inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == self.inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

    def todosNodosConectados(self, nodos, nodosConectados):
        for nodo in nodos:
            if nodo.id not in nodosConectados:
                return False
        return True

    def caminosMinimos(self):
        nodesConnected = []
        finalEdges = []
        edgesDataframe = pd.DataFrame(data=self.edges, columns=['idOrigen', 'idDestino', 'distancia'])
        while not self.todosNodosConectados(self.nodes, nodesConnected):
            minIndex = np.argmin(edgesDataframe['distancia'].values)
            if edgesDataframe['idOrigen'][minIndex] not in nodesConnected:
                nodesConnected.append(edgesDataframe['idOrigen'][minIndex])
            if edgesDataframe['idDestino'][minIndex] not in nodesConnected:
                nodesConnected.append(edgesDataframe['idDestino'][minIndex])
            finalEdges.append((edgesDataframe['idOrigen'][minIndex], edgesDataframe['idDestino'][minIndex],
                               edgesDataframe['distancia'][minIndex]))
            edgesDataframe = edgesDataframe.drop(minIndex)
        return finalEdges

