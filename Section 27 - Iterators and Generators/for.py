#Custom for loop

#for num in [1,2,3] #inside the for loop: iter([1,2,3]) -> returns iterator, then for loop keeps calling next(iter([1,2,3])) until catches error

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break   
        else: 
            func(item)
            
def square(x):
    print(x*x)


my_for("Hello", print)
print()
my_for([1,2,3,4,5], square)