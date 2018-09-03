def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while (list[j] > key) and (j >= 0):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


if __name__ == '__main__':
    import timeit
    import src.utils as util

    print("Enter the Record Size")
    reco = input()
    reco = int(reco)
    a = util.populate_list(reco)
    st = timeit.default_timer()
    sorted_list = insertion_sort(a)
    print("Running Time ", (timeit.default_timer() - st))