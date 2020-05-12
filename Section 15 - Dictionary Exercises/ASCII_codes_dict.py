# Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a
# dictionary comprehension and chr()  . Save the result to the answer variable. You only need to care
# about capital letters (65-90).

ASCII = {key:chr(key) for key in range(65,91)}
print(ASCII) 