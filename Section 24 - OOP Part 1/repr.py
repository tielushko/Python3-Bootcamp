# __repr__ method - allows to define a representation of an instance#used with @classmethod decorator


class User:

    active_users = 0 #serves as a class attribute, and not for each instance of the user.
    
    @classmethod #useful methods for an entire class-level
    def display_active_users(cls): #cls for indicating the passing of the class
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1 #modifies the class attribute variable
    
    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self): #have to pass in self
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} logged out!"

    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th Birthday, {self.first}"

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users) #refers to class attribute, not instance attribute
user2.logout()
print(User.active_users)

print(user1.display_active_users())
print(User.display_active_users())

#how class methods are useful

#Imagine CSV file
tom = User.from_string("Tom,Jones,12")
print(tom.first, tom.last, tom.age)
print(tom.birthday())
print(tom) #instead of printing User at memory reference, it will print nice thing defined in __repr__ method
#User.from_string("Sue,Pritchet,89")
j = User("Jay", "Judy", 16)
print(j)

