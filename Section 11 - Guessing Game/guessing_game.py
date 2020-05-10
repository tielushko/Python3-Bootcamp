from random import randint

play = "y"

while play != "n":
    random_number = randint(1, 10)
    answer = int(input("Guess a number between 1 and 10:"))
    while answer != random_number:
        if answer > random_number:
            print("Too high, try again")
        else:
            print("Too low try again")
        answer = int(input("Guess a number between 1 and 10:"))
    print("Yay! You answered it correctly. You won!")
    play = input("Do you want to play again? (y/n) \n")
print("Thank you for playing! Bye!")
