def solution(A, B, C):
    s = ""
    while A + B + C > 0:
        r1, r2, r3 = False, False, False
        if A > 0:
            r1, s = insert(s, "a")
            if r1:
                A = A - 1
        if B > 0:
            r2, s = insert(s, "b")
            if r2:
                B = B - 1
        if C > 0:
            r3, s = insert(s, "c")
            if r3:
                C = C - 1
        if r1 == False and r2 == False and r3 == False:
            break
    return s


def insert(s, c):
    N = len(s)
    for i in range(0, N + 1):
        left = i - 2 if i - 2 >= 0 else 0
        right = i + 2 if i + 2 <= N else N
        if c * 2 not in s[left:right]:
            s = s[:i] + c + s[i:]
            return True, s
    return False, s


if __name__ == '__main__':
    res = solution(6, 1, 1)
    print(res)