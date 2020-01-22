import logging
import multiprocessing as mp
from multiprocessing import Process, Lock


def printer(item, lock):
    """
    Prints out the Item that was passed
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['Tomatos', 'Potato', 'Banana', 'Leeche', 20]
    mp.log_to_stderr()
    logger = mp.get_logger()
    logger.setLevel(logging.INFO)
    for item in items:
        proc = Process(target=printer, args=(item, lock))
        proc.start()

    