import random


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

    def __init__(self, directed=False):
        self.__outgoing = {}
        self.__incoming = {} if directed else self.__outgoing

    def outgoing(self):
        return self.__outgoing

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self.__outgoing[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self.__outgoing[u][v] = e
        self.__incoming[v][u] = e

    def adjacent_edges(self, v):
        for edge in self.__outgoing[v].values():
            yield edge


class GraphTool:
    @staticmethod
    def create_connected_graph(g, num_nodes, min_conn, max_conn, max_weight, add_edge=0.1):

        for i in range(num_nodes):
            g.insert_vertex('oo')

        for u, vmap in g.outgoing().items():
            num_conn = 0
            is_new_edge = False
            while num_conn < min_conn or (is_new_edge and num_conn < max_conn):
                x = list(g.outgoing())
                v = None
                while not v:
                    random.choice(x)
                e = vmap[v]
                if e is None:
                    w = random.randint(1, max_weight)
                    g.insert_edge(u, v, w)
                    num_conn += 1
                is_new_edge = random.randint(0, 100) < add_edge * 100
