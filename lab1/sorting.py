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
