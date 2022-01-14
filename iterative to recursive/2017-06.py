from datastructure import BinarySearchTree, Node, Stack, deleteNode
#da aggiustare

def algo(T: Node, a, b):

    if T is not None:
        if T.data < a:
            T.left = algo(T.left, a, b)

        elif T.data > b:
            T.right = algo(T.right, a, b)
        else:
            T.left = algo(T.left, a, b)
            T.right = algo(T.right, a, b)
            T = deleteNode(T)
    return T


def iterative_algo(T: Node, a, b):
    StackT = Stack()
    lastT = None
    retval = T
    while T is not None or StackT.isEmpty() is False:
        if T is not None:
            StackT.push(T)
            if T.data < a:
                T = T.left
            elif T.data > b:
                T = T.right
            else:
                T = T.left
        else:
            T = StackT.top()
            if lastT is not T.right and T.right is not None:
                T.left = retval
                if T.data < a:
                    lastT = T
                    StackT.pop()
                    retval = T
                    T = None
                else:
                    T = T.right
            else:
                if T.right is not None:
                    T.right = retval
                    if T.data <= b:
                        T = deleteNode(T)
                    lastT = T
                    StackT.pop()
                    retval = T
                    T = None
                else:  # T.right is None e vengo da sinistra
                    T.left = retval
                    if T.data >= a:
                        T.right = None
                        T = deleteNode(T)
                    lastT = T
                    StackT.pop()
                    retval = T
                    T = None

    return retval


if __name__ == '__main__':
    T = BinarySearchTree()
    T.insert(5)
    T.insert(3)
    T.insert(7)
    T.insert(2)
    T.insert(4)
    T.insert(6)
    BinarySearchTree.printlevelorder(T.root)
    BinarySearchTree.printlevelorder(algo(T.root, 2, 6))
    BinarySearchTree.printlevelorder(iterative_algo(T.root, 2, 6))
