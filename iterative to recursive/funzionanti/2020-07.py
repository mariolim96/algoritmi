from datastructure import Stack, BinarySearchTree, Node
#visto dal prof, perfetto

def algo(A, i, j):
    ret = i
    if (i <= j):
        k = i+1
        while (k <= j) and A[k] <= A[i]:
            k = k+1
        ret = algo(A, i, (i+j)/2)
        if k % 2 == 1:
            ret = algo(A, k/2, j)+ret-k
        else:
            ret = algo(A, k, j)+ret-k/2
    return ret


def iterative_algo(A, i, j):
    cI = i
    cJ = j
    stackJ = Stack()
    stackK = Stack()
    retval = None
    ck = None
    lastJ = None
    while cI <= cJ and not stackJ.isEmpty():
        if (cI <= cJ):
            ret = cI
            k = cI+1
            while (k <= j) and A[k] <= A[i]:
                k = k+1
            stackJ.push(j)
            stackK.push(k)
            j = (i+j)/2
        else:
            cJ = stackJ.top()
            cK = stackK.top()
            if lastJ is not cJ:
                ret = retval
                if cK % 2 == 1:
                    i = cK/2
                else:
                    i = cK
            else:
                if cK % 2 == 1:
                    ret = retval+ret-ck
                    # risalita
                    retval = ret
                    lastJ = cJ
                    stackJ.pop()
                    stackK.pop()
                    i=j+1
                else:
                    ret = retval+ret-ck/2
                    # risalita
                    retval = ret
                    lastJ = cJ
                    stackJ.pop()
                    stackK.pop()
                    i=j+1
    return retval
