# Simplest possible class

class User: #capitalized camelcase - convention
    def __init__(self, first, last, age):
        self.first = first
        self.last = last 
        self.age = age

user1 = User("Perry", "Smith", 68)
user2 = User("Joe", "Lopez", 41)

print(user1.first, user1.last)
print(user2.first, user2.last)

