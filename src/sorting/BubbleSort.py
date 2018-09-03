def optimized_bubbleSort(a):
    for j in range(len(a)):
        changed = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
            if not changed:
                break
    return a


def bubbleSort(ar):
    n = len(ar)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ar[j] > a[j + 1]:
                ar[j], a[j + 1] = a[j + 1], a[j]
    return ar


if __name__ == '__main__':
    import timeit
    import src.utils as util
    print("Enter the Record Size")
    reco = input()
    reco = int(reco)
    a = util.populate_list(reco)
    st = timeit.default_timer()
    optimized_bubbleSort(a)
    print("Running Time ", (timeit.default_timer() - st))
