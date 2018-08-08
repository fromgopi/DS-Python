def count(S, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m <= 0 and n >= 1:
        return 0
    return count(S, m - 1, n) + count(S, m, n - S[m - 1])


def dynamic_count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n + 1)]

    for i in range(m):
        table[0][i] = 1

    print("N :: ", n)
    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0
            print("Table[] :: ", table[i])
            print("X :: ", x)
            y = table[i][j - 1] if j >= 1 else 0
            print("Y :: ", y)
            table[i][j] = x + y

    print(table[n][m - 1])


def space_optimised_dynamic_count(S, m, n):
    table = [0 for k in range(n + 1)]
    table[0] = 1

    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
    print(table[n])


if __name__ == '__main__':
    S = [5, 6, 7, 8, 10]
    m = len(S)
    n = 500000
    # print(count(S, m, n))
    # dynamic_count(S, m, n)
    space_optimised_dynamic_count(S, m, n)
