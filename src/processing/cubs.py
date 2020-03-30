import multiprocessing as mp


def print_cube(num) -> None:
    """
    Print cube of the given number.

    :param num: Int
    :return: None
    """
    print("Cube: {}".format(num * num * num))


def print_square(num) -> None:
    """
    Print the square of the number.

    :param num: Int
    :return: None
    """
    print("Square: {}".format(num * num))


if __name__ == '__main__':
    num = 100
    cube_process = mp.Process(target=print_cube, args=(num, ))
    square_process = mp.Process(target=print_square, args=(num, ))
    cube_process.start()
    square_process.start()
    pass
