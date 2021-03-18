import abc
import numpy as np


class Graph(abc.ABC):
    def __init__(self, numVertices, directed = False): # assuming by default graph is undirected
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod # needs to be implemented by any class and derives from class Graph(abc.ABC)
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v): # retrieves any adjacent vertices
        pass

    @abc.abstractmethod
    def get_indegree(self, v): # gets number of edges inserted in a vertex
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2): # gets weights of edges
        pass

    @abc.abstractmethod
    def display(self):
        pass

class AdjacencyMatrixGraph(Graph):
    
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices)) # initalize all items in matrix to 0

    def add_edge(self, v1, v2, weight=1):
        # checks if numbers passed in are valid
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] == weight # if an edge exists, entry is equal to weight

        if self.directed == False:
            self.matrix[v2][v1] = weight # allows the path in the other direction is there too

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices): # iterate through all nodes in adjacency matrix
            if self.matrix[v][i] > 0: # if there is a non-zero in any cell then that entry is adjacent
                adjacent_vertices.append(i) # append adjacent vertices to list of adjacent vertices
        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0: # if incoming edge is greater than zero, increment indegree
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


if __name__ == '__main__':
    g = AdjacencyMatrixGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    for i in range(4):
        print("Adjacent to:", i, g.get_adjacent_vertices(i))

    for i in range(4):
        print("Indegree ", i, g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge weight:", i, " ", j, "weight: ", g.get_edge_weight(i, j))

    g.display()
