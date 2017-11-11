class RNA:
    def __init__(self):
        pass

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

    def alignment(self, s1, s2, f):
        n = len(s1)
        m = len(s2)
        M = [[i for i in range(m)]]
        for i in range(1, n):
            M[i] = [i]

        for i in range(1, n):
            for j in range(1, m):
                vals = [self.a(M, i, j, f),
                        self.b(M, i, j, f),
                        self.c(M, i, j, f)]
                mynn = min(vals)
                M[i, j] = (mynn, self.getparent(vals.index(mynn)))

    def unpack_alignment(self):
        pass

    def getparent(self, val):
        pass

    def a(self, M, i, j, f):
        return M[i - 1, j - 1] + f(i, j)

    def b(self, M, i, j, f):
        return M[i - 1, j] + f("", j)

    def c(self, M, i, j, f):
        return M[i, j - 1] + f(i, "")


class RNATool:
    def __init__(self):
        pass
