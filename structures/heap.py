class BinaryTree:
    class Node:
        def __init__(self, vid, x):
            self.__id = vid
            self.__data = x
            self.__lchild = None
            self.__rchild = None

        def lchild(self):
            return self.__lchild

        def rchild(self):
            return self.__rchild

        def data(self):
            return self.__data

        def id(self):
            return self.__id

        def __hash__(self):
            return hash(id(self))

        def __repr__(self):
            return "id: {} data: {}\nlchild: {} rchild: {}".format(self.__id, self.__data, self.__lchild.id(),
                                                                   self.__rchild.id())

        def __str__(self):
            return "id: {} data: {}\nlchild: {} rchild: {}".format(self.__id, self.__data, self.__lchild.id(),
                                                                   self.__rchild.id())

    def __init__(self):
        self.__root = self.Node()


class TreeTool:
    @staticmethod
    def print_tree(t):
        TreeTool.depth_first_traversal(t, lambda x: print(x))

    @staticmethod
    def depth_first_traversal(t, f):
        f(t.root)
        if t.root.lchild():
            TreeTool.__depth_first_traversal(t, t.root.lchild, f)
        if t.root.rchild():
            TreeTool.__depth_first_traversal(t, t.root.lchild, f)

    @staticmethod
    def __depth_first_traversal(t, n, f):
        f(n)
        if t.root.lchild:
            TreeTool.__depth_first_traversal(t, t.root.lchild, f)
        if t.root.rchild:
            TreeTool.__depth_first_traversal(t, t.root.lchild, f)


class Heap:
    def __init__(self):
        t = BinaryTree()

    def insert(self, val):
        pass
