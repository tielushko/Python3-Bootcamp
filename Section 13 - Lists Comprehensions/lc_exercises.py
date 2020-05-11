# Exercise 1
# 1. Given a list  ["Elie", "Tim", "Matt"] , create a variable 
# called answer, 
# which is a new list containing the first letter of each
# name in the list.  I would use a list comprehension, though you 
# could also loop over manually
# 2. Given a list [1, 2, 3, 4, 5, 6] create a variable called 
# answer 2 which is a new list of all the even values

names = ["Elie", "Tim", "Matt"]
answer1 = [name[0] for name in names]
print(answer1)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
print(answer2)

# Exercise 2

# 1. Given two lists  [1,2,3,4]  and  [3,4,5,6] , create a 
# variable called answer, which is a new list that is
# the intersection of the two. Your output should be [3,4].  
# Hint: use the in operator to test whether an element is in a 
# list.  For example:  5 in [1,5,2]   is True.   3 in [1,5,2]   
# is False.
# 
# 2. Given a list of words  ["Elie", "Tim", "Matt"]  create a
# variable called answer2, which is a new list
# with each word reversed and in lower case (use a slice to do 
# the reversal!) Your output should be  ['eile', 'mit', 'ttam']

list_A = [1,2,3,4]
list_B = [3,4,5,6]

list_A_cross_B = [num for num in list_A if num in list_B]
print(list_A_cross_B)

words = ["Elie", "Tim", "Oleg"]
answer2 = [word[::-1].lower() for word in words]
print(answer2)

# Exercise 3
# For all the numbers between 1 and 100(including 100), create a 
# variable called answer, which contains a list with all the 
# numbers that are divisible by 12.  (12, 24, etc)

answer = [num for num in range(1, 101) if num % 12 == 0]
print(answer)

# Exercise 4
# Given the string "amazing", create a variable called answer, 
# which is a list containing all the letters from "amazing" but 
# not the vowels (a, e, i, o, and u).  The answer should look
# like: ['m', 'z', 'n', 'g'].
# 
# Use a list comprehension!

answer = [char for char in "amazing" if char not in "aeoui"]
print(answer)

# Exercise 5
# Using a nested list comprehension and range(), create a variable
# called answer   with the following value -  [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
# To break it down...start by using range and a list comp to 
# generate the list [0,1,2].  And then repeat that whole thing 3 
# times in a nested list comp.  

answer = [[num for num in range(1,4)] for val in range(1,4)] 
print(answer)

# Exercise 6
# Using list comprehension, create a variable called answer with 
# the following value:
answer = [[num for num in range(10)] for val in range(10)]
print(answer)