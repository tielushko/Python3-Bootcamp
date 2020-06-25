from random import choice
#we can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAH', 'lol', 'teheeee'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())