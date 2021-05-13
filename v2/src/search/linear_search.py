import random
import timeit

def linear_search(array, key):
    for index, value in enumerate(array):
        if value == key:
            return index
    return -1

if __name__ == '__main__':
    array = [random.randrange(1, 99999, 1) for i in range(10000)]
    key = 12
    start = timeit.default_timer()
    res = linear_search(array=array, key=key)
    stop = timeit.default_timer()
    if res != -1:
        print(key, " is found at ", res, "th index")
    else:
        print("not found")

    print('Time: ', stop - start)  