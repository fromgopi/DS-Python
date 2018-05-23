def char_frequecy(str):
    count = {}
    for n in str:
        keys = count.keys()
        if n in keys:
            count[n] += 1
        else:
            count[n] = 1
    return count


if __name__ == '__main__':
    print('Hello World!')
    print(char_frequecy("abracadabra"))
