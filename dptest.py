import dp
import unittest


class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.dynprog = dp.RNA()

    def test_alignment(self):
        # s1 = 'AGGCTATCACCTGACCTCCAGGCCGATGCCC'
        # s2 = 'TAGCTATCACGACCGCGGTCGATTTGCCCGAC'

        s1 = 'ACAGATTA'
        s2 = 'TAGCTTA'

        f = lambda x, y: 1 if y == "" or x == "" or x != y else 2

        align = self.dynprog.alignment(s1, s2, self.cost)

        r1 = ""
        r2 = ""
        r1, r2 = self.dynprog.unpack_alignment(align, s1, s2, r1, r2)

        print('Edit Distance: ' + str(align[-1][-1][0]))
        print('s1: ' + r1)
        print('s2: ' + r2)
        print()

    def test_secondary_structure(self):
        s = 'AUGGCUACCGGUCGAUUGAGCGCCAAUGUAAUCAUU'
        ss_score = self.dynprog.secondary_structure(s)
        print("String: " + s)
        print("Number of matching pairs: " + str(ss_score))

    @staticmethod
    def cost(x, y):
        if y == "" or x == "":
            return 1
        if x != y:
            return 1
        if x == y:
            return 0

if __name__ == '__main__':
    unittest.main()
