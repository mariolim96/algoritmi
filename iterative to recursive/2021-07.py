from datastructure import BinarySearchTree, Node, Stack
import random
# da rivedere condizione nell'else  last sbagliato


def Cancella(T: Node):
    pass


def algo(T: Node, x: int, k: int):

    if T is not None:
        z = (random.randint(0, 100)+x) % 2
        if x == 1:
            T.left = algo(T.left, z, k)
            T.right = algo(T.right, 1-z, k)
            if T.data % 2 == k % 2 and abs(T.data-k <= 3):
                T = Cancella(T)
        else:
            T.right = algo(T.right, 1-z, k)
            T.left = algo(T.left, z, k)

            if T.data % 2 != k % 2 and abs(T.data-k >= 3):
                T = Cancella(T)
    return T


def iterative_algo(T: Node, x: int, k: int):
    stackT = Stack()
    stackX = Stack()
    stackZ = Stack()
    lastT = None
    retval = None
    while(T is not None or not stackT.isEmpty()):
        if T is not None:
            z = (random.randint(0, 100)+x) % 2
            stackZ.push(z)
            stackT.push(T)
            stackX.push(x)
            if x == 1:
                x = z
                T = T.left
            else:
                x = 1-z
                T = T.right
        else:
            T = stackT.top()
            x = stackX.top()
            z = stackZ.top()
            if x == 1:
                if lastT is not T.right and T.right is not None:
                    T.left = retval
                    T = T.right
                    x = 1-z
                else:
                    if T.right is not None:
                        T.right = retval
                    else:
                        T.left = retval
                        T.right = None
                    if T.data % 2 == k % 2 and abs(T.data-k <= 3):
                        T = Cancella(T)
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None
            else:
                if lastT is not T.left and T.left is not None:
                    T.right = retval
                    T = T.left
                    x = z
                else:
                    if T.left is not None:
                        T.left = retval
                    else:
                        T.right = retval
                        T.left = None
                    if T.data % 2 != k % 2 and abs(T.data-k >= 3):
                        T = Cancella(T)
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None
    return retval


def iterative_algo1(T: Node, x: int, k: int):
    stackT = Stack()
    stackX = Stack()
    stackZ = Stack()
    lastT = None
    retval = None
    while(T is not None and stackT.isEmpty() is not False):
        if (T is not None):
            z = (random.randint(0, 100)+x) % 2
            stackT.push(T)
            stackX.push(x)
            stackZ.push(z)
            if x == 1:
                T = T.left
                x = z
            else:
                T = T.right
                x = 1-z
        else:
            T = stackT.top()
            x = stackX.top()
            z = stackZ.top()
            if x == 1:
                if lastT is not None and lastT is not T.right:
                    T.left = retval
                    T = T.right
                    x = 1-z
                elif lastT is T.right:
                    T.right = retval
                    if T.data % 2 == k % 2 and abs(T.data-k <= 3):
                        T = Cancella(T)
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None
                else:  # caso in cui last e null e si fa solo il ritorno del valore
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None
            else:  # codice praticamente inverso a quello sopra
                if lastT is not None and lastT is not T.left:
                    T.right = retval
                    T = T.left
                    x = z
                elif lastT is T.left:
                    T = T.left
                    if T.data % 2 == k % 2 and abs(T.data-k <= 3):
                        T = Cancella(T)
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None
                else:  # caso in cui last e null e si fa solo il ritorno del valore
                    lastT = T
                    stackT.pop()
                    stackX.pop()
                    stackZ.pop()
                    retval = T
                    T = None


if __name__ == '__main__':
    T = BinarySearchTree()
    T.insert(11)
    T.insert(32)
    T.insert(4)
    T.insert(5)
    T.insert(6)

    print(algo(T.root, 1, 11))
    print("\n")
    print(iterative_algo(T.root, 1, 5))
