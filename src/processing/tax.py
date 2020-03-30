import time


def basic_func(x) -> str:
    """
    Basic function to check if number is odd or even.

    :param x: Int
    :return: String
    """
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == '__main__':
    start_time = time.time()
    for i in range(0, 20):
        y = i * i
        time.sleep(2)
        print('{} squared results in a/an {} number'.format(i, basic_func(y)))

print('That took {} seconds'.format(time.time() - start_time))
