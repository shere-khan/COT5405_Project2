import random
import string

from structures import heap


class Vertex:
    def __init__(self, vid, x):
        self.__id = vid
        self.__data = x
        self.__discovered = False

    def get_id(self):
        return self.__id

    def set_id(self, v_id):
        self.__id = v_id

    def set_discovered(self, val):
        self.__discovered = val

    def get_discovered(self):
        return self.__discovered

    def get_data(self):
        return self.__data

    def set_data(self, val):
        self.__data = val

    def __hash__(self):
        return hash(id(self))

    def __repr__(self):
        return "id: {} data: {}".format(self.__id, self.__data)

    def __str__(self):
        return "id: {} data: {}".format(self.__id, self.__data)

    def __eq__(self, other):
        return self.get_data() == other.get_data() and self.get_id() == other.get_id()


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
        return "({}, {}) data: {}".format(self.__start, self.__end, self.__data)

    def __str__(self):
        return "({}, {}) data: {}".format(self.__start, self.__end, self.__data)

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_data(self):
        return self.__data

    def __eq__(self, other):
        return (self.__start == other.get_start()) \
               and (self.get_end() == other.get_end()) \
               and (self.__data == other.get_data())


class Graph:
    def __init__(self, directed=False):
        self.__outgoing = {}
        self.__incoming = {} if directed else self.__outgoing

    def outgoing(self):
        return self.__outgoing

    def insert_vertex(self, v_id, x=None):
        v = Vertex(v_id, x)
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
        e = Edge(u, v, x)
        self.__outgoing[u][v] = e
        self.__incoming[v][u] = e

        return e

    def adjacent_edges(self, v):
        for edge in self.__outgoing[v].values():
            if edge:
                yield edge

    def adjacent_nodes(self, v):
        l = []
        for u, edge in self.__outgoing[v].items():
            if edge:
                l.append(u)

        return l

    def get_all_edges(self):
        for u, vmap in self.__outgoing.items():
            for v, edge in vmap.items():
                yield edge

    def get_all_edges_list(self):
        l = set()
        for u, vmap in self.__outgoing.items():
            for v, edge in vmap.items():
                if edge:
                    l.add(edge)
        return list(l)

    def get_all_vertices(self):
        l = set()
        for u in self.__outgoing.items():
            l.add(u[0])
        return list(l)


class GraphTool:
    @staticmethod
    def create_hardcoded_graph(g, v_map, l):
        for i in string.ascii_uppercase[:9]:
            v = g.insert_vertex(i, "oo")
            v_map[i] = v

        v = g.insert_edge(v_map['A'], v_map['B'], 22)
        l.append(v)
        v = g.insert_edge(v_map['A'], v_map['C'], 9)
        l.append(v)
        v = g.insert_edge(v_map['A'], v_map['D'], 12)
        l.append(v)

        v = g.insert_edge(v_map['B'], v_map['C'], 35)
        l.append(v)
        v = g.insert_edge(v_map['B'], v_map['F'], 36)
        l.append(v)
        v = g.insert_edge(v_map['B'], v_map['H'], 34)
        l.append(v)

        v = g.insert_edge(v_map['C'], v_map['D'], 4)
        l.append(v)
        v = g.insert_edge(v_map['C'], v_map['E'], 65)
        l.append(v)
        v = g.insert_edge(v_map['C'], v_map['F'], 42)
        l.append(v)

        v = g.insert_edge(v_map['D'], v_map['E'], 33)
        l.append(v)
        v = g.insert_edge(v_map['D'], v_map['I'], 30)
        l.append(v)

        v = g.insert_edge(v_map['E'], v_map['F'], 18)
        l.append(v)
        v = g.insert_edge(v_map['E'], v_map['G'], 23)
        l.append(v)

        v = g.insert_edge(v_map['F'], v_map['G'], 39)
        l.append(v)
        v = g.insert_edge(v_map['F'], v_map['H'], 24)
        l.append(v)

        v = g.insert_edge(v_map['G'], v_map['H'], 25)
        l.append(v)
        v = g.insert_edge(v_map['G'], v_map['I'], 21)
        l.append(v)

        v = g.insert_edge(v_map['E'], v_map['I'], 19)
        l.append(v)

        return g


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
        """

        :param g: graph
        :param s: source node
        :param f: function to run while traversing graph

        :return:
        """

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
    def __dijkstras(g, s):
        """
        :param g: graph
        :param s: source node
        :return:

        """
        prev = {}
        visited = {}
        for u, vmap in g.outgoing().items():
            prev[u] = None
            visited[u] = False
            u.set_data('oo')
        s.set_data(0)
        q = heap.Heap(lambda x, y: x.get_data() < y.get_data())
        q.insert(s)
        while q.size():
            u = q.dequeue()
            visited[u] = True
            adj = g.adjacent_nodes(u)
            for v in adj:
                node = g.outgoing()[u][v]
                d = node.get_data()
                alt = u.get_data() + d
                if v.get_data() == 'oo' or alt < v.get_data() and not visited[v]:
                    v.set_data(alt)
                    prev[v] = u
                    q.insert(v)

        return prev

    @staticmethod
    def shortest_path(g, s, d):
        """

        :param g: graph
        :param s: source node
        :param d: destination node
        :return: returns string representing the shortest s-d path
        """

        prev = GraphTool.__dijkstras(g, s)
        shortest = GraphTool.unpack_paths(s, d, prev)

        return shortest


    @staticmethod
    def unpack_paths(s, d, prev):
        """

        :param g: graph
        :param s: source node
        :param prev: the array representing shortest paths. The key is a node u, the value is the neighboring node v
        such that the weight of edge (u,v) is the smallest out of all possible neighbors v
        :return: recurses over the dictionary prev and returns a concatenated string of the shortest s-d path

        """
        if prev[d] is None:
            return d.get_id()
        return GraphTool.unpack_paths(s, prev[d], prev) + " -> " + d.get_id()
