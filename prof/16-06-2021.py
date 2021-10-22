from random import randint
from datastructure import Stack


def ALGORITMO(A: list, i: int, j: int, x: bool):
    ret = 0
    if j-i >= 1:
        y = 1
        if (x == 1):
            ret = ALGORITMO(A, (i+j)//2 + 1,  j,     y)
            if ret % 2 == 0:
                ret = ALGORITMO(A,  i,  (i+j)//2, 1 - y)
        else:
            ret = ALGORITMO(A,  i,  (i+j)//2,   y)
            if ret % 2 == 1:
                ret = ret+ALGORITMO(A, (i+j)//2 + 1,  j, 1 - y)
            else:
                ret = A[i]
    return ret


def iterative_algo(A, i, j, x):
    stackRet = Stack()
    stackI = Stack()
    stackJ = Stack()
    ret = 0
    retval = None
    stackX = Stack()
    stackY = Stack()
    lastY = None
    if j-i >= 1 or not stackJ.isEmpty():
        if j-i >= 1:
            ret = 0
            y = randint(1, 10) % 2
            if (x == 1):
                stackI.push(i)
                i = (i+j)//2 + 1
            else:
                stackJ.push(j)
                j = (i+j)//2
            stackX.push(x)
            stackY.push(y)
            x = y
        else:
            x = stackX.Top()
            y = stackY.Top()
            if x == 1:
                if lastY != 1-y:
                    ret = retval
                    if ret % 2 == 0:
                        i = stackI.top()
                        j = (i+j)//2
                        x = 1-y
                    else:
                        stackX.pop()
                        stackY.pop()
                        stackI.pop()
                        retval = ret
                        lastY = y
                        i = j
                else:
                    ret = retval
                    stackX.pop()
                    stackY.pop()
                    stackI.pop()
                    retval = ret
                    lastY = y
                    i = j
            else:
                if lastY != 1-y:
                    ret = retval
                    if ret % 2 == 1:
                        j = stackJ.top()
                        i = (i+j)//2+1
                        x = 1-y
                    else:
                        ret = A[i]
                        stackX.pop()
                        stackY.pop()
                        stackJ.pop()
                        retval = ret
                        lastY = y
                        j = i
                else:
                    ret = ret+retval
                    stackX.pop()
                    stackY.pop()
                    stackJ.pop()
                    retval = ret
                    lastY = y
                    j = i
    return retval


if __name__ == '__main__':
    A = [i+1 for i in range(2)]
    print(A)
    print(ALGORITMO(A, 0, len(A)-1, 1))
    # print(iterative_algo(A, 0, len(A)-1, 1))
