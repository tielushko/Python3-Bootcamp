#we can raise errors (throw errors) by typing raise

# raise ValueError("Invalid Value")

# you want to be having useful information in the errors, and the type of error needs to match the Python type


#also helpful is to have a documentation that tells you which arguments go where. 
def colorize(text, color): 
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("Text must be an instance of string!") #good practice is to split tests for each of the arguments.
    if type(color) is not str:
        raise TypeError("Color must be an instance of string!")
    if color not in colors:
        raise ValueError("The color entered is not supported b the function")

    print(f"Printed {text} in {color}")


colorize("hello", "blue") # valid call
colorize("hello", "chicken") #invalid call
colorize(123, "cyan") #invalid
colorize("hello", 123) #invalid