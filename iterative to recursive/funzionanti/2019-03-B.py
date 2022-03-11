# 1. L’ho modficata prima della chiamata?
# 2. La dovrò leggere dopo la chiamata e prima della
# prossima chiamata o del return?
# prove fatte e sembra funzionare
from datastructure import Stack


def algo(A, p, r, k=1):
    ret = 0
    z = 0
    if(p <= r):
        q = (p + r) // 2
        if(k == A[q]):
            z = A[q]
            ret = z+algo(A, q+1, r, k)
        if(ret > 0):
            ret = ret + algo(A, p, q-1, k)
    return ret


def it_algo(A, p, r, k=1):
    stackP = Stack()
    stackQ = Stack()
    stackRet = Stack()
    stackZ = Stack()
    last = None
    retval = 0
    while p <= r or not stackP.isEmpty():
        if p == r:
            ret = 0
            z = 0
            q = (p+r)//2
            if(k == A[q]):
                z = A[q]
                ret = z+0
            # if not stackP.isEmpty():
            #     stackP.pop()
            #     stackQ.pop()
            #     stackZ.pop()
            retval = ret
            last = q
            p = r+1
        elif p <= r:
            ret = 0
            z = 0
            q = (p+r)//2
            if(k == A[q]):
                z = A[q]
                stackP.push(p)
                stackQ.push(q)
                stackZ.push(z)
                # stackRet.push(ret)
                p = q+1
            else:
                if ret > 0:
                    stackP.push(p)
                    stackRet.push(ret)
                    r = q-1
                else:
                    retval = ret
                    last = p
                    p = r+1
        else:
            p = stackP.top()
            if last != p:
                z = stackZ.top()
                q = stackQ.top()
                ret = z+retval
                if(ret > 0 and q < r):
                    r = q-1
                    # stackQ.pop()
                    # stackZ.pop()
                    stackRet.push(ret)
                else:
                    stackP.pop()
                    stackQ.pop()
                    stackZ.pop()
                    last = p
                    retval = ret
                    p = r+1
            else:
                ret = stackRet.top()
                ret = ret+retval
                stackP.pop()
                stackQ.pop()
                stackZ.pop()
                stackRet.pop()
                last = p
                retval = ret
                p = r+1
    return retval


if __name__ == "__main__":
    A = [1, 4, 1]
    print(algo(A, 0, len(A)-1, 1))
    print(it_algo(A, 0, len(A)-1, 1))
