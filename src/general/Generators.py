"""These are generator functions common across the project."""


def fib():
    a, b = 0,1
    while True:
        yield a
        a,b = b, a+b

if __name__ == "__main__":
    fgen = fib()
    print([next(fgen) for _ in range(50)])
    