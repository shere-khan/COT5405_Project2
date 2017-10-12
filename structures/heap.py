class Heap:
    def __init__(self):
        self.__data = []

    def change_val(self, val):
        self.__data

    @staticmethod
    def __parent(j):
        return (j - 1) // 2

    @staticmethod
    def __left(j):
        return 2 * j + 1

    @staticmethod
    def __right(j):
        return 2 * j + 2

    def __swap(self, i, j):
        """
        :param i: The first index into the data array to be swapped
        :param j: The second index into the data array to be swapped

        """
        temp = self.__data[i]
        self.__data[j] = self.__data[i]
        self.__data[i] = temp

    def insert(self, n, p):
        """
        :param n: element to be inserted
        :param p: the predicate function to evaluate min or max heap
        """
        self.__data.append(n)
        self.__heapify_up(self.__data[-1], p)

    def __heapify_up(self, i, p):
        """

        :param i: The index into the data array that needs to be corrected
        :param p: the predicate function to evaluate min or max heap

        """
        parent = Heap.__parent(i)

        # If index in question is not root
        # and the projected swap satisfies the respective
        # min or max orientation of the heap
        if i is not 0 and p(i, parent):
            self.__swap(i, parent)
            self.__heapify_up(parent, i)

    def dequeue(self):
        """
        Returns the first element of the queue. Internally, the queue must perform heapify down
        :return: first element of queue

        """
        # store element to return
        elem = self.__data[0]
        self.__swap(0, self.size() - 1)
        self.__data.remove(self.size() - 1)

        self.__heapify_down(0, lambda x, y: x < y)

        return elem

    def __heapify_down(self, i, p):
        n = self.size() - 1
        left = Heap.__left(i)
        right = Heap.__right(i)
        if 2 * i + 1 == n:
            j = self.__data

        if 2 * i < n:
            j = left if p(self.__data[left], self.__data[right]) else right

        if p(i, j):
            self.__swap(i, j)
            self.__heapify_down(j, p)

    def size(self):
        return len(self.__data)
