from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] == val:
                return fn(*args, **kwargs)
            return f"Invalid! First arg needs to be {val}"
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) #(burrit )
print(fav_foods("ice cream", "burrito")) #invalid, first argument isn't correct.

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 20)) #correct
print(add_to_ten(20, 10)) #invalid!