from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOOTTTT...")

rand_num = randint(0,2)

player = input("Player make a move: ").lower()

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

if player == computer:
    print("It's a tie!")
elif player == "scissors":
    if computer == "rock":
        print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
    else:
        print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
elif player == "rock":
    if computer == "scissors":
        print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
    else:
        print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
elif player == "paper":
    if computer == "rock":
        print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
    else:
        print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
else: 
    print("Uhoh... incorrect move")
