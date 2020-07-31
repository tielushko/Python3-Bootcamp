def enforce(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return func(*newargs, **kwargs)
        return wrapper
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a, b):
    print(a / b)


repeat_msg("Hello", '3')    
divide('1', '2')

"""
creates tuples ("Hello", str) ('3', int)
casts (line 7) the type onto the 1st element in tupple
adds to list (line 7)
returns new args.
"""