#SET COMPREHENSION

set1 = {x**2 for x in range(1,9)}
print(set1)
set2 = {x:2 for x in range(1,9)}
print(set2) #actually becomes a dictionary!!!

set3 = {char.upper() for char in 'hello'}
print(set3)