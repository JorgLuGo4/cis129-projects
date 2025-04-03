#Script: The Dice Game 
#Action: This code chooses two players and rolls a dice randomly to decide whoever wins.
#Author: Jorge Lucero
#Date: 4/02/25
import random

# the main function 
def main(): 
    print()
    
    # initialize variables 
    endProgram = 'no'  
    # while loop to run the program again
    while endProgram.lower() == 'no':  # continue loop until user says "yes"
        # populate variables 
        player1_name, player2_name = inputNames()  # plater's names
        player1_roll, player2_roll = rollDice()  # rolls

        # call to displayInfo 
        displayInfo(player1_name, player2_name, player1_roll, player2_roll)

        endProgram = input('Do you want to end program? (yes/no): ')  
    
# this function gets the players' names 
def inputNames():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    return player1_name, player2_name

# this function will get the random values (dice rolls)
def rollDice():
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)
    return player1_roll, player2_roll

# this function displays the winner 
def displayInfo(player1_name, player2_name, player1_roll, player2_roll):
    print(f"{player1_name} rolled a {player1_roll}")
    print(f"{player2_name} rolled a {player2_roll}")
    
    # who wins or if there's a tie
    if player1_roll > player2_roll:
        print(f"{player1_name} wins")
    elif player2_roll > player1_roll:
        print(f"{player2_name} wins")
    else:
        print("It's a tie")  # if both role the same, it is a tie

# calls main
main()
