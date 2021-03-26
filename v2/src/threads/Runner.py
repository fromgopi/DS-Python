import time
import threading as t

def hello_word(num):
    print("hello", num)
    print("world", num)

def thread_runner():
    task1 = t.Thread(target=hello_word, args=[1])
    task2 = t.Thread(target=hello_word, args=[2])
    task1.start()
    task2.start()
    print("print before .join()")
    task1.join()
    task2.join()
    print("print after .join()")

if __name__ == '__main__':
    thread_runner()