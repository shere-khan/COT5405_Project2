import random
import string
import unittest

from structures import heap, graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.p = lambda x, y: x.get_data() < y.get_data()
        self.h = heap.Heap(self.p)

    def test_insert(self):
        heapsize = 10
        l = []
        for i in range(heapsize):
            val = random.randint(1, 50)
            node = graph.Vertex(i, val)
            l.append(node)
            # lambda predicate < for a min heap
            self.h.insert(node, self.p)

        l.sort(key=lambda x: x.get_data())
        r = []
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_middle_of_tree_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(2, lambda x: x.set_data(8), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_middle_of_tree_heapify_up(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(2, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_root_of_tree_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(0, lambda x: x.set_data(32), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_root_of_tree_nothing(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(0, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_node_has_left_child_only_heapify_up(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(3, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_node_has_left_child_only_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(3, lambda x: x.set_data(32), self.p)
        l.sort(key=lambda x: x.get_data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.get_data(), v2.get_data())

    def test_change_key_list_of_one(self):
        v = graph.Vertex(0, 3)
        self.h.insert(v, self.p)
        self.h.change_key(0, lambda x: x.set_data(32), self.p)
        x = self.h.dequeue(self.p)
        self.assertEqual(graph.Vertex(0, 32), x)

    def test_edge_sort_on_project_graph(self):
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

        for e in self.g.get_all_edges_list():
            if e:
                self.h.insert(e, lambda x, y: x.get_data() < y.get_data())

        l.sort(key=lambda y: y.get_data())
        h = []
        for i in range(self.h.size()):
            r = self.h.dequeue(lambda x, y: x.get_data() < y.get_data())
            h.append(r)

        self.assertEqual(h, l)

if __name__ == '__main__':
    unittest.main()
