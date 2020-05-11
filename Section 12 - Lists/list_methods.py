data = [1, 2, 3]
print(f"Initial list data: {data}")

#add data in the back with 'append'
data.append("purple")
print(f"After appending 'purple': {data}")

#data.append([5, 4, 6, 7]) #can combine in a list, but will add it as a list

#add multiple items with 'extend' to the back of the list 
data.extend([4, 5, 6, 7, 8]) #will merge the two lists together
print(f"after extending with [4,5,6,7,8]: {data}")

#'.insert' - insert an item in a given position
first_list = [1,2,3,4]
print(f"\nfirst_list:{first_list}")
first_list.insert(2, 'Hi!') #inserts AFTER the item with index 2 
print(f"After inserting 'Hi!' AFTER the index 2: {first_list}")
first_list.insert(-1, 'The end') #inserts BEFORE the item with index -1
print(f"After inserting 'The end' BEFORE the index -1: {first_list}")

#'clear' - remove all items in the list
clear_list = [1,2,3,4]
print(f"\nTest list clear_list: {clear_list}")
clear_list.clear()
print(f"Test list clear_list after calling 'clear': {clear_list}")


#'pop' - removes the last item by default and returns it -if passed with index, removes items at that index
pop_list = [1,2,3,4]
print(f"\nTest list pop_list: {pop_list}")
temp = pop_list.pop()
print(f"Test list clear_list after calling 'pop' without parameters (default): {pop_list} returned element: {temp}")
temp = pop_list.pop(1) 
print(f"Test list clear_list after calling 'pop' with index 1: {pop_list} returned element: {temp}")

#'remove' - removes the first item in the list who's value is x - throws a ValueError if the item is not found
remove_list = [1,2,3,4,4,4,4]
print(f"\nTest list remove_list: {remove_list}")
remove_list.remove(2)
print(f"Test list remove_list after calling 'remove' on value 2: {remove_list}")
remove_list.remove(4)
print(f"Test list remove_list after calling 'remove' on value 4. Notice the removal of only 1 occurence of an item: {remove_list}")

#'del' - deletes a value from the list at a specified index EX: del list[index]
del_list = [1, 2, 3, 4]
del del_list[3]
print(f"After deleting value at index 3: {del_list}") # [1, 2, 3]
del del_list[1]
print(f"After deleting value at index 1: {del_list}") # [1, 3]

#'index' - find the position of a given item in the list 
index_list = [5,6,7,8]
print(f"\nTest list index_list: {index_list}")
print(f"Index of number 7 in the index_list: {index_list.index(7)}")
print(f"Index of number 5 in the index_list: {index_list.index(5)}")
# - can specify start and end index(value_to_search, start_index, end_index)
numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(f"\nTest list numbers: {numbers}")
print(f"Index of number 5 in the numbers starting from beginning: {numbers.index(5)}") # 0
print(f"Index of number 5 in the numbers starting from index 1: {numbers.index(5,1)}") # 1
print(f"Index of number 5 in the index_list starting from index 2: {numbers.index(5,2)}") # 4
print(f"Index of number 8 in the index_list starting from index 6 ending at index 8: {numbers.index(8,6,8)}") # 6

#'count' - counts number of times element appears in the list
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
print(f"\nTest list numbers: {numbers}")

print(f"Number of 2 in the list:{numbers.count(2)}") # 3
print(f"Number of 21 in the list:{numbers.count(21)}") # 0
print(f"Number of 3 in the list:{numbers.count(3)}") # 2

#'sort'- sorts the elements in ascending order (in-place)
another_list = [6, 4, 1, 2, 5]
print(f"\nUnsorted list: {another_list}")
another_list.sort()
print(f"Sorted list in ascending order: {another_list}") # [1, 2, 4, 5, 6]


#'reverse' - reverse the number of elements in the list (in-place)
first_list = [1, 2, 3, 4]
print(f"\nReversing the list: {first_list}")
first_list.reverse()
print(f"Reversed list: {first_list}") # [4, 3, 2, 1]

#'join' - actually is string list method. -uses
words = ['Coding', 'Is', 'Fun!']
print(f"\nList words before calling join: {words}")
print(f"After calling with space ' '.join(words): {' '.join(words)}") # 'Coding is Fun!'

name = ['Mr', "Steele"]
print(f"\nList words before calling join: {name}")
print(f"After calling with dot and space '. '.join(name): {'. '.join(name)}")# 'Mr. Steele'