"""
r - reading fike
w - writing to file
a - append to file / add to the end of the file - always at the end
r+ - read and write to file (writing based on python cursor position) -> by default at the beginning of file -> won't insert and shift things over,
will overwrite the contents. -> r+ can only be used with already existing files.

"""

with open("haiku.txt", "w") as file:
    file.write("This is the line 1 of the haiku\n")
    file.write("Following the line 2 of the haiku\n")
    file.write("Finishing off with the line 3 of the haiku\n")

with open("haiku.txt", "a") as file:
    file.write("This is the line 1 of the haiku\n")
    file.write("Following the line 2 of the haiku\n")
    file.write("Finishing off with the line 3 of the haiku\n")

with open("existing_file.txt", "r+") as file:
    file.write("This is the line 1 of the haiku\n")
    file.write("Following the line 2 of the haiku\n")
    file.write("Finishing off with the line 3 of the haiku\n")