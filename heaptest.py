import unittest, random
from structures import heap, graph


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.h = heap.Heap()

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
            self.h.insert(node, lambda x, y: x.data() < y.data())

        l.sort(key=lambda x: x.data())
        r = []
        for i in range(len(l)):
            v1 = self.h.dequeue(lambda x, y: x.data() < y.data())
            v2 = l[i]
            self.assertEqual(v1.data(), v2.data())

    def test_change_key_full_list(self):
        l = [graph.Vertex(0, 3), graph.Vertex(0, 4),
             graph.Vertex(2, 2), graph.Vertex(3, 8), graph.Vertex(1, 9)]
        for i in l:
            # lambda predicate < for a min heap
            self.h.insert(i, lambda x, y: x.data() < y.data())

        self.h.change_key(2, lambda x: x.set_data(13))
        h_list = []
        for i in range(len(l)):
            h_list.append(self.h.dequeue())
        self.assertEqual([1, 2, 3, 4, 5, 7, 8, 10], h_list)

    def test_change_key_list_of_one(self):
        pass


if __name__ == '__main__':
    unittest.main()
