class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound("MEOW")
print(blue.cool)
print(Cat.cool)
print(Animal.cool)
print(isinstance(blue, Animal))
print(isinstance(blue, Cat))

