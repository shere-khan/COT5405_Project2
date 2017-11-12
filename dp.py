class RNA:
    class Pair:
        def __init__(self, l, r):
            self.l = l
            self.r = r

    def secondary_structure(self, s):
        n = len(s)

    def opt(self, i, j, n):
        for k in range(3, 10):
            for i in range(0, n - k):
                j = i + k
                vals = []
                l = 0
                for t in range(i, j - 4):
                    vals[l] = self.compute_opt(i, j, t)
                    l += 1

    def compute_opt(self, i, j, t):
        max(self.secondary_structure(i, j - 1), max())

    def populate_base_no_pointer(self, M, m, n):
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                M.append([i]) if j == 0 else M[i].append(0)

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

    def alignment_no_pointer(self, s1, s2, f):
        n = len(s1)
        m = len(s2)
        M = [[i for i in range(m + 1)]]
        self.populate_base_no_pointer(M, m, n)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                vals = [M[i - 1][j - 1] + f(s1[i - 1], s2[j - 1]),
                        M[i - 1][j] + f("", s2[j - 1]),
                        M[i][j - 1] + f(s1[i - 1], "")]
                mynn = min(vals)
                M[i][j] = mynn

        return M

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
