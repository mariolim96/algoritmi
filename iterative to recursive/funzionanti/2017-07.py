from datastructure import BinarySearchTree, Node, Stack

# funziona perfettamente


def algo(T: Node, h):
    ret = -1
    s = 0
    d = 0
    if T is not None:
        if T.left is not None:
            s = algo(T.left, h+1)
        if T.right is not None:
            d = algo(T.right, h+1)
        if s == 0 and d == 0:
            ret = h
        else:
            ret = s+d
    return ret


def iterative(T: Node, h):
    stackT = Stack()
    stackS = Stack()
    stackD = Stack()
    lastT = None
    ret = retval = -1
    while T is not None or not stackT.isEmpty():
        if T is not None:
            s = d = 0
            if T.left is not None:
                stackT.push(T)
                T = T.left
                h = h+1
            elif T.right is not None:
                stackT.push(T)
                stackS.push(s)
                T = T.right
                h = h+1
            elif s == 0 and d == 0:
                ret = h
                lastT = T
                retval = ret
                T = None
            else:
                ret = s+d
                lastT = T
                retval = ret
                T = None
        else:
            T = stackT.top()
            h = h-1
            if lastT is not T.right and T.right is not None:  # destro non nullo ma vengo da sinistra
                s = ret
                stackS.push(s)
                T = T.right
                h = h+1
            else:
                if T.right is not None:  # vengo da destra
                    s = stackS.pop()
                    d = retval
                    if s == 0 and d == 0:
                        ret = h
                        lastT = T
                    else:
                        ret = s+d
                        lastT = T
                    retval = ret
                    T = None
                    stackT.pop()
                else:  # vengo da sinistra ma destro nullo
                    s = retval
                    d = 0
                    if s == 0 and d == 0:
                        ret = h
                        lastT = T
                    else:
                        ret = s+d
                        lastT = T
                    retval = ret
                    T = None
                    stackT.pop()
    return retval


if __name__ == '__main__':
    T = BinarySearchTree()
    T.insert(5)
    T.insert(3)
    T.insert(7)
    T.insert(2)
    T.insert(6)
    T.insert(8)
    T.insert(1)
    T.insert(4)
    T.insert(9)
    print(algo(T.root, 0))
    print(iterative(T.root, 0))
