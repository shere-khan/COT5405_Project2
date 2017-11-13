import random
import string

import heap


class Vertex:
    def __init__(self, vid, x):
        self.__id = vid
        self.__object_id = id(self)
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
        return (self.__start == other.get_start() and self.get_end() == other.get_end()) \
               or (self.__start == other.get_end() and self.__end == other.get_start()) and (
            self.__data == other.get_data())


class Graph:
    def __init__(self, directed=False):
        self.__outgoing = {}
        self.__incoming = {} if directed else self.__outgoing

    def outgoing(self):
        return self.__outgoing

    def is_directed(self):
        return self.__incoming is not self.__outgoing

    def insert_vertex_object(self, v):
        node_map = {v: {}}
        for u, vmap in self.__outgoing.items():
            # initialize the new node's map that has as
            # keys all the nodes in the current outgoing map
            node_map[u] = {}
            # set the new node as a key for itself
            # set the new node as a key for all the existing nodes
            vmap[v] = {}

        self.__outgoing[v] = node_map

        if self.is_directed():
            for u, vmap in self.__incoming.items():
                # initialize the new node's map that has as
                # keys all the nodes in the current outgoing map
                node_map[u] = {}
                # set the new node as a key for itself
                # set the new node as a key for all the existing nodes
                vmap[v] = {}

        return v

    def insert_vertex(self, v_id, x=None):
        v = Vertex(v_id, x)
        node_map = {v: {}}
        for u, vmap in self.__outgoing.items():
            # initialize the new node's map that has as
            # keys all the nodes in the current outgoing map
            node_map[u] = {}
            # set the new node as a key for itself
            # set the new node as a key for all the existing nodes
            vmap[v] = {}

        self.__outgoing[v] = node_map

        node_map = {v: {}}
        if self.is_directed():
            for u, vmap in self.__incoming.items():
                # initialize the new node's map that has as
                # keys all the nodes in the current outgoing map
                node_map[u] = {}
                # set the new node as a key for itself
                # set the new node as a key for all the existing nodes
                vmap[v] = {}

        self.__incoming[v] = node_map

        return v

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self.__outgoing[u][v] = e
        self.__incoming[v][u] = e

        return e

    def insert_edge_object(self, e):
        u = e.get_start()
        v = e.get_end()
        try:
            self.__outgoing[u][v] = e
            self.__incoming[v][u] = e
        except KeyError as er:
            print('Invalid key')

        return e

    def adjacent_edges(self, v, outgoing=True):
        adj = self.__outgoing if outgoing else self.__incoming
        for edge in adj[v].values():
            if edge:
                yield edge

    def adjacent_nodes(self, v, outgoing=True):
        l = []
        adj = self.__outgoing if outgoing else self.__incoming
        for u, edge in adj[v].items():
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
    def dfs(g, s, t, capacity, flow):
        stk = [s]
        paths = {s:[]}
        if s is t:
            return paths[s]
        while stk:
            u = stk.pop()
            for e in g.adjacent_edges(u):
                v = e.get_end()
                if capacity[e] - flow[e] > 0 and v not in paths:
                    paths[v] = paths[u] + [(u, v)]
                    print(paths)
                    if v is t:
                        return paths[v]
                    stk.append(v)


    @staticmethod
    def create_hardcoded_maxflow_graph(g, v_map, l):
        for i in range(1, 9):
            v = g.insert_vertex(i, "oo")
            v_map[i] = v

        v = g.insert_edge(v_map[1], v_map[2], 10)
        l.append(v)
        v = g.insert_edge(v_map[1], v_map[3], 5)
        l.append(v)
        v = g.insert_edge(v_map[1], v_map[4], 15)
        l.append(v)

        v = g.insert_edge(v_map[2], v_map[5], 9)
        l.append(v)
        v = g.insert_edge(v_map[2], v_map[6], 15)
        l.append(v)
        v = g.insert_edge(v_map[2], v_map[3], 4)
        l.append(v)

        v = g.insert_edge(v_map[3], v_map[6], 8)
        l.append(v)
        v = g.insert_edge(v_map[3], v_map[4], 4)
        l.append(v)

        v = g.insert_edge(v_map[4], v_map[7], 30)
        l.append(v)

        v = g.insert_edge(v_map[5], v_map[8], 10)
        l.append(v)
        v = g.insert_edge(v_map[5], v_map[6], 15)
        l.append(v)

        v = g.insert_edge(v_map[6], v_map[8], 10)
        l.append(v)
        v = g.insert_edge(v_map[6], v_map[7], 15)
        l.append(v)

        v = g.insert_edge(v_map[7], v_map[8], 10)
        l.append(v)
        v = g.insert_edge(v_map[7], v_map[3], 6)
        l.append(v)

    @staticmethod
    def create_hardcoded_undirected_graph(g, v_map, l):
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

        v = g.insert_edge(v_map['H'], v_map['I'], 19)
        l.append(v)

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
    def mst(g):
        return GraphTool.__kruskals(g)

    @staticmethod
    def __kruskals(g):
        t = []
        uf = UnionFind()
        tot_w = 0
        for v in g.get_all_vertices():
            uf.make_set(v, lambda x: x.get_id())
        edges = g.get_all_edges_list()
        h = heap.Heap(lambda x, y: x.get_data() < y.get_data())
        list(map(lambda x: h.insert(x), edges))
        print()
        print("Heap array after heapify:")
        print(h.get_data())
        print()
        print("Heap array after sort:")
        for i in range(h.size()):
            e = h.dequeue()
            print('{}, '.format(e), end='')
            u = e.get_start()
            v = e.get_end()
            u_set = uf.find_set(u)
            v_set = uf.find_set(v)
            if u_set is not v_set:
                tot_w += e.get_data()
                t.append(e)
                uf.join(u, v)

        print()
        return t, tot_w

    @staticmethod
    def unpack_kruskal(t):
        nodeset = set()
        edgeset = set()
        for e in t:
            edgeset.add(e.get_end().get_id() + '-' + e.get_start().get_id())
            nodeset.add(e.get_end().get_id())
            nodeset.add(e.get_start().get_id())
        return list(nodeset), list(edgeset)

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


class UnionFind:
    class Node:
        def __init__(self, nid):
            self.__parent = self
            self.__level = 0
            self.__nid = nid

        def get_level(self):
            return self.__level

        def set_level(self, lvl):
            self.__level = lvl

        def set_parent(self, o):
            self.__parent = o

        def get_parent(self):
            return self.__parent

        def get_nid(self):
            return self.__nid

        def __eq__(self, other):
            return self.__nid == other.get_nid() and self.__level == other.get_level()

    def get_node(self, o):
        return self.__data[o]

    def __init__(self):
        self.__data = {}

    def find_set(self, o):
        a = self.__data[o]
        if a.get_parent() is a:
            return a
        else:
            val = self.__find_set(a.get_parent(), [a])
            return val

    def __find_set(self, a, l):
        if a.get_parent() is a:
            for n in l:
                n.set_parent(a)

            return a
        else:
            l.append(a)
            return self.__find_set(a.get_parent(), l)

    def join(self, n, o):
        a = self.find_set(n)
        b = self.find_set(o)

        if a.get_level() < b.get_level():
            a.set_parent(b)
            a.set_level(0)
            b.set_level(b.get_level() + 1)
        else:  # case if a.level >= b.level
            b.set_parent(a)
            b.set_level(0)
            a.set_level(a.get_level() + 1)

    def make_set(self, a, f):
        self.__data[a] = self.Node(f(a))
