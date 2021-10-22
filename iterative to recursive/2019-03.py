from datastructure import Stack

# ci sono dei problemini , funziona a meta
#da correggere

def algo(A, p, r, k):
    ret = False
    if(p <= r):
        if(p == r):
            ret = (k == A[p])
        else:
            q = (p + r) // 2
            ret1 = algo(A, p, q-1, k)
            ret = (k == A[p]) or ret1
            if(not ret):
                ret = algo(A, q+1, r, k)
    return ret


def iterative_algo(A, p, r, k):
    stackR = Stack()
    stackRet = Stack()
    stackQ = Stack()
    retval = False
    lastR = None
    while p <= r or not stackR.isEmpty():
        if p <= r:
            ret = False
            if(p == r):
                ret = (k == A[p])
                # ritorno
                retval = ret
                r = p-1
            else:
                q = (p + r) // 2
                ret = (k == A[q])
                if not ret:
                    stackR.push(r)
                    stackQ.push(q)
                    r = q-1
        else:
            r = stackR.top()
            q = stackQ.top()
            if lastR != r:
                ret = retval
                if not ret:
                    p = q+1
                else:
                    # ritorno
                    stackR.pop()
                    stackQ.pop()
                    retval = ret
                    lastR = r
                    r = p-1
            else:
                ret = retval
                # ritorno
                retval = ret
                stackR.pop()
                stackQ.pop()
                lastR = r
                r = p-1
    return retval


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(algo(A, 0, len(A)-1, 5))
    print(iterative_algo(A, 0, len(A)-1, 5))
