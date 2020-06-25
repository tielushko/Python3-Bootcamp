#Higher order funcs- we can pass funcs as args to other funcs

def square(x):
    return x * x

def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total 

print(sum(3,square))