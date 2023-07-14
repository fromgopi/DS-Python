def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lower = func.lower()
        return string_lower
    return wrapper 

def splitter_decorator(function): 
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split 
    print(wrapper)
    return wrapper
 
def uppercase_decorator(func): 
    def f():
        fu = func()
        string_upper = func().upper()
        return string_upper
    return f
 
  
@splitter_decorator
@uppercase_decorator 
def hello():
    return "Hello World"
    

if __name__ == "__main__":
    print(hello())

