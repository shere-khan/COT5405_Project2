import unittest

from structures import graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.v_map = {}
        self.g = graph.Graph()
        self.l = []
        graph.GraphTool.create_hardcoded_graph(self.g, self.v_map, self.l)

    def test_shortest_path(self):
        self.g.outgoing()
        path = graph.GraphTool.shortest_path(self.g, self.v_map['A'], self.v_map['E'])
        self.assertEqual("A -> D -> E", path)

    def test_unpack_paths(self):
        v1 = graph.Vertex('A', 3)
        v2 = graph.Vertex('B', 4)
        v3 = graph.Vertex('C', 5)
        v4 = graph.Vertex('D', 2)

        prev = {v4: v3, v3: v2, v2: v1, v1: None}

        path = graph.GraphTool.unpack_paths(v1, v4, prev)

        self.assertEqual("A -> B -> C -> D", path)

    def test_union_find_make_set(self):
        pass

    def test_union_find_join(self):
        pass

    def test_union_find_find(self):
        pass


if __name__ == '__main__':
    unittest.main()
