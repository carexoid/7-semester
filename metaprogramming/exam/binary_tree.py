from abc import ABC, abstractclassmethod


class BinaryTree(ABC):
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self._out = ""
        self._root = None

    @abstractclassmethod
    def insert(self, value):
        pass

    @abstractclassmethod
    def search(self, value):
        pass

    def __sym_print(self, node: Node):
        if node.left != None:
            self.__sym_print(node.left)
        self._out = self._out + str(node.value) + ", "
        if node.right != None:
            self.__sym_print(node.right)

    def __str__(self):
        self._out = ""
        self.__sym_print(self._root)
        return "( " + self._out + ")"


def type_checked(func):
    def wrapper(*args):
        if type(args[1]) not in args[0].types:
            raise ValueError("Value has  wrong type")
        return func(*args)
    return wrapper


class BinarySearchTree(BinaryTree):
    def __init__(self, types):
        super().__init__()
        self.types = types

    @staticmethod
    def __insert(root: BinaryTree.Node, new_node: BinaryTree.Node):
        if root.value > new_node.value:
            if root.left == None:
                root.left = new_node
            else:
                BinarySearchTree.__insert(root.left, new_node)
        else:
            if root.right == None:
                root.right = new_node
            else:
                BinarySearchTree.__insert(root.right, new_node)

    @type_checked
    def insert(self, value):
        new_node = BinaryTree.Node(value)

        if self._root == None:
            self._root = new_node
            return

        BinarySearchTree.__insert(self._root, new_node)

    @staticmethod
    def __search(root: BinaryTree.Node, value):
        if root == None:
            return False

        if root.value == value:
            return True

        if root.value > value:
            return BinarySearchTree.__search(root.left, value)
        else:
            return BinarySearchTree.__search(root.right, value)

    @type_checked
    def search(self, value):
        return BinarySearchTree.__search(self._root, value)

    def __str__(self):
        return super().__str__()


if __name__ != '__main__':
    import sys
    import inspect
    import pprint
    module = sys.modules[__name__]
    classes = [m for m in inspect.getmembers(
        module, inspect.isclass) if m[1].__module__ == __name__]
    for cls in classes:
        print(cls[0])
        print(cls[1].__doc__)
        pprint.pprint(vars(cls[1]))
