class Heap:
    def __init__(self):
        self.__data = []

    @staticmethod
    def __parent(j):
        return (j - 1) // 2

    @staticmethod
    def __left(j):
        return 2 * j + 1

    @staticmethod
    def __right(j):
        return 2 * j + 2

    def __insert(self, i):
        self.__data.append(i)
        self.__heapify_up(self.__data[-1])

    def __swap(self, i, j):
        temp = self.__data[i]
        self.__data[j] = self.__data[i]
        self.__data[i] = temp

    def __heapify_up(self, i, p):
        parent = self.__parent(i)
        if i is not 0 and p(i, parent):
            self.__swap(i, self.__parent)
            self.__heapify_up(parent, i)

    def __heapify_down(self, i, p):
        n = len(self.__data) - 1
        left = self.__left(i)
        right = self.__right(i)
        if 2 * i + 1 == n:
            j = self.__data

        if 2 * i < n:
            j = left if p(self.__data[left], self.__data[right]) else right

        if p(i, j):
            self.__swap(i, j)
            self.__heapify_down(j, p)

    def dequeue(self):
        elem = self.__data[0]
        self.__swap(0, len(self.__data))
        self.__data.remove(len(self.__data))

        self.__heapify_down(0, lambda x, y: x < y)

        return elem
