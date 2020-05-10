from random import randint

number = 0
i = 0

while number != 5:
    number = randint(1, 10)
    i += 1
    print(f"Number generated {number} and this is {i} iteration")
print("Reached 5... exiting")