# Return a number further away from zero
def max_magnitude(list_l):
    return max(abs(number) for number in list_l)

# sum of even values
'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''
def sum_even_values(*args):
    return sum(filter(lambda x: x % 2 == 0, args))


#Define a sum floats function
'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

def sum_floats(*args):
    sum = 0
    for num in args:
        if type(num) == float:
            sum += num
    return sum

"""Version 2
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
"""

# Interleave strings
"""
interleave('hi','ha')     # 'hhia'
interleave('aaa', 'zzz')   # 'azazaz'
interleave('lzr','iad') #  'lizard'

"""

def interleave(string1, string2):
    zipped = list(zip(string1, string2))
    zipped = ["".join(word) for word in zipped]
    zipped = "".join(zipped)
    return zipped

"""
Version 2:
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))
"""

##########################################################
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(l_for_list):
    return [num * 3 for num in list(filter(lambda x: x % 4 == 0, l_for_list))]

"""Version 2
def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))
"""

#####################################################################
"""
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
"""

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']