"""
all() - returns True if all elements are truthy and False if any are falsy
"""

people = ["Charlie", "Chris", "Cody"]

all([name[0]=='C' for name in people]) #TRUE

"""
any() - returns true if any of the elements is truthy and False if all are falsy
"""

#if we don't use brackets with those two functions, we will get generator expression instead
# - saves space in memory if you don't need list, there is no need for creating a new list

# Implement your is_all_strings function below:
def is_all_strings(iterable):
    return all(type(word) == str for word in iterable) 

"""
sorted() returns a new LIST that is sorted from the items in iterable
it does not change the original list, it returns a sorted copy. NOT INPLACE!

sorted(nums, reversed=True) will sort the list in DESCENDING ORDER

to sort the dictionaries - need to specify what should be sorted
sorted(users, key=len)
"""