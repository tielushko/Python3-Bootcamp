"""
__dunderscore__ - do not use often, defined by Python, don't wanna overwrite. 
"""

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!" #notice that _secret is not a private member, since Python does not support private, but convention is to assign them with _
        self.__message = 'I like turtles!'
        self.__lol = 'ahhagaga'
p = Person()

print(p.name)
print(p._secret)
# print(p.__message) #will return error and put #_Person__message
# can print with 
print(p._Person__message) #name mangling, useful in the inheritance, puts the class name before the 
print(p._Person__lol)