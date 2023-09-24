# Pair of elements

def find_pairs(arr: list[int], k: int):
    numbers_seen = {}
    for num in arr:
        diff = k - num
        if diff in numbers_seen:
            print(numbers_seen)
            return [num, diff]
        numbers_seen[num] = True
    

if __name__ == '__main__':
    print(find_pairs([-5, 4, -2, 16, 8, 9], 15))