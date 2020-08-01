"""
we can make simple assertions with assert keyword
assert accepts an expression
Returns None if the expression is truthy
Raises an AssertionError if the expression is falsy
accepts an optional error message as an argument

shouldn't use assert for all of the code testing
"""

def add_positive_numbers(x,y):
    assert x > 0 and y > 0, "Both Numbers Must Be Positive" #if true, nothing happens, if false, the message will raise an error.
    return x + y

#print(add_positive_numbers(1,1)) #runs fine
#add_positive_numbers(-1,0) #invalid, raises AssertionError


def eat_junk(food):
    assert food in [
        "pizza", 
        "ice cream", 
        "candy", 
        "butter"
        ], "food must be junk food" 
    
    return f"Nom Nom Nom, I am eating {food}"

food = input("Enter a food please: ")
print(eat_junk(food))


#Assertions can be overriden with optimized code: if the python code is run with -O tag, it will ignore all assertions
"""Example: Never write code like this, becuase when ran with -O tag, anybody will have capability to run this.
def do_something_bad(user):
    assert user.is_admin, "Only admins can remove bad stuff"
    destroy_a_bunch_of_stuff()
    return "MUHAHAHAHA"
"""