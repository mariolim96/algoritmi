from datastructure import BinarySearchTree, Node, Stack


def G(i):
    return i*i


def algo(T: Node, i: int):
    a = G(i)
    if T is None:
        return a
    else:
        z = algo(T.left, 2*i)
        a = z+a+(T.data)*i
        z = algo(T.right, 2*i+1)+a
        return 3*z


def iterative_algo(T: Node, i: int):
    stackT = Stack()
    stackA = Stack()
    stackI = Stack()
    lastT = None
    retval = None
    if T is None:
        return G(i)
    while(T is not None or not stackT.isEmpty()):
        if T is not None:
            a = G(i)
            if(T.left is not None):
                stackT.push(T)
                stackI.push(i)
                T = T.left
                i = 2*i
            else:
                z = G(2*i)
                a = z+a+(T.data)*i
                if(T.right is not None):
                    stackT.push(T)
                    stackI.push(i)
                    stackA.push(a)
                    T = T.right
                    i = 2*i+1
                else:
                    z = G(2*i+1)+a
                    retval = 3*z
                    lastT = T
                    T = None
        else:
            T = stackT.top()
            if lastT is not T.right and T.right is not None:
                i = stackI.top()
                z = retval
                a = G(i)
                a = z+a+(T.data)*i
                stackA.push(a)
                T = T.right
                i = 2*i+1
            else:
                if T.right is not None:  # torno da destra
                    a = stackA.pop()
                    z = retval+a
                    retval = z*3
                    lastT = T
                    T = None
                    stackT.pop()
                    stackI.pop()
                else:  # torno da sinistra ma destro e nil
                    i = stackI.top()
                    z = retval
                    a = G(i)
                    a = z+a+(T.data)*i
                    z = G(2*i+1)+a
                    retval = z*3
                    lastT = T
                    T = None
                    stackT.pop()
                    i = stackI.pop()
    return retval


if __name__ == "__main__":
    T = BinarySearchTree()
    T.insert(2)
    print(algo(T.root, 1))
    print(iterative_algo(T.root, 1))
    T.insert(1)
    print(algo(T.root, 1))
    print(iterative_algo(T.root, 1))
    T.insert(3)
    print(algo(T.root, 1))
    print(iterative_algo(T.root, 1))
