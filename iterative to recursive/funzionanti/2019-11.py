from datastructure import Stack
#funzionante 100


def algo(A: list, p, r):
    if p <= r:
        q1 = (2*p+r)//3
        q2 = (2*r+p)//3
        if p <= q1-1:
            ret1 = algo(A, p, q1-1)
        else:
            ret1 = 0
        if A[q1] % 2 == 0:
            ret1 = ret1+1
        if q1+1 <= q2-1:
            ret2 = algo(A, q1+1, q2-1)
        else:
            ret2 = 0
        if A[q2] % 2 == 0:
            ret2 = ret2+1
        if q2+1 <= r:
            ret3 = algo(A, q2+1, r)
        else:
            ret3 = 0
        return ret1+ret2+ret3
    return 0


def algo_iterative(A, p, r):

    retval = 0
    lastR = None
    stackR = Stack()
    stackQ1 = Stack()
    stackQ2 = Stack()
    stackRet1 = Stack()
    stackRet2 = Stack()
    ret1 = ret2 = ret3 = 0
    while p <= r or not stackQ1.isEmpty():
        if p <= r:
            q1 = (2*p+r)//3
            q2 = (2*r+p)//3
            if p <= q1-1:
                stackQ1.push(q1)
                stackQ2.push(q2)
                stackR.push(r)
                r = q1-1
            else:
                ret1 = 0
                if A[q1] % 2 == 0:
                    ret1 = ret1+1
                if q1+1 <= q2-1:
                    stackRet1.push(ret1)
                    stackQ1.push(q1)
                    stackQ2.push(q2)
                    stackR.push(r)
                    r = q2-1
                    p = q1+1
                else:
                    ret2 = 0
                    if A[q2] % 2 == 0:
                        ret2 = ret2+1
                    if q2+1 <= r:
                        stackRet1.push(ret1)
                        stackRet2.push(ret2)
                        stackQ1.push(q1)
                        stackQ2.push(q2)
                        stackR.push(r)
                        p = q2+1
                    else:
                        ret3 = 0
                        lastR = r
                        r = p-1
                        retval = ret1+ret2+ret3
        else:
            q1 = stackQ1.top()
            q2 = stackQ2.top()
            r = stackR.top()
            if lastR != q1-1 and lastR != q2-1:
                # uguale ad r
                ret3 = retval
                ret1 = stackRet1.pop()
                ret2 = stackRet2.pop()
                stackQ1.pop()
                stackQ2.pop()
                stackR.pop()
                lastR = r
                r = p-1
                retval = ret1+ret2+ret3
            elif lastR != q1-1:
                # ritorno da q2-1
                ret1 = stackRet1.top()
                ret2 = retval
                if A[q2] % 2 == 0:
                    ret2 = ret2+1
                if q2+1 <= r:
                    stackRet1.push(ret1)
                    stackRet2.push(ret2)
                    p = q2+1
                else:
                    ret3 = 0
                    stackQ1.pop()
                    stackQ2.pop()
                    stackR.pop()
                    stackRet1.pop()
                    lastR = r
                    r = p-1
                    retval = ret1+ret2+ret3
            else:
                # ritorno da q1-1
                ret1 = retval
                if A[q1] % 2 == 0:
                    ret1 = ret1+1
                if q1+1 <= q2-1:

                    stackRet1.push(ret1)
                    r = q2-1
                    p = q1+1
                else:
                    ret2 = 0
                    if A[q2] % 2 == 0:
                        ret2 = ret2+1
                    if q2+1 <= r:

                        stackRet1.push(ret1)
                        stackRet2.push(ret2)
                        p = q2+1
                    else:
                        ret3 = 0
                        stackQ1.pop()
                        stackQ2.pop()
                        stackR.pop()
                        ret1 = stackRet1.pop()
                        ret2 = stackRet2.pop()
                        lastR = r
                        r = p+1
                        retval = ret1+ret2+ret3

    return retval


if __name__ == "__main__":
    A = [1, 2, 5, 8, 5, 4, 9]
    print(algo(A, 0, len(A)-1))
    print(algo_iterative(A, 0, len(A)-1))
