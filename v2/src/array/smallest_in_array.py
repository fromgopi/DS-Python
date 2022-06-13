import sys

def find(arr):
    """
    """
    first_min = second_min = sys.maxsize
    len_of_array = len(arr)
    """
    Base case Logic
    there should be min 2 number in the array
    """
    if len_of_array < 2:
        print("There should be more than 2 elements")
        return

    """
    Logic
    loop through the arry
    if given item is smaller than 1st and 2nd min
        update 1st with array item and 2nd with 1st
    else if given item is smaller than 2nd min and 
        not equal to 1st min then update the 2nd min
    """
    print(arr)
    for num in range(0, len(arr)):
        print("for " + str(num) + "th iteration " + 
            " 1st min is " + str(first_min) + 
            " and 2nd min is " + str(second_min))
        if arr[num] < first_min:
            second_min = first_min
            first_min = arr[num]
        elif arr[num] < second_min and  arr[num] != first_min:
            second_min = arr[num]
if __name__ == '__main__':
    arr = [2]
    find(arr)