def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError: 
        print("Don't divide by zero please!")
        print(err)
    except TypeError as err:
        print("a and b must be ints or floats!")
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')

print(divide(1, 2))
print(divide(2, 2))