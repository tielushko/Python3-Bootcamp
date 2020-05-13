################################
'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(day_number):
    days = {
        1 : "Sunday",
        2 : 'Monday', 
        3 : 'Tuesday',
        4 : 'Wednesday',
        5 : 'Thursday',
        6 : 'Friday',
        7 : 'Saturday'
    }
    return days.get(day_number)

#######################################
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list_arg):
    length = len(list_arg)
    if length == 0:
        return None
    return list_arg[length - 1]

#simpler way
# def last_element(list_arg):
#    if list_arg:
#        return list_arg[-1]
#    return None

##############################################
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a,b):
    if a < b:
        return "Second is greater"
    elif a > b:
        return "First is greater"
    return "Numbers are equal"

#############################################
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

def single_letter_count(word, letter):
    return word.upper().count(letter.upper())

#####################################################################
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(string):
    return {char:string.count(char) for char in string}

##########################################################################
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(l_for_list, command, location, value=0):
    if command == "remove" and location == "end":
        return l_for_list.pop()
    elif command == "remove" and location == "beginning":
        return l_for_list.pop(0)
    elif command == "add" and location == "beginning":
        l_for_list.insert(0, value)
        return l_for_list
    elif command == "add" and location == "end":
        l_for_list.append(value)
        return l_for_list
    return "Invalid arguments."

################################################################3
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    string = string.upper().replace(" ", "")
    return string[::-1] == string

#####################################################################
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(l_for_list, number):
    return l_for_list.count(number)

#############################################################
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(l_for_list):
    total = 1
    even = [num for num in l_for_list if num % 2 == 0]
    for num in even:
        total *= num 
    return total

##############################################################
'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    return string.capitalize()

""" Version 2 using slices
def capitalize(string):
    return string[:1].upper() + string[1:]
"""

########################################################################
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(l_for_list):
    return [val for val in l_for_list if val]

########################################################################

"""
intersection([1,2,3], [2,3,4]) #[2,3,4]
intersection([a,b,z], [x,y,z]) #[z]
"""
# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return [l for l in list1 if l in list2]

""" Set Solution
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]
"""
###################################################################

'''
provided
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0

def partition(l_for_list, isEven):
    combined = []
    combined.append([val for val in l_for_list if isEven(val)])
    combined.append([val for val in l_for_list if not isEven(val)])
    return combined

""" version 2
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
"""

####################################################################################

