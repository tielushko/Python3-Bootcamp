from random import randint

#Define your make_noise function below
def make_noise():
    print("THE CROWD GOES WILD!")

#Then, call make_noise once:
make_noise()


#function that will toss a coin
def flip_coin():
    if (randint(0,1) == 0):
        return "heads"
    else:
        return "tails"

print(flip_coin())

# Write a function called generate_evens   that returns a list of the even numbers between 1 and 50(not including 50). 
# Basically, it should return a list: [2,4,6....all the way up to 48] 
# Inside the function, you can construct the list using either a loop OR list comprehension.
# You do not need to call the function in this exercise, defining it is enough.

def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]


#default parameters
def exponent(base, power=2): #if power argument is not provided, the function will use power of 2 by default
    return base ** power

print(exponent(3,3))
print(exponent(3))

#default parameters can be anything, even other functions
def add(a,b):
    return a+b
def math(a,b,func=add): #make sure to put the default parameters at the very end
    return func(a,b)

def subtract(a,b):
    return a - b

math(2,2) #4
math(2,2,subtract) #0

#global variables 
total = 0

def increment(): # if we modify global variable in local scope we need to use keyword global. if we just access it, we don't need it
    global total
    total += 1
    return total

#nonlocal - lets us modify a parent's variables in a child function
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

#function documentation 
# use """"""

def say_hello():
    """A simple function that returns the word hello"""
    return "Hello!"

print(say_hello.__doc__)
