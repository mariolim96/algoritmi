from datastructure import Stack
# p=0       r=3    q1=2   q2=1
# [1, 2, 3, 4]


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


def iterative_algo(A, p, r):
    stackRet = Stack()
    stackR = Stack()
    last = None
    retval = None
    q1 = q2 = None
    while(p <= r or stackR.isEmpty() is not None):

        if p <= r:
            if p == r:
                ret = A[p]
                retval = ret
                last = r
                r = p-1
            else:
                ret = 0
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
                p = q1+1
                r = q2
            else:
                if last != r:
                    ret = stackRet.pop()
                    q2 = (2*p + r) // 3
                    ret = ret + retval
                    p = q2+1
                    stackRet.push(ret)
                else:
                    ret = stackRet.pop()
                    ret = ret+retval
                    p = r+1
                    last = r
                    stackR.pop()
    return retval


A = [1]
print("ecco")
print(algo(A, 0, len(A)-1))
#print(iterative_algo(A, 0, len(A)-1))
