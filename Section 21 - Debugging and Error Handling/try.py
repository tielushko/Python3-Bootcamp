#In python, it is strongly encouraged to use try: except blocks

#THE BASIC SYNTAX
# try: 
# except:

try: 
    foobar
except:
    print("PROBLEM!") #not a good idea: generic, we are not handling it, nothing is being done about it, also it is catching all sorts of errors along the way

print("After the try")

#more specific
try:
    colt
except NameError:
    print("You tried to use a variable that was never declared")

def get(d, key):
    try: 
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "name")) #"Ricky"
print(get(d, "City")) #none