import random
import string
import unittest

from structures import heap, graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.h = heap.Heap()
        self.p = lambda x, y: x.data() < y.data()

        g = graph.Graph()
        v_map = {}
        for i in string.ascii_uppercase[:9]:
            v = g.insert_vertex(i, "oo")
            v_map[i] = v

        # A-edges
        g.insert_edge(v_map['A'], v_map['B'], 22)
        g.insert_edge(v_map['A'], v_map['C'], 9)
        g.insert_edge(v_map['A'], v_map['D'], 12)

        # B-edges
        g.insert_edge(v_map['B'], v_map['C'], 35)
        g.insert_edge(v_map['B'], v_map['F'], 36)
        g.insert_edge(v_map['B'], v_map['H'], 34)

        # C-edges
        g.insert_edge(v_map['C'], v_map['D'], 4)
        g.insert_edge(v_map['C'], v_map['E'], 65)
        g.insert_edge(v_map['C'], v_map['F'], 42)

        # D-edges
        g.insert_edge(v_map['D'], v_map['E'], 33)
        g.insert_edge(v_map['D'], v_map['I'], 30)

        # E-edges
        g.insert_edge(v_map['E'], v_map['F'], 18)
        g.insert_edge(v_map['E'], v_map['G'], 23)

        # F-edges
        g.insert_edge(v_map['F'], v_map['G'], 39)
        g.insert_edge(v_map['F'], v_map['H'], 24)

        # G-edges
        g.insert_edge(v_map['G'], v_map['H'], 25)
        g.insert_edge(v_map['G'], v_map['I'], 21)

        # H-edges

        # I-edges
    def test_heap_size_one(self):
        pass

    def test_insert(self):
        heapsize = 10
        l = []
        for i in range(heapsize):
            val = random.randint(1, 50)
            node = graph.Vertex(i, val)
            l.append(node)
            # lambda predicate < for a min heap
            self.h.insert(node, self.p)

        l.sort(key=lambda x: x.data())
        r = []
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_middle_of_tree_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(2, lambda x: x.set_data(8), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_middle_of_tree_heapify_up(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(2, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_root_of_tree_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(0, lambda x: x.set_data(32), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_root_of_tree_nothing(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(0, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_node_has_left_child_only_heapify_up(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(3, lambda x: x.set_data(1), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_node_has_left_child_only_heapify_down(self):
        l = [graph.Vertex(0, 3), graph.Vertex(1, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(4, 9),
             graph.Vertex(5, 7), graph.Vertex(6, 29), graph.Vertex(7, 13)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, self.p)

        self.h.change_key(3, lambda x: x.set_data(32), self.p)
        l.sort(key=lambda x: x.data())
        for i in range(len(l)):
            v1 = self.h.dequeue(self.p)
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_list_of_one(self):
        v = graph.Vertex(0, 3)
        self.h.insert(v, self.p)
        self.h.change_key(0, lambda x: x.set_data(32), self.p)
        x = self.h.dequeue(self.p)
        self.assertEqual(graph.Vertex(0, 32), x)


if __name__ == '__main__':
    unittest.main()
