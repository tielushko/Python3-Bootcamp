# Given two lists  ["CA", "NJ", "RI"]  and  ["California", "New Jersey", "Rhode Island"]  create a
# dictionary that looks like this  {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'} .
# Save it to a variable called answer. I expect you to do this with a dictionary comprehension, but you can also use a built-in function called
# zip.  We cover it later in the course

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(len(list1))}
print(answer)

# or 
answer = dict(zip(list1, list2))
print(answer)