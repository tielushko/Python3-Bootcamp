nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[0][1])
print(nested_list[2][1])
print("\n\n")
#printing values in nested lists
for row in nested_list:
    for val in row:
        print(val)