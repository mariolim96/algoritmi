from datastructure import Stack

# fibonacci algorith


def fibonacci(n):
    if n <= 1:
        return n
    else:
        x = fibonacci(n-1)
        r = x + fibonacci(n-2)
    return r


def iiterative_fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n):
        a, b = b, a + b
    return a


def iterative_fibonacci(n):
    cn = n
    stackN = Stack()
    stackX = Stack()
    ret = 0
    while cn >= 0 or not stackN.isEmpty():
        if cn >= 0:
            if cn <= 1:
                r = cn  # questa si puo evitare
                ret = r  # _____
                last = cn  # return
                cn = -1  # _____
            else:
                stackN.push(cn)
                cn = cn - 1
        else:
            cn = stackN.top()
            if last != cn-2:  # termine prima chiamata
                x = ret
                stackX.push(x)
                cn = cn-2
            else:
                x = stackX.top()  # queste due istruzione si possono evitare mettendo tutto dentro ret
                r = x+ret
                stackX.pop()
                stackN.pop()
                ret = r  # ______
                last = cn  # return
                cn = -1  # ______
    return ret


if __name__ == "__main__":
    print(fibonacci(14))
    print(iterative_fibonacci(14))
