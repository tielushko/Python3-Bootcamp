#Set - collection of data with 1) No duplicate values 2) Unordered values => cannot access them by indexing
#useful when keeping track about collection of values, but don't care about ordering, keys or values, and duplicates

#creating sets
set1 = {1, 4, 5}
print(set1)

set2 = set({1,2,3,4,4,5,5,6,1})
print(set2)

#no indexing is supported, but can test with ___ in ___
print(1 in set2)
print(8 in set1)

#looping through set
for number in set2:
    print(number)


#gives the ability to distil the list to hold only a set of unique values
cities = ["LA", "San fran", "Tokyo", "LA", "NY", "Oslo", "kyoto", "Tokyo", "NY"]

unique_cities = set(cities)
print(unique_cities)
print(list(unique_cities))

#METHODS

#.add() - add an element to the set, if already in set, it doesn't change it

#.remove() - remove a value from set. if not present in set, throws a KeyError

#.discard() - to avoid the KeyError from remove, use this.

#.copy() - creates a copy of the set, makes a duplicate of data, but makes a whole other reference in memory

#.clear() - removes all contents of the set

#SET MATH
math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

#intersection
print(math_students & biology_students)
#symmetric_difference

#union
print(math_students | biology_students)