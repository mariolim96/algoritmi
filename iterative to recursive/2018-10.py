from datastructure import Stack, BinarySearchTree

#dovrebbe essere giusto
def algo(T, x, y):
    a = 1
    b = 1
    if T is not None:
        val = T.data
        if x <= val <= y:
            a = algo(T, x, val-1)
            if a != 0:
                b = algo(T, val+1, y)
        else:
            a = 0
    ret = a and b
    return ret


def iterative_algo(T, x, y):
    stackY = Stack()
    lastY = None
    retval = None
    # stackA=
    while(T is not None or not stackY.isEmpty()):
        if T is not None:
            a = 1
            b = 1
            val = T.data
            if x <= val <= y:
                stackY.push(y)
                y = val-1
            else:
                a = 0
                # terminazione
                ret = a and b
                lastY = y
                retval = ret
                T = None
        else:
            y = stackY.top()
            if lastY != y:
                a = ret
                if a != 0:
                    x = val+1
                else:
                    ret = a and b
                    stackY.pop()
                    lastY = y
                    retval = ret
                    T = None
            else:
                b = ret
                stackY.pop()
                lastY = y
                retval = ret
                T = None

    return retval


if __name__ == "__main__":
    T = BinarySearchTree()
    T.insert(40)
    for i in range(0, 100):
        T.root.data = i
        print(i, ": ", algo(T.root, 1, 1))

    # print(iterative_algo(T.root, 1, 9))
