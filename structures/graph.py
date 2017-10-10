class Graph:
    class Vertex:
        def __init__(self, x):
            self.__data = x

        def data(self):
            return self.__data

        def __hash__(self):
            return hash(id(self))

    class Edge:
        def __init__(self, u, v, x):
            self.__start = u
            self.__end = v
            self.__data = x

        def __hash__(self):
            return hash((self.__start, self.__end))

        def opposite(self, v):
            return self.__end if v is self.__end else self.__start

    def __init__(self):
        self.__matrix = {}

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self.__matrix[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self.__matrix[u][v] = e

    def adjacent_edges(self, v):
        for edge in self.__matrix[v].values():
            yield edge
