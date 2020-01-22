from multiprocessing import Process, Lock


def printer(item, lock):
    """
    Prints out the Item that was passed
    """
    print("Acquring the lock")
    lock.acquire()
    try:
        print("Printing the item")
        print(item)
    finally:
        print("Rleasing the lock")
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['Tomatos', 'Potato', 'Banana', 'Leeche', 20]
    for item in items:
        proc = Process(target=printer, args=(item, lock))
        proc.start()

    