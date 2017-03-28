import random

moves = ["r", "p", "s"]
player_wins = ["pr","sp", "rs"]

while true:
    player_move = input("Your Move: ")
# This code create a continuous loop - break to stop
    if player_move == "quit":
        break

# computer_move is random
    computer_move = random.choise(moves)

print("Aiden", player_move)
print("Computer", computer_move)
    if player_move == computer_move:
        print("It's a Tie")
    elif player_move + computer_move in player_wins:
        print("Aiden wins")
    else:
        print("You lose!!")
