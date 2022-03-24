
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end

# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

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
    quick_sort(start = 0, end= size-1, array=arr)
    sort_et = t.default_timer()
    print("time take for sorting list ", (sort_et-sort_st))





    