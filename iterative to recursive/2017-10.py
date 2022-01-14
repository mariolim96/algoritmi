from datastructure import BinarySearchTree, Node, Stack


def algo(T: Node, a, b):
    if T is not None:
        if T.data > a and T.data < b:
            T.left = algo(T.left, a, T.data)
            T.right = algo(T.right, T.data, b)
        else:
            T = None
    return T


def iterative_algo(T, a, b):
    stackT = Stack()
    stackB = Stack()
    lastT = None
    ret = T
    while T is not None or not stackT.isEmpty():
        if T is not None:
            if T.data > a and T.data < b:
                stackT.push(T)
                stackB.push(b)
                b = T.data
                T = T.left
            else:
                lastT = T
                T = None
                ret = T
        else:
            T = stackT.top()
            b = stackB.top()
            if lastT is not T.right and T.right is not None:
                T.left = ret
                a = T.data
                T = T.right
            else:
                if T.right is not None:
                    T.right = ret

                else:
                    T.left = ret
                    T.right = None
                ret = T
                stackT.pop()
                stackB.pop()
                lastT = T
                T = None
    return ret


if __name__ == '__main__':
    T = BinarySearchTree()
    T.insert(5)
    T.insert(10)
    T.insert(4)
    T.insert(2)

    T.insert(8)
    T.insert(16)
    BinarySearchTree.printlevelorder(T.root)
    BinarySearchTree.printlevelorder(algo(T.root, 3, 13))
    BinarySearchTree.printlevelorder(iterative_algo(T.root, 3, 13))
