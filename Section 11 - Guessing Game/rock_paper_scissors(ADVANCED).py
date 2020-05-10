from random import randint

response = "y"

while True: 
    limit = int(input("Please enter the winning score of the game!: \n"))
    print("*******\nLet the GAMES BEGIN!!!!")

    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("SHOOOTTTT...\n********************")

    AI_win = 0
    player_win = 0
    round_counter = 1

    while AI_win < limit and player_win < limit:
        print(f"\nRound: {round_counter}\n")
        #assign the moves to the computer and request user input
        rand_num = randint(0,2)
        player = input("Player make a move: ").lower()
        
        #assign the computer move appropriately
        if rand_num == 0:
            computer = "rock"
            print("Computer played: " + computer)
        elif rand_num == 1:
            computer = "paper"
            print("Computer played: " + computer)
        else:
            computer = "scissors"
            print("Computer played: " + computer)

        if player == computer:
            print("It's a tie!")
        elif player == "scissors":
            if computer == "rock":
                print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
                AI_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
            else:
                print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
                player_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
        elif player == "rock":
            if computer == "scissors":
                print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
                player_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
            else:
                print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
                AI_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
        elif player == "paper":
            if computer == "rock":
                print("Player: " + player + " vs. Computer: " + computer + " Player wins!!")
                player_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
            else:
                print("Player: " + player + " vs. Computer: " + computer + " Computer wins!!")
                AI_win += 1
                print(f"Current Score: Computer: {AI_win} vs. Player: {player_win}")
        else: 
            print("Uhoh... incorrect move")
        round_counter += 1
    if (AI_win > player_win):
        print(f"Final Score: Computer: {AI_win} vs. Player: {player_win}. MACHINE DOMINATION MUHAHAHAH")
    elif (AI_win < player_win):
        print(f"Final Score: Computer: {AI_win} vs. Player: {player_win}. PUNY HUMAN DOMINATION MUHAHAHAH")
    else:  
        print("Woah. There was an error in picking a move")
    
    response = input("\n********\nWould you like to play again? (y/n): \n")
    if response == "n":
        break
