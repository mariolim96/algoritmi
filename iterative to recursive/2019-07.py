from datastructure import Stack


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


def iterative_algo(A, p, r):
    stackRet = Stack()
    stackr = Stack()
    last = None
    retval = 0

    while(p <= r or stackRet.isEmpty() is not None):
        if p == r:
            ret = A[p]
            retval = ret
            r = p-1
        else:
            if p < r:
                ret = 0
                q1 = (p + 2*r) // 3
                stackr.push(r)
                r = q1
                # p = q1+1
            else:
                if last is None or last == q1:
                    r = stackr.top(r)
                    q1 = (p + 2*r) // 3

                    ret = retval
                    q2 = (2*p + r) // 3
    return retval
