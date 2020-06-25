def shout(fn): #this becomes the standard decorator form
    def wrapper(*args, **kwargs):#def wrapper(name):
        return fn(*args, **kwargs).upper() #fn(name).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi! I am {name}"

@shout #won't work.... solution -> *args and **kwargs
def order(main,side):
    return f"Hi! Id like the {main} with a side of {side}"

print(greet("todd"))
print(order("burger", "fries"))