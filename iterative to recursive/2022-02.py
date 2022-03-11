from datastructure import Stack
# perfetta


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


def iterative_algo(A: list, l: int, r: int):
    stackZ = Stack()
    stackR = Stack()
    stackL = Stack()
    last = None
    retval = None

    while(r-l >= 0 or not stackR.isEmpty()):
        if r-l+1 >= 0:
            s = r-l+1
            if s <= 3:
                retval = S(A, l, r)
                last = r
                r = l-2
            else:
                k = s//3
                stackR.push(r)
                stackL.push(l)
                r = r-k
        else:
            r = stackR.top()
            l = stackL.top()
            k = (r-l+1)//3
            h = (r-l+1)//2
            if last != r and last != r-k:
                z = stackZ.top()  # torno dalla terza
                z = z+retval
                retval = z
                last = r
                r = l-2
                stackZ.pop()
                stackR.pop()
                stackL.pop()
            else:
                if last != r:
                    z = retval  # torno dalla prima e chiamo seconda
                    stackZ.push(z)
                    l = l+k
                else:
                    z = stackZ.pop()  # torno dalla seconda e chiamo la terza
                    z = z+retval
                    stackZ.push(z)
                    l = l+h
                    r = r-h
    return retval


if __name__ == "__main__":
    A = [1, 2, 6, 6, 3, 4, 6, 6]
    print(algo(A, 0, len(A)-1))
    print(iterative_algo(A, 0, len(A)-1))
