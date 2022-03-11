# T=0
# T have a root and a left or right
# lef
class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self, node=None):
        self.root = node

    @staticmethod
    def search(T, val):
        if T is not None:
            if T.data < data:
                search(T.right, data)
            else:
                search(T.left, data)
        return T

    def ricerca()

    def inserimento(T, val):
        if T is None:
            newNode = Node(val)
            T = newNode(val)
        if T.data > val:
            T = inserimento(T.left, val)
        else:
            T = inserimento(T.right, val)
        return T


    def cancella(T, val):
        if T is not None:

            if T.data > val:
                T.left = cancella(T.left, val)
            elif t.data < val:
                T.rigth = cancella(T.right, val)
            else:
                T = cancella_root(T)
        return T
    # 1 t ha al massimo un figlio
    # 2 t ha 2 figli

    def cancella_root(T):
        if t is not None:
            if T.left is None or T.right is None:
                tmp = T
                if T.left:
                    T = T.left
                else:
                    T = T.right
                free(tmp)
            else:  # caso 2
                tmp = staccaMin(T.right, T)
                scrivi val in T.key
                free(tmp)

    def staccaMin(T, P):
        if T is not None:
            if T.left is not None:
                ret = staccaMin(T.left, T)
            else:
                if p is not None:
                    if T == P.left:
                        P.left = T.right
                    else:
                        P.right = T.right
                ret = T
        return ret
