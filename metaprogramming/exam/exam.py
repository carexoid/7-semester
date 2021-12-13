import binary_tree

if __name__ == "__main__":
    a = binary_tree.BinarySearchTree((int,))
    a.insert(12312)
    a.insert(3)
    a.insert(7)
    print(a.search(5))
    print(a.search(3))

    print(a)
