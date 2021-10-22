from datastructure import Stack
#sembra funzionare

def algo(A, i, j, k):
    ret = -1
    if i < j:
        m = i+j//2
        if A[m] == k:
            ret = m
        else:
            if i < m:
                ret = algo(A, i, m-1, k)
            if m < j and (ret == -1 or A[ret] != k):
                ret = algo(A, m+1, j, k)
    else:
        if A[i] == k:
            ret = i
    return ret


def iterative_algo(A, i, j, k):
    retval = ret = -1
    stackI = Stack()
    stackJ = Stack()
    lastI = None
    while i < j or not stackI.isEmpty():
        # gestisco il caso base e quello delle ricorsioni
        if i == j:
            if A[i] == k:
                ret = i
            else:
                ret = -1
            lastI = i
            retval = ret
            i = j+1
        elif i < j:
            m = i+j//2
            if A[m] == k:
                ret = m
                i = j+1
            else:
                if i < m:
                    stackI.push(i)
                    stackJ.push(j)
                    j = m-1
                elif m < j and (ret == -1 or A[ret] != k):
                    stackI.push(i)
                    stackJ.push(j)
                    i = m+1
        else:
            i = stackI.top()
            j = stackJ.top()
            m = i+j//2
            if lastI != m+1:
                ret = retval
                if m < j and (ret == -1 or A[ret] != k):
                    i = m+1
                else:
                    # ritorno
                    stackI.pop()
                    stackJ.pop()
                    retval = ret
                    lastI = i
                    i = j+1
            else:
                ret = retval
                stackI.pop()
                stackJ.pop()
                retval = ret
                lastI = i
                i = j+1

    return ret


if __name__ == '__main__':
    A = [1, 2, 3]
    print(algo(A, 0, len(A)-1, 3))
    print(iterative_algo(A, 0, len(A)-1, 3))
