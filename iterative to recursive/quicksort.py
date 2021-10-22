from datastructure import Stack


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, start, end):
    x = array[end]
    i = start - 1
    for j in range(start, end):
        if (array[j] <= x):
            i = i+1
            swap(array, i, j)
    swap(array, i+1, end)
    return i+1


def partition2(A, start, end):
    p = start-1
    r = end+1
    x = A[start]
    while not p >= r:
        while True:
            r -= 1
            if A[r] >= x:
                break
        while True:
            p += 1
            if A[p] <= x:
                break
        if p < r:
            swap(A, p, r)


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)


def quicksort_iterativo(array, p, r):
    stackR = Stack()
    stackQ = Stack()
    cp = p
    cr = r
    q = None
    last = None
    while cp <= cr or not stackQ.isEmpty():
        if cp < cr:
            q = partition(array, cp, cr)
            stackQ.push(q)
            stackR.push(cr)
            cr = q-1
        elif cp == cr:
            last = cr
            cr = cp-1
        else:
            q = stackQ.pop()
            cr = stackR.pop()
            if last != cr:
                cp = q+1
            else:
                last = cr
                cr = cp-1


if __name__ == '__main__':
    unsortedArray = [2, 8, 7, 1, 3, 5, 6, 4, 9, 0]
    quicksort_iterativo(unsortedArray, 0, len(unsortedArray)-1)
    print(unsortedArray)


# iterativa
# QS(A, P, R)
#     stackQ = stackR = NULL
#     lastR = NULL
#     cP = P
#     cR = R lastR = NULL
#     while(cP <= cR | | stackR=NULL)
#        if(cP <= cR)then
#            if(cP < cR)then
#                 Q = partiziona(A, cP, cR)
#                 stackR.push(cR)
#                 stackQ.push(Q)
#                 cR = Q
#             else
#                 lastR = cR
#                 cR = cP-1
#         else
#             cR = top(stackR)
#             Q = top(stackQ)
#             if lastR !=cR then
#                 cP = Q+1
#             else
#                stackR.pop(stackR)
#                 stackQ.pop(stackQ)
#                 lastR = cR
#                 cR = cP-1


# altre versioni
# void quickSortIterative(int arr[], int l, int h)
# {
#     // Create an auxiliary stack
#     int stack[h - l + 1]

#     // initialize top of stack
#     int top = -1;

#     // push initial values of l and h to stack
#     stack[++top] = l;
#     stack[++top] = h;

#     // Keep popping from datastructure while is not empty
#     while (top >= 0) {
#         // Pop h and l
#         h = stack[top--];
#         l = stack[top--];

#         // Set pivot element at its correct position
#         // in sorted array
#         int p = partition(arr, l, h);

#         // If there are elements on left side of pivot,
#         // then push left side to stack
#         if (p - 1 > l) {
#             stack[++top] = l;
#             stack[++top] = p - 1;         }

#         // If there are elements on right side of pivot,
#         // then push right side to stack
#         if (p + 1 < h) {
#             stack[++top] = p + 1;
#             stack[++top] = h;         }
#     }
# }
