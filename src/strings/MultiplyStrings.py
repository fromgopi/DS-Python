
class MultipleStrings(object):

    def multiply(self, num1, num2):
        try:
            return str(int(num1) * int(num2))
        except:
            return ''


if __name__ == '__main__':
    mul = MultipleStrings()
    print(mul.multiply(1234, 1235))