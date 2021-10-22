def sx(i):
    return 2*i+1


def dx(i):
    return 2*i+2


def padre(i):
    return i//2


def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def heapyfy(A, i, heapsize):
    l = sx(i)
    r = dx(i)
    maggiore = i
    if l < heapsize and A[l] > A[i]:
        maggiore = l
    if r < heapsize and A[r] > A[maggiore]:
        maggiore = r
    if maggiore != i:
        swapPositions(A, i, maggiore)
        heapyfy(A, maggiore, heapsize)


def heap(A):
    heapsize = len(A)
    for i in range(padre(heapsize)-1, -1, -1):
        heapyfy(A, i, heapsize)


def heapsort(A):
    heap(A)
    heapsize = len(A)-1
    print(A)
    for i in range(len(A)-1, 0, -1):
        swapPositions(A, 0, i)
        heapsize -= 1
        print(A[:heapsize+1])
        heapyfy(A, 0, heapsize=heapsize)


if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3, 7]
    print(A)
    heapsort(A)
    print(A)
