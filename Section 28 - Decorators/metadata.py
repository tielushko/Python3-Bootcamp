#Preserving metadata of a function: doc, name
from functools import wraps
#wraps preserves a function's metadata when it is decorated by wrappers

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I am a wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here is the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Adds two numbers together"""
    return x + y

print(add(10,30))
print(add.__doc__)
print(add.__name__)
help(add)