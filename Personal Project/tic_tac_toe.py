board = [[" " for i in range(3)] for j in range(3)]

def print_board():
    for row in board:
        print("----------------")
        print("    |     | ")
        output = " " + row[0] + "  |  " + row[1] + "  |  " + row[2]
        print(output) 
        print("    |     | ")
        print("----------------")

win_state = False

print("Welcome to the Tic Tac Toe Game")  
x_or_o_player = input("Would you like to play as an X or an O?")

if x_or_o_player == "X":
    x_or_o_AI = "O"
elif x_or_o_player == "O": 
    x_or_o_AI = "X"
else: 
    print("Invalid Input")
