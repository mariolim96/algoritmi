from datastructure import Stack

# qualche problema nella variabile ret ma funziona abbastanza bene
def algo(A: list, p: int, r: int):
    ret = 0
    if p <= r:
        if p == r:
            ret = A[p]
        else:
            q1 = (p + 2*r) // 3
            ret = algo(A, p, q1)
            q2 = (2*p + r) // 3
            ret = ret+algo(A, q1+1, q2)
            ret = ret+algo(A, q2+1, r)
    return ret


def iterative_algo(A, p, r):
    stackRet = Stack()
    stackR = Stack()
    stackP = Stack()
    last = None
    retval = None
    q1 = q2 = None
    while(p <= r or not stackR.isEmpty()):

        if p <= r:
            ret = 0
            if p == r:
                ret = A[p]
                retval = ret
                last = r
                r = p-1
            else:
                retval = ret
                q1 = (p + 2*r) // 3
                stackR.push(r)
                r = q1
        else:
            r = stackR.top()
            if last != q2 and last != r:
                q1 = (p + 2*r) // 3
                ret = retval
                q2 = (2*p + r) // 3
                stackRet.push(ret)
                stackP.push(p)
                p = q1+1
                r = q2
            else:
                ret = stackRet.pop()
                if last != r:
                    p = stackP.pop()
                    q2 = (2*p + r) // 3
                    ret = ret + retval  # errore ret , si salva il valore precedente
                    p = q2+1
                    stackRet.push(ret)
                else:
                    ret = ret+retval
                    retval = ret
                    p = r+1
                    last = r
                    stackR.pop()
    return retval


A = [1, 2]
print("ecco")
print(algo(A, 0, len(A)-1))
print(iterative_algo(A, 0, len(A)-1))
