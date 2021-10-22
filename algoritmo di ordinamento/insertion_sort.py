# in pratica quello che si fa e prendere il primo elemento e confrontaro a ritroso con gli elementi a destra,
#  vedendo se e maggiore rispetto a quell a[i] e si scambia se e maggiore

def insertion_sort(A):
    for j in range(2, len(A)):
        i = j-1
        key = A[j]
        while i > 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
