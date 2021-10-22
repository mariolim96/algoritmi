from random import randint

## aggiustare variabile  nell'else
class Stack:

    def __init__(self):
        self.stack = []

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def sizeStack(self):
        return len(self.stack)


def ALGORITMO(A: list, i: int, j: int, x: bool):
    ret = 0
    if j-i >= 1:
        y = randint(0, 10) % 2
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
    retval = ret
    stackX = Stack()
    stackY = Stack()
    lastY = None
    while j-i >= 1 or not stackX.isEmpty():
        if j-i >= 1:
            ret = 0
            y = 1
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
            x = stackX.top()
            y = stackY.top()
            if x == 1:
                if lastY != 1-y:
                    i = stackI.top()
                    ret = retval
                    if ret % 2 == 0:
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
                    j = stackJ.top()
                    ret = retval
                    if ret % 2 == 1:
                        j = stackJ.top()
                        stackRet.push(ret)
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
                    ret = stackRet.pop()
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
    # print(ALGORITMO(A, 0, len(A)-1, 1))
    print(iterative_algo(A, 0, len(A)-1, 1))
