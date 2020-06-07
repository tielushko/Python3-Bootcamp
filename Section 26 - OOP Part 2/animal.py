class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        #uncommon
        # Animal.__init__(self, name, species)
        # super refers to the base class - in Cats super refers to animal
        super().__init__(name, species) 
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat('Blue', 'Cat', 'Scottish fold', 'String')
print(blue)
blue.play()