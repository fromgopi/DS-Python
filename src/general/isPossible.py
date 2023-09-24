def check(a, b, c, d):
    if a == c and b == d:
        return True
    if a > c or b > d:
        return False
    print("[a = " + str(a) + ", b = " + str(b) + "]")
    check(a, a + b, c, d) or check(a+b, b, c, d)


def isPossible(a, b, c, d):
    print("[c = " + str(c) + ", d = " + str(d) + "]")
    if check(a, b, c, d):
        print("yes")
    else:
        print("No")


if __name__ == '__main__':
    isPossible(1, 4, 5, 9)







