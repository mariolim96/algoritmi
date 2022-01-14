from datastructure import BinarySearchTree, Stack, Node


def algo(T: Node, k: int):
    X = None
    if T is not None and k >= 0:
        X = Node()
        X.data = T.data
        if T.right is not None:
            X.right = algo(T.right, k - 1)
        if T.left is not None:
            X.left = algo(T.left, k - 1)
    return X


def iterative_algo(T: Node, k: int):
    stackT = Stack()
    stackK = Stack()
    stackX = Stack()
    lastT = None
    retX = None
    while (T is not None and k >= 0) or not stackT.isEmpty():

        if T is not None and k >= 0:
            X = Node()
            X.data = T.data
            if T.right is not None:
                stackT.push(T)
                stackX.push(X)
                T = T.right
                k = k-1
            elif T.left is not None:
                stackT.push(T)
                stackX.push(X)
                T = T.left
                k = k-1
            else:
                X = Node()
                X.data = T.data
                RetX = X
                lastT = T
                T = None
        else:
            X = stackX.top()
            T = stackT.top()
            k += 1
            if lastT is not T.left and T.left is not None:
                X.right = retX
                T = T.left
                k = k-1
            elif T.left is not None:
                X.left = retX
                stackT.pop()
                stackX.pop()
                lastT = T
                T = None
                retX = X
            else:
                X.right = retX
                X.left = None
                stackT.pop()
                stackX.pop()
                lastT = T
                T = None
                retX = X
    return RetX


if __name__ == "__main__":
    T = BinarySearchTree()
    T.insert(10)
    T.insert(5)
    T.insert(15)
    T.insert(3)
    T.insert(7)
    T.insert(13)
    T.insert(17)
    BinarySearchTree.printlevelorder(T.root)

    X = algo(T.root, 1)
    Y = iterative_algo(T.root, 1)
    BinarySearchTree.printlevelorder(algo(T.root, 1))
    BinarySearchTree.printlevelorder(iterative_algo(T.root, 1))
