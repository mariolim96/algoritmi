from datastructure import Stack


class Node(object):

    def __init__(self, data):
        self.data = data
        self.f1 = None
        self.f2 = None
        self.f3 = None


def algo(T: Node, k1, k2, L):
    if T is not None:
        Li = algo(T.f1, k1, k2, L)
        Li = algo(T.f2, k1, k2, Li)
        Li = algo(T.f3, k1, k2, Li)
        if T.data >= k1 and T.data <= k2:
            L = alloca_nodo()
            L.data = T.data
            L.next = Li
        else:
            L = Li
    return L


def iterative_algo(T: Node, k1, k2, L):
    stackT = Stack()
    stackL = Stack()
    lastT = None
    ret = None
    while T is not None and not stackT.isEmpty():
        if T is not None:
            stackT.push(T)
            stackL.push(L)
            T = T.f1
        else:
            T = stackT.Top()
            L = stackL.Top()
            if lastT is not T.f2 and T.f2 is not None:
                Li = ret
                L = Li
                T = T.f2
            elif lastT is T.f2:
                Li = ret
                L = Li
                T = T.f3
            else:
                Li = ret
                if T.data >= k1 and T.data <= k2:
                    L = alloca_nodo()
                    L.data = T.data
                    L.next = Li
                else:
                    L = Li
                stackT.pop()
                stackL.pop()
                ret = L
                lastT = T
                T = None
    return L
