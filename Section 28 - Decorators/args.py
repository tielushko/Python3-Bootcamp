#NOT A WORKING CODE, JUST A LEARNING EXAMPLE

#when we write 
@decorator
def func(*args, **kwargs):
    pass

#what we really doing is:
func = decorator(func)

#when we write
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass

#what we really doing is:
func = decorator_with_args(arg)(func)