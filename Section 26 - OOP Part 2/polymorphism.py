#1. Polymorphism and Inheritance - same method name is used different classes

class Animal:
    def speak():
        raise NotImplementedError("Subclass needs to implement this method")
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak()) #note the error as the speak isn't implemented inside the Fish!

#2. The same operation works for different kinds of objects (being passed in as arguments to a function)
