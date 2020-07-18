from functools import wraps
'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        item = fn(*args,**kwargs)
        return [item, item]
    return wrapper