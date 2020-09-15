#File can be opened and read in the following ways.

"""
Option 1
file = open("story.txt")
file.read()
file.close()

#file.closed # True

Option 2
with open("story.txt") as file:
    file.read()

file.closed #True
"""