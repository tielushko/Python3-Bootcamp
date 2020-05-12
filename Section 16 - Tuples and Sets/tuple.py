#Tuple - an ordered collection of items that is IMMUTABLE (cannot be changed)

numbers = (1, 2, 3, 4, 5, 6)
alphabet = ('a', 'b', 'c', 'd')

#Tuples are commonly used for UNCHANGING data:
months = ('January', 'February', 'March')

#create with ()

#dict with tuple
locations = {
    (35, 75) : "Tokyo",
    (50, 50) : "New York",
    (37, 122) : "San Fransisco"
}

print(locations[(35,75)])
print()

#.items() dict method returns tuples

#looping
names = ('Oleg', 'Darcy', 'Elliot')

for name in names:
    print(name)

print() 

i = len(names) - 1

while i >= 0:
    print(names[i])
    i -=1

#.count() number of elements inside the tupl

#.index() index of a value found inside of the tuple - only the first matching index will show up, error if the value is not present

#can also use slices as with lists

#tuples are like lists, but are lightweight and IMMUTABLE
#tuples can serve as keys in the dictionary

