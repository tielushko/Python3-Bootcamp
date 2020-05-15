"""
try: 
    num = int(input("Please enter a number"))
except:
    print("thats not a not a number!")
else: #runs when except is not run
    print("I run when except doesn't run when the error is not caught!")
finally: #runs no matter what: whether error happened or else happened
    print("I run no matter what!")
"""

#a more practical way to handle the incorrect input

while True:
    try: 
        num = int(input("Please enter a number"))
    except ValueError:
        print("thats not a not a number!")
    else: #runs when except is not run
        print("Good job, you entered a number")
        break
    finally: #runs no matter what: whether error happened or else happened
        print("I run no matter what!")
print("rest of logic game runs!")
