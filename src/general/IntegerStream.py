from collections import OrderedDict
str = 'abcabd'
# arr = [0]*26

def get_first_non_repeated_char(input_string):
    
    order_dict = OrderedDict()

    tmp_list = [(char,1) for char in input_string]
    for key, value in tmp_list:
        if key in order_dict.keys():
            order_dict[key] = order_dict[key] + value
        else: 
            order_dict[key] = value
    
    result=[]
    for key, value in order_dict.items():
        if value == 1:
            result.append(key)
    return result[0]


if __name__ == '__main__':
    print(get_first_non_repeated_char(input_string=str))