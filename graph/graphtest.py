import unittest

import graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        # self.v_map = {}
        # self.undirected_g = graph.Graph()
        self.l = []
        # graph.GraphTool.create_hardcoded_undirected_graph(self.undirected_g, self.v_map, self.l)

        self.v_map_directed = {}
        self.directed_g = graph.Graph(directed=True)
        graph.GraphTool.create_hardcoded_maxflow_graph(self.directed_g, self.v_map_directed, self.l)

    # def test_get_edges_directed_graph(self):
    #     edges = self.directed_g.get_all_edges_list()

    def test_dfs_maxflow(self):
        paths = list()

        s = self.v_map_directed[1]
        t = self.v_map_directed[8]

        mf = graph.GraphTool.maxflow(self.directed_g, s, t)

        print('Maxflow is: ' + str(mf))

        # def test_shortest_path(self):
        #     self.undirected_g.outgoing()
        #     path = graph.GraphTool.shortest_path(self.undirected_g, self.v_map['A'], self.v_map['E'])
        #     self.assertEqual("A -> D -> E", path)
        #
        # def test_unpack_paths(self):
        #     v1 = graph.Vertex('A', 3)
        #     v2 = graph.Vertex('B', 4)
        #     v3 = graph.Vertex('C', 5)
        #     v4 = graph.Vertex('D', 2)
        #     prev = {v4: v3, v3: v2, v2: v1, v1: None}
        #
        #     path = graph.GraphTool.unpack_paths(v1, v4, prev)
        #
        #     self.assertEqual("A -> B -> C -> D", path)
        #
        # def test_union_find_make_set(self):
        #     pass
        #
        # def test_union_find_join(self):
        #     uf = graph.UnionFind()
        #     for v in self.undirected_g.get_all_vertices():
        #         uf.make_set(v, lambda x: x.get_id())
        #     a = self.v_map['A']
        #     b = self.v_map['B']
        #     uf.join(a, b)
        #     aprime = uf.find_set(a)
        #     self.assertEqual('A', aprime.get_nid())
        #     bprime = uf.find_set(b)
        #     self.assertEqual('A', bprime.get_nid())
        #
        #     self.assertEqual(0, uf.get_node(b).get_level())
        #     self.assertEqual(1, uf.get_node(a).get_level())
        #
        # def test_union_find_join_level_two_with_level_one(self):
        #     uf = graph.UnionFind()
        #     for v in self.undirected_g.get_all_vertices():
        #         uf.make_set(v, lambda x: x.get_id())
        #     a = self.v_map['A']
        #     b = self.v_map['B']
        #     uf.join(a, b)
        #     aprime = uf.find_set(a)
        #     self.assertEqual('A', aprime.get_nid())
        #     bprime = uf.find_set(b)
        #     self.assertEqual('A', bprime.get_nid())
        #
        #     c = self.v_map['C']
        #     uf.join(c, b)
        #     aprime = uf.find_set(a)
        #     self.assertEqual('A', aprime.get_nid())
        #     bprime = uf.find_set(b)
        #     self.assertEqual('A', bprime.get_nid())
        #     cprime = uf.find_set(c)
        #     self.assertEqual('A', cprime.get_nid())
        #
        #     self.assertEqual(0, uf.get_node(b).get_level())
        #     self.assertEqual(2, uf.get_node(a).get_level())
        #
        # def test_union_find_join_level_3_with_level_2(self):
        #     uf = graph.UnionFind()
        #     for v in self.undirected_g.get_all_vertices():
        #         uf.make_set(v, lambda x: x.get_id())
        #     a = self.v_map['A']
        #     b = self.v_map['B']
        #     uf.join(a, b)
        #     aprime = uf.find_set(a)
        #     self.assertEqual('A', aprime.get_nid())
        #     bprime = uf.find_set(b)
        #     self.assertEqual('A', bprime.get_nid())
        #
        #     c = self.v_map['C']
        #     uf.join(c, b)
        #     aprime = uf.find_set(a)
        #     self.assertEqual('A', aprime.get_nid())
        #     bprime = uf.find_set(b)
        #     self.assertEqual('A', bprime.get_nid())
        #     cprime = uf.find_set(c)
        #     self.assertEqual('A', cprime.get_nid())
        #
        #     self.assertEqual(0, uf.get_node(b).get_level())
        #     self.assertEqual(2, uf.get_node(a).get_level())
        #
        #     d = self.v_map['D']
        #     e = self.v_map['E']
        #     uf.join(d, e)
        #     dprime = uf.find_set(d)
        #     self.assertEqual('D', dprime.get_nid())
        #     eprime = uf.find_set(e)
        #     self.assertEqual('D', eprime.get_nid())
        #
        #     uf.join(c, e)
        #     self.assertEqual('A', uf.find_set(d).get_nid())
        #     eprime = uf.find_set(e)
        #     self.assertEqual('A', eprime.get_nid())
        #
        #     self.assertEqual(3, uf.get_node(a).get_level())
        #     self.assertEqual(0, uf.get_node(b).get_level())
        #     self.assertEqual(0, uf.get_node(c).get_level())
        #     self.assertEqual(0, uf.get_node(d).get_level())
        #     self.assertEqual(0, uf.get_node(e).get_level())
        #
        # def test_union_find_find(self):
        #     uf = graph.UnionFind()
        #     for v in self.undirected_g.get_all_vertices():
        #         uf.make_set(v, lambda x: x.get_id())
        #     a = self.v_map['A']
        #     aprime = uf.find_set(a)
        #     self.assertEqual(a.get_id(), aprime.get_nid())
        #
        # def test_mst(self):
        #     mst = graph.GraphTool.mst(self.undirected_g)
        #     self.assertEqual('a', 'a')


if __name__ == '__main__':
    unittest.main()
