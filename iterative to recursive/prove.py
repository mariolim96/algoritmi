from datastructure import Stack


class Node:
    def __init__(self, dataval=None):
        self.key = dataval
        self.next = None


def listprintNode(node: Node):
    printval = node
    while printval is not None and printval.key is not None:
        print(printval.key)
        printval = printval.next


def algo(A, p, r, L: Node):
    ret = L
    if p <= r:
        Li = Node()
        q = (p+r)//2
        Li.key = A[q]
        if A[q] % 2 == 0:
            Li.next = algo(A, q+1, r, L)
            ret = algo(A, p, q-1, Li)
        else:
            Li.next = algo(A, p, q-1, L)
            ret = algo(A, q+1, r, Li)
    return ret


def iterative_algo(A, p, r, L: Node):
    stackP = Stack()
    stackR = Stack()
    stackL = Stack()
    stackQ = Stack()
    lastR = None
    retval = None
    ret = 0
    while p <= r and not stackR.isEmpty():
        if p <= r:
            Li = Node()
            q = (p+r)//2
            Li.key = A[q]
            if A[q] % 2 == 0:
                stackQ.push(q)
                stackP.push(p)
                stackR.push(r)
                p = q+1
            else:
                stackQ.push(q)
                stackR.push(r)
                r = q-1
        else:
            r = stackR.top()
            q = stackQ.top()
            if A[q] % 2 == 0:
                if lastR == r:
                    Li.next = retval
                    p = stackP.top()
                    r = q-1
                    L = Li
                else:
                    ret = retval
                    stackR.pop()
                    stackQ.pop()
                    stackP.pop()
                    lastR = r
                    r = q-1
            else:
                if lastR != r:
                    Li.next = retval
                    p = q+1
                    L = Li
                else:
                    ret = retval
                    stackR.pop()
                    stackQ.pop()
                    lastR = r
                    r = q-1
    return ret


if __name__ == '__main__':
    A = [1, 2]
    L = Node(3)
    ret = iterative_algo(A, 0, len(A)-1, L)
    print(ret,)
