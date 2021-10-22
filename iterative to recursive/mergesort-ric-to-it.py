import math


class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def top(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)
# function for merge sort
# arr[l..r] is the array that needs to be sorted
# l and r are the left and right indices of arr


# function for merging two sub arrays of arr[l..r]
def merge(arr, l, m, r):
    # length of left half of arr
    nL = m - l + 1

    # length of right half of arr
    nR = r - m

    # create two empty arrays L[0..nL] and R[0..nR]
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)

    # copy left half of arr in L[0..nL-1]
    for i in range(0, nL):
        L[i] = arr[l + i]

    # copy right half of arr in R[0..nR-1]
    for j in range(0, nR):
        R[j] = arr[m + 1 + j]

    # put infinity as sentinel value at the end of Both L and R
    L[nL] = math.inf
    R[nR] = math.inf

    # iterate over L and R
    # and copy the smallest of L[i] and R[j] to arr[k]
    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def mergeSort(arr, l, r):

    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# merge sort not recursive
def mergeSortIterative(arr, l, r):
    cl = l
    cr = r
    stackM = Stack()
    stackL = Stack()
    stackR = Stack()
    last = None
    while(cl <= cr or not stackR.isEmpty()):
        if(cl <= cr):
            if(cl < cr):
                m = (cl + cr) // 2
                stackM.push(m)
                stackR.push(cr)
                stackL.push(cl)
                cr = m
            else:
                last = cr
                cr = cl-1
        else:
            m = stackM.top()
            cl = stackL.top()
            cr = stackR.top()
            if last != cr:
                cl = m+1
            else:
                merge(arr, cl, m, cr)
                stackM.pop()
                stackL.pop()
                stackR.pop()
                last = cr
                cr = cl-1


if __name__ == '__main__':
    A = [2, 1, 4, 3, 5, 6]
    mergeSortIterative(A, 0, len(A)-1)
    print(A)


# iterative mergesort


# iterativa
# QS(A, P, R)
#     stackQ = stackR = stackP = NUll
#     lastR = NUll
#     cP = P
#     cR = R lastR = NUll
#     while(cP <= cR | | stackR=NUll)
#        if(cP <= cR)then
#            if(cP < cR)then
#                 Q = (P+R)/2
#                 stackR.push(cR)
#                 stackP.push(cP)
#                 stackQ.push(Q)
#                 cR = Q
#             else
#                 lastR = cR
#                 cR = cP-1
#         else
#             cP = top(stackP)
#             cR = top(stackR)
#             Q = top(stackQ)
#             if lastR !=cR then
#                 cP = Q+1
#             else
#                 Merge(A, cP,Q,cR)
#                 stackP.pop(stackP)
#                 stackR.pop(stackR)
#                 stackQ.pop(stackQ)
#                 lastR = cR
#                 cR = cP-1
