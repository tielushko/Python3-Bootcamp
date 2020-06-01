#convention put __ methods above all other methods

class User:

    active_users = 0 #serves as a class attribute, and not for each instance of the user.
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1 #modifies the class attribute variable
    
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

"""
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user1.age)
print(user2.full_name())
print(user1.initials())
print(user1.likes("Candy"))
print(user2.likes("Ice cream"))
print(user1.is_senior())
print(user2.is_senior())
print(user1.birthday())
print(user2.birthday())
"""