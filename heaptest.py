import unittest, random
from structures import heap


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.h = heap.Heap()

    def test_insert(self):
        heapsize = 10
        l = []
        for i in range(heapsize):
            val = random.randint(1, 20)
            l.append(val)
            self.h.insert(val, lambda x, y: x < y)

        l.sort()
        for i in l:
            self.assertEqual(self.h.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
