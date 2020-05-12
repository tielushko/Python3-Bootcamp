# Given a person variable:
#   person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# Create a dictionary called answer , that makes each first item in each list a key and the second item
# a corresponding value.  That's a terrible explanation.  I think it'll be easier if you just look at the end goal:
#   {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {item[0]:item[1] for item in person}
print(answer)

#version 2
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

#version 3 - easy
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)