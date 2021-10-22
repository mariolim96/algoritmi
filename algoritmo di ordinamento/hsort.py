import operator as op

from utils import swap, MAX_SENTINEL, MIN_SENTINEL


# do we have a max heap or min heap?
MIN = 0
MAX = 1

test_arr = [10, 14, 16, 8, 7, 2, 4, 1, 9, 3]
midterm = [25, 24, 21, 20, 13, 17, 16, 12]
final = [84, 12, 16, 96, 2, 8, 18, 24]


def get_sentinel(min_or_max=MAX):
    """
        Args:
            min_or_max: max heap or min heap?
        Returns:
            Which sentinel we need to use.
    """
    if min_or_max == MAX:
        return MIN_SENTINEL
    else:
        return MAX_SENTINEL


"""
Next come three functions to navigate the heap:
"""


def parent(i):
    """
        Args:
            i: the index of the child
        Returns:
            The index of the parent.
    """
    return (i - 1) // 2


def left(i):
    """
        Args:
            i: the index of the parent
        Returns:
            The index of the left child.
    """
    return 2 * i + 1


def right(i):
    """
        Args:
            i: the index of the parent
        Returns:
            The index of the right child.
    """
    return 2 * i + 2


def get_opt(min_or_max):
    """
        Args:
            min_or_max: Are we dealing with a min or max heap?
        Returns:
            The proper operator to deal with our heap type.
    """
    if min_or_max == MAX:
        return op.gt
    else:
        return op.lt


def heapify(h, i, heapsize=None, min_or_max=MAX):
    """
        In the text book, there is a max-heapify function.
        and a separate function would be needed for min-heapify.
        But we can easily combine them into one function, and
        just pass in the operator we need to differentiate 
        a max heap from a min heap.
        Args:
            h: the list containing the heap.
            i: the node that might violate the heap property.
            heapsize: the size of the heap
            min_or_max: are we dealing with a max heap or min heap?
        Returns:
            None
    """
    if heapsize is None:
        heapsize = len(h)

    comp = get_opt(min_or_max)

    l = left(i)
    r = right(i)
    if l < heapsize and comp(h[l], h[i]):
        largest = l
    else:
        largest = i
    if r < heapsize and comp(h[r], h[largest]):
        largest = r
    if largest != i:
        swap(h, i, largest)
        heapify(h, largest, heapsize, min_or_max)


def build_heap(h, min_or_max=MAX):
    """
        Args:
            h: the list to heapify.
            min_or_max: are we creating a max heap or a min heap?
        Returns:
            None
            The heap is built in place.
    """
    heapsize = len(h)
    for i in range((heapsize // 2), -1, -1):
        heapify(h, i, heapsize, min_or_max)


def heapsort(h, min_or_max=MAX):
    """
        Args:
            h: the list to heap sort
            min_or_max: are we sorting a max heap or a min heap?
        Returns:
            None
        Performance: O(n lg n)
    """
    build_heap(h, min_or_max)
    print("After build_heap, h = " + str(h))
    heapsize = len(h)
    for i in range(len(h) - 1, -1, -1):
        print("Looping in heapsort with i = " + str(i)
              + "; h = " + str(h))
        swap(h, 0, i)
        heapsize -= 1
        heapify(h, 0, heapsize, min_or_max)


if __name__ == "__main__":
    h = [1, 3, 4, 5, 6, 34, 6, 3, 2, 56, 2, 778, 3]
    heapsort(h, MAX)

    
