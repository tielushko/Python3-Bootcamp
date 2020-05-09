# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for odd in range(11,21,2):
    x += odd
print(x)

#for 4 and 13 print "x is unlucky"
#for even numbers print "x is even"
#for odd numbers print "x is odd"

for number in range(1,21):
    if number == 4 or number == 13:
        state = "unlucky"
    elif number % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{number} is " + state)

