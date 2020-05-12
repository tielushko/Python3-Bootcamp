#declare dictionary

cat = {"name": "Blue", "age": 3.5, "isCute": True}
print(cat)

another_dict = dict(name="kitty", age = 3.5, isCute = False)
print(another_dict)

print()
#Accessing value 
cat["name"] #Blue

#use .value()
print(cat.values())

#use .keys()
print(cat.keys())

print() 
for key in cat.keys():
    print(f"{key}:  {cat[key]}")
print()

#use .items()
print(cat.items())

for key, value in cat.items():
    print(f"Key is {key} and value is {value}")
print()

#testing presence of a key in dict
print("name" in cat) #True
print("color" in cat) #False

print() 

#testing presence of a value
print("Blue" in cat.values())
print("Kitty" in cat.values())

#methods

#clear - remove everything in dictionary

#copy - make a copy of a dictionary

#fromkeys - creates key-value pairs from csv - gotta pass iterable object as first argument!
dic = {}.fromkeys("a", "b")

new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], None) # helpful in creating default dicts

new_user.fromkeys('phone', None)

#get - retrieves a key in an object and returns None instead of KeyError when key DNE

#pop - have to provide the key of an item to remove the key-value pair from the dictionary. If popping non-existing element, error
#pop returns the value from the given key

#.popitem() - removes the last item from the dictionary

#.update(some dict) used to combine dictionaries together 
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite an existng key
second['a'] = "AMAZING"

# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}