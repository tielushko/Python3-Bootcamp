def square(num): return num*num

#syntax - lambda parameter: code in one line without return - you usually don't store that in variable

square2 = lambda num: num * num
add = lambda num: num + num

print(square2(3))
print(square2.__name__)

#use case - passing in a function as a parameter  into another function. short and sweet, single expression


#map - accepts at least two arguments, a function and an "iterable"
""" It runs the lambda for each value in the iterable and returns a map object that can be converted into a different data structure"""
nums = [2,4,6,8,10]
doubles = map(lambda x: x*2, nums) # returns map object

people = ["Darcy", 'Anabel', 'Dana', 'Christina']

peeps = map(lambda name: name.upper(), people)

print(list(peeps))

#Exercise 1: Decrement each element in list by one
def decrement_list(l_for_list):
    return list(map(lambda x: x - 1, l_for_list))

#filter - there is a lambda for each value in the iterable
"""
returns filter object, contains only objects that return true to lambda
"""

l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)