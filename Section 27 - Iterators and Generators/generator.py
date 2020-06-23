#generator - a special type of iterator. All generators are iterators, but not all iterators are generators.
# reg func vs generator functions
"""
    uses return     vs      uses yield
    returns once    vs      can yield multiple times
    returns value   vs      returns a generator
"""

def count_to_max(max):
    count = 1
    while count <= max:
        yield count
        count += 1

print(count_to_max(5)) #gives generator object
counter = count_to_max(5)
print(next(counter))
print(next(counter))

for count in counter: 
    print(count)


'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

def week():
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in days:
        yield day


'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    choice = 'yes'
    while True:
        yield choice
        choice = 'no' if choice == 'yes' else 'yes'