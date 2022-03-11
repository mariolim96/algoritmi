from datastructure import Stack


def S(A: list, l: int, r: int):
    idx = (l-r+1)
    return A[idx]


def algo(A, l, r):
    s = r-l+1
    if s <= 3:
        return S(A, l, r)
    else:
        k = s//3
        z = algo(A, l, r-k)
        z = z+algo(A, l+k, r)
        h = s//2
        z = z+algo(A, l+h, r-h)
        return z


# r-l <= 1, = > r = -l+2


def iterative_algo(A: list, l: int, r: int):
    stackZ = Stack()
    stackR = Stack()
    stackK = Stack()
    last = None
    retval = None

    while(r-l >= 2 or not stackR.isEmpty()):
        if r-l >= 2:
            s = r-l+1
            if s == 3:
                retval = S(A, l, r)
                last = r
                r = l+1
            else:
                k = s//3
                stackR.push(r)
                stackK.push(k)
                r = r-k
        else:
            r = stackR.top()
            k = stackK.top()
            if last != r and last != r-k:
                z = stackZ.top()
                z = z+retval
                retval = z
                last = r
                r = l+1
                stackZ.pop()
                stackR.pop()
                stackK.pop()
            else:
                if last != r:
                    z = retval
                    stackZ.push(z)
                    l = l+k
                else:
                    z = stackZ.pop()
                    z = z+retval
                    h = s//2
                    stackZ.push(z)
                    l = l+h-k
                    r = r-h
    return retval


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print(algo(A, 0, len(A)-1))
    print(iterative_algo(A, 0, len(A)-1))
