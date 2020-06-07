class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age #private for the class
        else:
            self._age = 0
    """
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
    instead we can use propert"""
    @property #getter
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cant be negative!")

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter

    def fullname(self, name):
        self.first, self.last = name.split(" ")
    
jane = Human("Jane", 'Goodall', 30)
"""
print(jane.get_age())
jane.set_age(50)
print(jane.get_age())
"""
print(jane.age) #notice no parentheses #getter
jane.age = 20 #setter
print(jane.age)
# jane.age = -100 #test error
print(jane.fullname)
jane.fullname = "Tim Munchkin"
print(jane.__dict__)