
def algo(T, L):
    if T is not None:
        p = T.data % 2
        d = algo(T.right, L)
        if p == 0:
            x = newNode(T.data)
            L = algo(T.left, x)
            x.next = d
        else:
            L = algo(T.left, d)
    return L


def iterative(T, L):
    stackT = Stack()
    stackL = Stack()
    lastT = None
    ret = None
    while(T is not None or stackT.isEmpty() is False):
        if T is not None:
            p = T.data % 2
            stackT.push(T)
            T = T.right
        else:
            T = stackT.Top()
            p = T.data % 2
            if lastT is not T.left and lastT is not None:
                # stackL.push(lastT)
                d = ret
                if p == 0:
                    x = newNode(T.data)
                    T = T.left
                    L = x
                else:
                    T = T.left
                    L = d
            elif lastT is T.left:
                if p == 0:
                    L = ret
                    x.next = d
                    # ritorno
                    stackT.pop()
                    lastT = T
                    T = None
                    ret = L
                    retval = ret
                else:
                    L = ret
                    # ritorno
                    stackT.pop()
                    lastT = T
                    T = None
                    ret = L
                    retval = ret
            elif lastT is None:
                stackT.pop()
                lastT = T
                T = None
                ret = L
                retval = ret
