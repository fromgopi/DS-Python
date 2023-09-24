import re


class CountAndSay(object):

    def countNSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s


if __name__ == '__main__':
    coun = CountAndSay()
    print(coun.countNSay(121))

