from datastructure import Stack, BinarySearchTree, Node
#non testato

def cancellaRoot(root):
    pass


def algo(T: Node, k1: int, k2: int, P) -> int:
    ret = 0
    if T is not None:
        if T.key < k1:
            ret = algo(T.right, k1, k2, T)
        elif T.key > k2:
            ret = algo(T.left, k1, k2, T)
        else:
            ret = algo(T.left, k1, k2, T)
            ret = ret or algo(T.right, k1, k2, T)
        if not ret:
            if P.left is not None:
                P.left = cancellaRoot(T)
            else:
                P.right = cancellaRoot(T)
    return ret


def iterative_algo(T: Node, k1: int, k2: int, P):
    stackP = Stack()
    stackT = Stack()
    cT = T
    cP = P
    lastT = None
    retval = None
    while cT is not None or not stackP.isEmpty():
        if cT is not None:
            ret = 0
            if cT.key < k1:
                stackP.push(cP)
                stackT.push(cT)
                cP = cT
                cT = cT.right
            elif cT.key > k2:
                stackP.push(cP)
                stackT.push(cT)
                cP = cT
                cT = cT.left
            else:
                stackP.push(cP)
                stackT.push(cT)
                cP = cT
                lastT = cT
                cT = cT.left
        else:
            cT = stackT.top()
            cP = stackP.top()
            if cT.key < k1:
                # assegnamento ret e risalita
                ret = retval
                cT = None
                stackT.pop()
                stackP.pop()
                lastT = cT
                if not ret:
                    if P.left is not None:
                        P.left = cancellaRoot(T)
                else:
                    P.right = cancellaRoot(T)
                retval = ret
            elif cT.key > k2:
                ret = retval
                cT = None
                cT = stackT.pop()
                cP = stackP.pop()
                lastT = cT
                if not ret:
                    if P.left is not None:
                        P.left = cancellaRoot(T)
                else:
                    P.right = cancellaRoot(T)
                retval = ret
            else:
                if lastT is not cT.left and lastT is not None:
                    ret = ret or retval
                    stackT.pop()
                    stackP.pop()
                    if not ret:
                        if P.left is not None:
                            P.left = cancellaRoot(T)
                        else:
                            P.right = cancellaRoot(T)
                    lastT = cT
                    cT = None
                    retval = ret
                elif lastT is cT.left:
                    ret = retval
                    cT = cT.right
                else:
                    ret = ret or 0
                    stackT.pop()
                    stackP.pop()
                    lastT = cT
                    if not ret:
                        if P.left is not None:
                            P.left = cancellaRoot(T)
                        else:
                            P.right = cancellaRoot(T)
                    cT = None
                    retval = ret
