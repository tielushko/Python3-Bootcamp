import time

#generators from generator expressions

def nums():
    for num in range(10):
        yield num

#instead
"""
g = (num for num in range(10)) #g is a generator object and is iterable -> notice how we enclose generator expression in ()
s = sum(num for num in range(10))
print(s)
"""

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_tot = time.time() - gen_start_time
print(gen_tot)

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_tot = time.time() - list_start_time
print(list_tot)
