class LetterCombination(object):
    keyPad = {
        '9': 'wxyz',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '1': '',
        '0': '',
        '*': '',
        '': '#'
    }

    def findCombination(self, digits):
        if digits == '':
            return []

        len_dig = len(digits)
        result = list()
        s = ""
        self.backtrack(len_dig, result, digits, s, 0)
        return result

    def backtrack(self, len_dig, result, digits, s, count):
        if len_dig == count:
            result.append(s)
            return
        else:
            for i in self.keyPad[digits[count]]:
                s = s + i
                self.backtrack(len_dig, result, digits, s, count + 1)
                s = s[:-1]


if __name__ == '__main__':
    findCom = LetterCombination()
    print(findCom.findCombination("24"))
