class Fibonacci(object):

    def __init__(self):
        pass

    def fibSerics(self, fib_range):
        table = []
        while len(table) < fib_range+1:
            table.append(0)

        #Base case for the serics
        if fib_range <= 1:
            return fib_range
        else:
            if table[fib_range - 1] == 0:
                table[fib_range - 1] = self.fibSerics(fib_range-1)
            if table[fib_range - 2] == 0:
                table[fib_range - 2] = self.fibSerics(fib_range-2)

            table[fib_range] = table[fib_range-1] + table[fib_range - 2]
        return table[fib_range]


    def space_optimised_fib_serics(self, n):
        a = 0
        b = 1
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2,n):
                c = a + b
                print("C :: ", c)
                a = b
                print("A :: ", a)
                b = c
                print("B :: ", a)
            return b
