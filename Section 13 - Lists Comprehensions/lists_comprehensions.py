#the syntax
#[_____ for ____ in ____]

nums = [1,2,3]
print(nums)

nums = [num*10 for num in nums]

print(nums)

#example 2

name = 'colt'
print(name)
name = [char.upper() for char in name]
print(name)

friends = ["ashley", "mike", "oleg"]
print(friends)
friends = [friend.capitalize() for friend in friends]
print(friends)

#example 3 

example3 = [num * 10 for num in range (1, 6)]
print(example3)

#example 4

example4 = [bool(val) for val in [0, [], '']]
print(example4)

#example 5
example5 = [1, 2, 3, 4, 5]
print(example5)
example5 = [str(num) for num in example5]
print(example5)