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
    
