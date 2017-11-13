class RNA:
    class Pair:
        def __init__(self, l, r):
            self.l = l
            self.r = r

    def secondary_structure(self, s):
        opt = [[0]]
        n = len(s)
        for k in range(4, 10):
            for i in range(n - k):
                j = i + k
                max(opt[i, j - 1], self.max_base_pairs(i, j, opt))

    def max_base_pairs(self, s, i, j, opt):
        vals = []
        for k, t in enumerate(range(j-4)):
            if self.is_match(s[t], s[j], s):
                vals[k] = 1 + opt[i, t - 1] + opt[t + 1,  - 1]

    def is_match(self, x, y, s):
        if s[x] is 'C' and s[y] is 'G':
            return True
        elif s[x] is 'G' and s[y] is 'C':
            return True
        elif s[x] is 'A' and s[y] is 'U':
            return True
        elif s[x] is 'U' and s[y] is 'A':
            return True
        else:
            return False

    def populate_base(self, M, m, n):
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0 and j == 0:
                    M.append([(i, None)])
                elif i == 0 and j > 0:
                    M[i].append((j, (i, j - 1, 'left')))
                elif i > 0 and j == 0:
                    M.append([(i, (i - 1, j, 'up'))])
                else:
                    M[i].append((0, None))

    def alignment(self, s1, s2, f):
        n = len(s1)
        m = len(s2)
        M = []
        self.populate_base(M, m, n)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                a = M[i - 1][j - 1][0] + f(s1[i - 1], s2[j - 1])
                b = M[i - 1][j][0] + f("", s2[j - 1])
                c = M[i][j - 1][0] + f(s1[i - 1], "")
                vals = [a, b, c]
                mynn = min(vals)
                M[i][j] = (mynn, self.getparent(vals.index(mynn), i, j))

        return M

    def getparent(self, val, i, j):
        if val == 0:
            return i - 1, j - 1, 'diag'
        if val == 1:
            return i - 1, j, 'up'
        if val == 2:
            return i, j - 1, 'left'

    def unpack_alignment(self, M, s1, s2, r1, r2):
        if M is None:
            return 'No alignment'
        n = len(s1)
        m = len(s2)
        parent_info = M[n][m][1]
        if parent_info is None:
            return 'No alignment'

        parent_i = parent_info[0]
        parent_j = parent_info[1]
        res = self.getstring(s1, s2, parent_info[2], n, m)
        r1 += res[0]
        r2 += res[1]

        r1, r2 = self.__unpack_alignment(M, parent_i, parent_j, s1, s2, r1, r2)
        return r1, r2

    def __unpack_alignment(self, M, i, j, s1, s2, r1, r2):
        parent_info = M[i][j][1]
        if parent_info is None:
            return r1, r2
        if parent_info[0] == parent_info[1] == 0:
            if parent_info[2] == 'up':
                r1 = s1[i - 1] + r1
                r2 = "_" + r2
                return r1, r2

            r1 = "_" + r1
            r2 = s2[j - 1] + r2
            return r1, r2

        res = self.getstring(s1, s2, parent_info[2], i, j)
        r1 = res[0] + r1
        r2 = res[1] + r2

        parent_i = parent_info[0]
        parent_j = parent_info[1]
        parent = M[parent_i][parent_j][1]

        r1, r2 = self.__unpack_alignment(M, parent_i, parent_j, s1, s2, r1, r2)
        return r1, r2

    def getstring(self, s1, s2, s, i, j):
        if s == 'diag':
            return s1[i - 1], s2[j - 1]
        if s == 'up':
            # return s1[i - 1], s2[j]
            return s1[i - 1], "_"
        if s == 'left':
            # return s1[i], s2[j - 1]
            return "_", s2[j - 1]


class RNATool:
    def __init__(self):
        pass
