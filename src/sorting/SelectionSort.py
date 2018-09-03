def selection_sort(list):
    """
    Simple logic for Selection Sort algorithm.
    :param list of random unsorted items:
    :return list of sorted Random items:
    """
    n = len(list)
    for i in range(n):
        min_element = i
        for j in range(i+1, n):
            if list[min_element] > list[j]:
                min_element = j

        list[i], list[min_element] = list[min_element], list[i]

    return list


if __name__ == '__main__':
    import timeit as t
    import src.utils as util

    print("Enter the Record Size")
    reco = int(input())
    unsorted_array =  util.populate_list(reco)
    st = t.default_timer()
    sorted_array = selection_sort(unsorted_array)
    et = t.default_timer()
    print("Time taken to Sort list using Selection Sort ", (et-st))