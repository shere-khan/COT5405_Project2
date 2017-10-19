import string
import unittest

from structures import graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.g = graph.Graph()
        v_map = {}
        for i in string.ascii_uppercase[:9]:
            v = self.g.insert_vertex(i, "oo")
            v_map[i] = v

        l = []
        v = self.g.insert_edge(v_map['A'], v_map['B'], 22)
        l.append(v)
        v = self.g.insert_edge(v_map['A'], v_map['C'], 9)
        l.append(v)
        v = self.g.insert_edge(v_map['A'], v_map['D'], 12)
        l.append(v)

        v = self.g.insert_edge(v_map['B'], v_map['C'], 35)
        l.append(v)
        v = self.g.insert_edge(v_map['B'], v_map['F'], 36)
        l.append(v)
        v = self.g.insert_edge(v_map['B'], v_map['H'], 34)
        l.append(v)

        v = self.g.insert_edge(v_map['C'], v_map['D'], 4)
        l.append(v)
        v = self.g.insert_edge(v_map['C'], v_map['E'], 65)
        l.append(v)
        v = self.g.insert_edge(v_map['C'], v_map['F'], 42)
        l.append(v)

        v = self.g.insert_edge(v_map['D'], v_map['E'], 33)
        l.append(v)
        v = self.g.insert_edge(v_map['D'], v_map['I'], 30)
        l.append(v)

        v = self.g.insert_edge(v_map['E'], v_map['F'], 18)
        l.append(v)
        v = self.g.insert_edge(v_map['E'], v_map['G'], 23)
        l.append(v)

        v = self.g.insert_edge(v_map['F'], v_map['G'], 39)
        l.append(v)
        v = self.g.insert_edge(v_map['F'], v_map['H'], 24)
        l.append(v)

        v = self.g.insert_edge(v_map['G'], v_map['H'], 25)
        l.append(v)
        v = self.g.insert_edge(v_map['G'], v_map['I'], 21)
        l.append(v)

        v = self.g.insert_edge(v_map['E'], v_map['I'], 19)
        l.append(v)

    def test_dijkstras_algorithm(self):
        pass

    def test_unpack_paths(self):
        v1 = graph.Vertex('A', 3)
        v2 = graph.Vertex('B', 4)
        v3 = graph.Vertex('C', 5)
        v4 = graph.Vertex('D', 2)

        prev = {v4: v3, v3: v2, v2: v1, v1: None}

        path = graph.GraphTool.unpack_paths(v1, v4)

        self.assertEqual("A -> B -> C -> D")

_
if __name__ == '__main__':
    unittest.main()
