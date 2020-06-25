#decorator - a function that wraps other functions, enhancing the behavior of a func being wrapped
# used with "@" syntax

def be_polite(func):
    def wrapper():
        print("Nice to meet you")
        func()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Oleg")

greet()
greet = be_polite(greet)
greet()
greet()
greet()
