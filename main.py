# Well this is a terminal game of rock , paper, scissors I know,but you have to start somewhere right??
import random
while True:                                                     # The while loop is to enable the player to play another round if he chooses to.
    characters = ["rock","paper","scissors"]   # Array(system) for computer to choose from.

    me = random.choice(characters)                # The computer(me) selects from the array(characters) randomly.

    player = None                                              # The player is initialized.

    while player not in characters:                     # When the player does not choose any of the characters given
        player = print(" Select either rock, paper, or scissors?:>: ").lower()  # Code for player input.
    if player == me:
        print("The computer chooses: ",me)
        print("You choose: ",player)
        print("You Tie!:")                                       # If the system(me) and the player have the same characters then it is a tie.
    elif player == 'rock':
        if me == "paper":
            print("The computer choose: ",me)
            print("You choose: ",player)
            print("You lose")                                   # If the system(me) selects paper and the player selects rock, the player loses.
        if me == "scissors":
            print("The computer chooses: ",me)
            print("You choose: ",player)
            print("You win")                                      # If the system(me) selects scissors and the player selects rock, the player wins.
    elif player == "scissors":
        if me == "rock":
            print("The computer chooses: ",me)
            print("You choose: ",player)
            print("You lose")                                   # If the player selects scissors, and the system selects rock the player loses.
        if me == "paper":
            print("The computer chooses: ",me)
            print("You choose: ",player)
            print("You win")                                    # If the player selects scissors and the system paper the player wins.
    elif player == "paper":
        if me == "scissors":
            print("The computer chooses: ",me)
            print("You choose: ",player)
            print("You lose")                                   # If the player selects paper and the system selects scissors the player loses.
        if me == "rock":
            print("The computer chooses: ",me)                          # If  the player selects paper and the system selects rock  the player wins.
            print("You choose: ",player)
            print("You win")
    continue_playing = input("You can play again just type YES or NO if my game does not interest  you :>:").lower()  # Variable to get the user input
    if continue_playing != "yes": # If the player accepts to play again, the code loops else the code ends
        break
print("You are always welcome to play!!")


