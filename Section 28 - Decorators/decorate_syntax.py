def be_polite(func):
    def wrapper():
        print("Nice to meet you")
        func()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Oleg") 

#we don't need to set   greet = be_polite(greet)

greet()
