def heapify(arr, len, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len and arr[i] < arr[left]:
        largest = left
    
    if (right < len and arr[largest] < arr[right]):
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, len, largest)


def heap_sort(array = []):
    length = len(array)
    for i in range(length//2, -1, -1):
        heapify(arr, length, i)
    for i in range(length-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
    return arr

def populate_list(ran):
    """
    Returns a list of random integers
    :param random number range:
    :return list:
    """
    import random as r
    my_randoms = []
    for i in range(ran):
        my_randoms.append(r.randrange(1, 10000, 1))
    return my_randoms


if __name__ == '__main__':
    import timeit as t
    print("Enter Input size")
    size = int(input())
    list_cst = t.default_timer()
    arr = populate_list(size)
    list_cet = t.default_timer()
    print("time take for list creation time ", (list_cet-list_cst))
    sort_st = t.default_timer()
    heap_sort(array=arr)
    sort_et = t.default_timer()
    print("time take for sorting list ", (sort_et-sort_st))
    