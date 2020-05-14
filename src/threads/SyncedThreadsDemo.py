import threading as t

x = 0


def increment():
    global x
    x += 1


def thread_increment():
    for _ in range(10000):
        increment()


def main_thread():
    global x
    x = 0
    t1 = t.Thread(target=thread_increment)
    t2 = t.Thread(target=thread_increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main_thread()
        print("Iteration {0}: x = {1}".format(i, x))
