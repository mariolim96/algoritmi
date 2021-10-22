def find_Max(A, r):
    max = A[0]
    for i in range(1, r):
        if A[i] > A[max]:
            max = i
    return max


def selection_sort(A):
    for i in range(len(A), 1, -1):
        max = find_Max(A, i)
        J = A[i-1]
        A[i-1] = A[max]
        A[max] = J


if __name__ == "__main__":
    A = [1, 2, 5, 3, 4, 6, 897, 7, 8, 9, 10]
    selection_sort(A)
    print(A)
