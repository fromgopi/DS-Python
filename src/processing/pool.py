from multiprocessing import Pool


def mul(x):
    return x ^ x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(mul, [1, 2, 3]))
