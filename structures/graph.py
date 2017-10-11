import random
import copy


class Graph:
    class Vertex:
        def __init__(self, vid, x):
            self.__id = vid
            self.__data = x
            self.__discovered = False

        def set_discovered(self, val):
            self.__discovered = val

        def get_discovered(self):
            return self.__discovered

        def data(self):
            return self.__data

        def __hash__(self):
            return hash(id(self))

        def __repr__(self):
            return "id: {}".format(self.__id)

        def __str__(self):
            return "id: {}".format(self.__id)

    class Edge:
        def __init__(self, u, v, x):
            self.__start = u
            self.__end = v
            self.__data = x

        def __hash__(self):
            return hash((self.__start, self.__end))

        def opposite(self, v):
            return self.__end if v is self.__end else self.__start

        def __repr__(self):
            return "id: {}".format(self.__id)

        def __str__(self):
            return "({}, {}) data: {}".format(self.__start, self.__end, self.__data)

    def __init__(self, directed=False):
        self.__outgoing = {}
        self.__incoming = {} if directed else self.__outgoing

    def outgoing(self):
        return self.__outgoing

    def insert_vertex(self, id, x=None):
        v = self.Vertex(id, x)
        node_map = {v: {}}
        # map[v] = {}
        for u, vmap in self.__outgoing.items():
            # initialize the new node's map that has as
            # keys all the nodes in the current outgoing map
            node_map[u] = {}
            # set the new node as a key for itself
            # set the new node as a key for all the existing nodes
            vmap[v] = {}

        self.__outgoing[v] = node_map

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
            g.insert_vertex(i + 1, 'oo')

        for u, vmap in g.outgoing().items():
            num_conn = 0
            insert_extra_edge = False
            while num_conn < min_conn or (insert_extra_edge and num_conn < max_conn):
                available = list(g.outgoing())
                v = random.choice(available)
                has_edge = bool(g.outgoing()[u][v])
                v_is_u = v is u
                # Make sure new node is not itself and there
                # is no edge bw new node and v
                while v_is_u or has_edge:
                    v = random.choice(available)
                    v_is_u = v is u
                    has_edge = bool(g.outgoing()[u][v])

                w = random.randint(1, max_weight)
                g.insert_edge(u, v, w)
                num_conn += 1
                insert_extra_edge = random.randint(0, 100) < add_edge * 100

    @staticmethod
    def is_connected(g):
        u = random.choice(list(g.outgoing()))
        GraphTool.breadth_first_traversal(g, u, lambda *args: None)
        for u, vmap in g.outgoing().items():
            for v in vmap.items():
                if v[0].get_discovered() is False:
                    return False

        return True

    @staticmethod
    def breadth_first_traversal(g, s, f):
        ''' g = graph
            s = source node
            f = function to run while traversing graph '''
        f(s)
        s.set_discovered(True)
        to_visit_queue = [s]
        while to_visit_queue:
            u = to_visit_queue.pop(0)
            f(u)
            neighbors = g.outgoing()[u]
            for v in neighbors:
                if v.get_discovered() is False:
                    v.set_discovered(True)
                    to_visit_queue.append(v)

    @staticmethod
    def print_graph_matrix_sequentially(g):
        for u, vmap in g.outgoing().items():
            for v, e, in vmap.items():
                print(u, v, e)

    @staticmethod
    def dijkstras(s, f):
        pass

    @staticmethod
    def relax_node():
        pass

