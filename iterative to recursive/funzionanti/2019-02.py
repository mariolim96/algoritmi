from datastructure import Stack

#funziona

def algo(A, x, y, k):
    val = 0
    if x <= y:
        z = (x+y)//2
        if A[z] == k:
            val = 1
        a = algo(A, x, z-1, k)
        if a > val:
            b = algo(A, z+1, y, k)
        else:
            b = a+val
        val = val+a+b
    return val


def iterative_algo(A, x, y, k):
    stackY = Stack()
    stackZ = Stack()
    stackVal = Stack()
    stackA = Stack()
    lastY = None
    retval = 0
    while(x <= y or not stackY.isEmpty()):
        if x <= y:
            val = 0
            z = (x+y)//2
            if A[z] == k:
                val = 1
            stackY.push(y)
            stackZ.push(z)
            stackVal.push(val)
            y = z-1
        else:
            y = stackY.top()
            z = stackZ.top()
            val = stackVal.top()
            if lastY != z+1:  # ritorniamo dalla prima
                a = retval
                if a > val:
                    stackA.push(a)
                    x = z+1
                else:
                    b = a+val
                val = val+a+b
                # ritorno
                retval = val
                lastY = y
                stackY.pop()
                stackZ.pop()
                stackVal.pop()
                x = y+1
            else:
                a = stackA.pop()
                b = retval
                val += a+b
                # ritorno
                retval = val
                lastY = y
                stackY.pop()
                stackZ.pop()
                stackVal.pop()
                x = y+1

    return retval


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(algo(A, 0, len(A)-1, 3))
    print(iterative_algo(A, 0, len(A)-1, 3))
