from datastructure import Stack, BinarySearchTree
from sys import maxsize

#perfetta funziona
def algo(T, k):
    ret = maxsize
    if T is not None:
        x = T.data % 2
        y = algo(T.left, k)
        if x == k % 2:
            ret = 0
        else:
            ret = y
        z = algo(T.right, k)
        ret = min(ret, z)+1
    return ret


def iterative(T: BinarySearchTree, k):
    stackT = Stack()
    lastT = 1
    ret = retval = maxsize
    stackRet = Stack()
    while T is not None or not stackT.isEmpty():
        if T is not None:
            ret = maxsize
            stackT.push(T)
            T = T.left
        else:
            T = stackT.top()
            x = T.data % 2
            if lastT is not T.right and T.right is not None:  # torno da sinistra e destro e non null
                y = retval
                x = T.data % 2
                if x == k % 2:
                    ret = 0
                else:
                    ret = y
                T = T.right
                stackRet.push(ret)
            else:
                if T.right is not None:  # torno da destra
                    z = retval
                    ret = stackRet.pop()
                elif lastT is not T.right:  # torno da sinistra ma destro e null
                    y = retval
                    if x == k % 2:
                        ret = 0
                    else:
                        ret = y
                    z = maxsize
                # ritorno
                ret = min(ret, z)+1
                stackT.pop()
                lastT = T
                T = None
                retval = ret
    return retval


if __name__ == "__main__":
    T = BinarySearchTree()
    T.insert(11)
    T.insert(32)
    T.insert(4)

    print(algo(T.root, 10))
    print(iterative(T.root, 10))
