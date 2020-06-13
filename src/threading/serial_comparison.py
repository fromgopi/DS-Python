import time
from concurrent.futures.thread import ThreadPoolExecutor


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as worker:
        res = worker.map(func, args)

    return list(res)

def cpu_heavy(x):
    print('I am,', x)
    count = 0
    for i in range(10**10):
        count += i


n_jobs = 5

if __name__ == '__main__':
    maker = time.time()
    for i in range(n_jobs):
        cpu_heavy(i)

    maker = time.time()
    multithreading(cpu_heavy, range(n_jobs), 4)
    print("Multithreading spent", time.time() - maker)