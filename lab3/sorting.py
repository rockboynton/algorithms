def insertion_sort(lst):
    """
    Sorts the list lst in place using insertion_sort.
    """
    for i in range(1, len(lst)):
        key = lst[i]

        # shift element in sorted sequence lst[1..i - 1]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1

        # insert lst[i] into the sorted sequence
        lst[j+1] = key 


def merge_sort(lst, p, r):
    """
    Sorts the list lst in place using merge_sort.

    Args:
        lst: list to be sorted
        p: starting index of the list, i.e 0
        r: ending index of the list, i.e. len(lst) - 1
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q+1, r)
        merge(lst, p, q, r)


def merge(lst, p, q, r):
    """
    Merges two sorted partitions of lst.  This is
    performed in-place. It is assumed that the
    two partitions are contiguous in the list.

    Args:
        lst: list that is being sorted
        p: starting index of first partition
        q: ending index of first partition
        r: ending index of second partition
    """
    left = [lst[i] for i in range(p, q+1)]
    right = [lst[j] for j in range(q+1, r+1)]

    i = j = 0
    for k in range(p, r+1):
        if i <= q - p and (j >= r - q or left[i] <= right[j]):
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
    

def build_max_heap(A):
    """Build heap from existing array
    
    Args:
        A (lst): List to heapify
    """
    for i in range(len(A) // 2, -1, -1):
        _max_heapify(A, i)


def heap_extract_max(A):
    """Extracts the max element (root) of the heap

    The heap property is maintained following the call to this function
    
    Args:
        A (list): the heap
    Raises:
        ValueError: if the heap size is not at least 1
    Returns:
        int: the max element in the heap
    """
    if len(A) < 1:
        raise ValueError('Heap underflow')

    max_ = A[0]
    A[0] = A[-1]
    A.pop()
    _max_heapify(A, 0)
    return max_


def max_heap_insert(A, key):
    """Inserts an element into the heap
    
    Args:
        A (list): the heap
        key (int): the element to insert
    """
    A.append(float('-inf'))
    _heap_increase_key(A, len(A) - 1, key)


def heapsort(A):
    """Sort using a max heap

    Takes a list and first converts it to a heap, then pops off the max element
    to a new list while maintaining the heap property until the heap is emptied.
    The original list then has the new sorted list copied into it.
    
    Args:
        A (list): the list to be sorted
    """
    build_max_heap(A)
    sorted_A = []
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        sorted_A.insert(0, A.pop())
        _max_heapify(A, 0)

    for val in sorted_A:
        A.append(val)


def _heap_increase_key(A, i, key):
    """bubbles up key into place in the heap starting at an index
    
    Args:
        A (list): the heap
        i (int): index to start at
        key (int): element to insert
    
    Raises:
        ValueError: if new key is smaller than current key
    """
    if key < A[i]:
        raise ValueError('New key is smaller than current key')

    A[i] = key
    while i > 0 and A[_parent(i)] < A[i]:
        A[i], A[_parent(i)] = A[_parent(i)], A[i]
        i = _parent(i)


def _max_heapify(A, i):
    """Called whenever a heap is modified to maintain heap property
    A[parent(i)] >= A[i]

    Uses recursion

    Args:
        A: the heap array
        i: the index to start with
    """
    l = _left(i)
    r = _right(i)

    largest = i
    if l < len(A) and A[l] > A[largest]:
        largest = l

    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _max_heapify(A, largest)


def _parent(i):
    return (i - 1) // 2


def _left(i):
    return 2 * i + 1


def _right(i):
    return 2 * i + 2
