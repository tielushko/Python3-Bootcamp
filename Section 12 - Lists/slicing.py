#some_list[start:end:step]
first_list = [1, 2, 3, 4]

#start - the index you start from 
first_list[1:] # slice from index 1 to end - [2,3,4]
first_list[3:] # slice from index 3 to end - [4]
first_list[-1:] # [4]
first_list[-3:] # [2, 3, 4]

#end - the index you copy up to (does not include value AT the index provided)
first_list[:2] # [1, 2]
first_list[:4] # [1, 2, 3, 4]
first_list[1:3] # [2, 3]

first_list[:-1] # [1, 2, 3]
first_list[1:-1] # [2, 3]

#step - same step as in ranges, how many values to skip over
first_list = [1, 2, 3, 4, 5, 6]
first_list[1::2] # [2, 4, 6]
first_list[::2] # [1, 3, 5] 

first_list[1::-1] # [2, 1]
first_list[:1:-1] # [6, 5, 4, 3]
first_list[2::-1] # [3, 2, 1]

#Some tricks with slices

#reverse string
string = "this is fun"
string[::-1]

#modifying portions of list
numbers = [1, 2, 3, 4, 5]
numbers [1:3] = ["a", "b", "c"] #end result: [1, "a", "b", "c", 4, 5]

#can chain the slices with index like so: colors[5] is 'violet' colors[5][::-1] is 'teloiv'