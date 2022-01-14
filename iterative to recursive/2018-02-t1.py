from datastructure import Stack


def algo(A, i, j):
    x = A[i]
    y = A[j]
    ret = 0
    if i <= j:
        q = (i+j)//2
        if i < q:
            x = algo(A, i, q)
            ret = ret+x
        if q+1 < j:
            y = algo(A, q+1, j)
            ret = ret+y
    return ret


def iterative(A, i, j):
    stackI = Stack()
    stackJ = Stack()
    stackRet = Stack()
    stackX = Stack()
    retval = ret = 0
    lastJ = None

    while i <= j or not stackI.isEmpty():
        if i == j:
            ret = 0
            retval = ret
            i = j+1
        elif i <= j:
            x = A[i]
            y = A[j]
            ret = 0
            q = (i+j)//2
            if i < q:
                stackI.push(i)
                stackJ.push(j)
                j = q
            elif q+1 < j:
                stackRet.push(ret)
                stackI.push(i)
                stackJ.push(j)
                i = q+1
            else:
                i = j+1
                retval = ret

        else:
            i = stackI.top()
            j = stackJ.top()
            x = A[i]
            y = A[j]
            q = (i+j)//2
            if lastJ != j:
                x = retval
                ret = ret+x
                if q+1 < j:
                    stackRet.push(ret)
                    stackI.push(i)
                    stackJ.push(q)
                    i = q+1
                else:
                    stackI.pop()
                    stackJ.pop()
                    lastJ = j
                    i = j+1
                    retval = ret
            else:
                ret = stackRet.pop()
                y = retval
                ret = ret+y
                stackI.pop()
                stackJ.pop()
                lastJ = j
                i = j+1
                retval = ret
    return retval


if __name__ == '__main__':
    A = [11, 23, 34, 45, 56, 67, 78, 89, 90, 100]
    print(algo(A, 0, len(A)-1))
    print(iterative(A, 0, len(A)-1))
