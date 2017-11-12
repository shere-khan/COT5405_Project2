import dp
import unittest


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.dynprog = dp.RNA()

    # def test_alignment_no_pointer(self):
    #     s1 = 'AACG'
    #     s2 = 'ACTG'
    #
    #     f = lambda x, y: 1 if y == "" or x == "" or x != y else 0
    #
    #     align = self.dynprog.alignment_no_pointer(s1, s2, f)
    #
    #     print(align[-1][-1])

    def test_alignment(self):
        # s1 = 'AACGD'
        # s2 = 'ACTG'
        # s1 = 'AACGDXXQQQY'
        # s2 = 'ACTGQXCQY'

        s1 = 'AGGCTATCACCTGACCTCCAGGCCGATGCCC'
        s2 = 'TAGCTATCACGACCGCGGTCGATTTGCCCGAC'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 2

        align = self.dynprog.alignment(s1, s2, self.cost)

        # print(align[-1][-1])
        r1 = ""
        r2 = ""
        r1, r2 = self.dynprog.unpack_alignment(align, s1, s2, r1, r2)
        #
        print(r1)
        print(r2)

    @staticmethod
    def cost(x, y):
        if y == x == "":
            return 1
        if x != y:
            return 2
        if x == y:
            return 0

if __name__ == '__main__':
    unittest.main()
