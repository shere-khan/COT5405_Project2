import unittest, random
from structures import heap


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.h = heap.Heap()

    def test_heap_size_one(self):
        pass

    def test_insert(self):
        heapsize = 10
        l = []
        for i in range(heapsize):
            val = random.randint(1, 20)
            l.append(val)
            # lambda predicate < for a min heap
            self.h.insert(val, lambda x, y: x < y)

        l.sort()
        r = []
        for i in l:
            r.append(self.h.dequeue())

        self.assertEqual(l, r)


if __name__ == '__main__':
    unittest.main()
