from queue import Queue
from threading import Thread
from time import sleep


def do_task(q):
    while True:
        print(q.get())
        q.task_done()


def workers(number_of_threads, q):
    for x in range(number_of_threads):
        worker = Thread(target=do_task, args=(q,))
        worker.setDaemon(True)
        worker.start()

    for u in range(10):
        for v in range(100):
            q.put(u + v * 100)
        q.join()
        print("Batch " + str(u) + " Done")


def fill_queue(max_size) -> Queue:
    q = Queue(maxsize=max_size)
    return q


def test04():
    q = fill_queue(10)
    for x in range(10):
        q.put(x)

    while not q.empty():
        print('Content --------> ', q.get())
        sleep(1)
    re = q.task_done()
    print('state--->', re, '\n')
    q.join()
    print('Over \n')


if __name__ == '__main__':
    test04()
    pass
