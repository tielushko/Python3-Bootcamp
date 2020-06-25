from random import choice
#inner functions can access outer functions scope (EX: person that was passed into outer, but can be accessed in inner (get_laugh))
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAH', 'lol', 'teheeee'))
        return f"{laugh} {person}"
    return get_laugh

laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())