import time
import unittest

def is_unique_chars_algorithmic(string):
    # Assuming chars in set ASCII
    if len(string)> 128:
        return False
    
    char_set  = [False] * 128
    for char in string:
        val = ord(char)
        print(val)
    

if __name__ == '__main__':
    is_unique_chars_algorithmic("1bc")