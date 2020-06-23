def fib_list(max):
    final = []
    a = 0
    b = 1
    while  len(final) < max:
        final.append(b)
        a, b = b, a+b
    return final

def fib_gen(max):
    a, b = 0, 1
    count = 0 

    while count < max:
        yield a
        a, b = b, a+b
        count+=1

print(fib_list(10))
fib = fib_gen(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))