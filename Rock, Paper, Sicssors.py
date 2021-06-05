#This is an basic Rock, Paper, Sicssors program were the player plays against the computer.
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpuScore = 0 # Computer's initial score is 0
playerScore = 0 # Player's initial score is 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
## Game conditions of Rock, Paper and Scissors
    # If the player input is equal to the computer's input.
    if player == computer: #input
        print("We're Tie!")
    #This section details if the player picks "Rock."
    elif player == "Rock": # player's inpu
        if computer == "Paper": # computer's input
            print("Sorry, you lose!", computer, "Paper covers", player)
            cpuScore+=1 # The computer gains one point.
        else:
            print("Wow, You win!", player, " You totally smashed the", computer)
            playerScore+=1 # The player gains one point.
    #This section details if the player picks "Paper."
    elif player == "Paper": #input
        if computer == "Scissors": #input
            print("Sorry, You lose!", computer, "Sicssors cuts", player)
            cpuScore+=1 # The computer gains one point.
        else:
            print("Wow, You win!", player, "You totally cover the", computer)
            playerScore+=1 # The player gains one point.
    #This section details if the player picks "Scissors."
    elif player == "Scissors": #input
        if computer == "Rock": #input
            print("You lose...", computer, " Rock totally smashes", player)
            cpuScore+=1 # The computer gains one point.
        else:
            print("You win!", player, "cut", computer)
            playerScore+=1  # The player gains one point.
    #Player ends the game by typing "End"
    elif player=='End': # input by player
        print("Final Scores:")
        print(f"Computer:{cpuScore}")
        print(f"Player:{playerScore}")
        break # game ends
