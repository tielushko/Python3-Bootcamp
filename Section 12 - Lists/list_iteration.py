numbers = [1,2,3,4]

#just print the list
for num in numbers:
    print(num)

print()

#do multiplication with an element in list 
for num in numbers: 
    print(num*num)

print()

#while loop example and getting index
i = 0
while i < len(numbers):
    print(f"{i}: number: {numbers[i]}")
    i += 1

print() 
#list iteration exercise - combining a string in the list
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""

for sound in sounds:
    result += sound.upper()
print(result)