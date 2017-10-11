class HeapPriorityQueue:
    def __init__(self):
        self.__data = []

    def __parent(self, j):
        (j - 1) // 2

    def __left(self, j):
        return 2 * j + 1

    def __right(self, j):
        return 2 * j + 2

    def __insert(self, i):
        self.__data.append(i)
        self.__heapify_up(i)

    def __heapify_up(self, i):
        pass
