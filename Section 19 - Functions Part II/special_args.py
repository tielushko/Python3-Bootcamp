# *args - a special operator we can pass into functions. gather remaining arguments as a tuple
# can call whatever we want

#limitation, if we want more nums we need to define parameters for the function!
"""
def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3
"""
#*args allows us to pass in as man as we want

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(3, 1, 3, 4, 5))
print(sum_all_nums(3, 1, 3))

 #**kwargs - gathers remaining keyword arguments and stores them as a dictionary

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is: {color}")

fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")


#PARAMETER ORDERING
"""
1. parameters
2. *args
3. Default parameters
4. **kwargs
"""