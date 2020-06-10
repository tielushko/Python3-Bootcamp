class Aquatic:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        return f"{self.name} is swimming"
       
    def greet(self):
        return f"I am {self.name} of the sea"

class Ambulatory:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")    
lassie = Ambulatory("Lassy")
cook = Penguin("Cook")
print(cook.swim())
print(cook.walk())
print(cook.greet()) #calls ambulatory version not aquatic! depends on the order of elements I put in the inheritance.

"""
MRO - method resolution order
__mro__ attribute on class
.mro() method on class
help(cls) built in method - most helpful!

"""
