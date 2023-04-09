# Project1.py
# Noah Graham
# nlg838
# CS303E
#
# 2/22/23
# This program is a playable game of rock paper scissors. The player inputs
# a play and the program randomly picks another choice. The number of 
# games and win/loss/tie percentages are displayed if asked to.

import random

ROCK = "1"
PAPER = "2"
SCISSORS = "3"

def machinePlay ():
    # This chooses one of the three moves randomly.
    play = random.choice([ROCK, PAPER, SCISSORS])
    return play

def playName(play):
    # This is supposed to print out the correct value
    if play == "1":
        return "rock"
    if play == "2":
        return "paper"
    if play == "3":
        return "scissors"

def printStats( plays, wins, losses, draws ):
    # This neatly prints out the stats of the games given these 4 variables
    print("Game statistics:")
    print("   Games played:", plays)
    print("   You won:     ", wins,   " (", format((wins/plays), "4.1%"), ")", sep="")
    print("   You lost:    ", losses, " (", format((losses/plays), "4.1%"), ")", sep="")
    print("   No winner:   ", draws,  " (", format((draws/plays), "4.1%"), ")", sep="")

def game(user, comp):
    # This runs the actual RPS game and returns either 0, 1, or 2 based on the outcome.
    print("You played ", playName(user), "; your opponent played ", playName(comp), sep="")
    if user == "1":
        if comp == "1":
            print("There's no winner. Try again!")
            return 0
        elif comp == "2":
            print("Sorry, you lost")
            return 1
        elif comp == "3":
            print("Congratulations, you won!")
            return 2
    elif user == "2":
        if comp == "1":
            print("Congratulations, you won!")
            return 2
        elif comp == "2":
            print("There's no winner. Try again!")
            return 0
        elif comp == "3":
            print("Sorry, you lost")
            return 1
    elif user == "3":
        if comp == "1":
            print("Sorry, you lost")
            return 1
        elif comp == "2":
            print("Congratulations, you won!")
            return 2
        elif comp == "3":
            print("There's no winner. Try again!")
            return 0
            

def main():
    # This is the main function that starts the game and runs the menu
    gamesWon = 0
    gamesLost = 0
    noWinners = 0
    gamesPlayed = 0
    playing = True
    print("\nWelcome to a game of Rock, Paper, Scissors!")
    
    while playing == True:
        print()
        print("Choose your play:")
        print("   Enter 1 for rock;")
        print("   Enter 2 for paper;")
        print("   Enter 3 for scissors;")
        userInput = str(input("   Enter 4 to exit: "))
        if userInput == "1" or userInput == "2" or userInput == "3":
            result = game(userInput,machinePlay())
            if result == 1:
                gamesLost += 1
            elif result == 2:
                gamesWon += 1
            elif result == 0:
                noWinners += 1
            gamesPlayed += 1
        elif userInput == "4":
            if gamesPlayed > 0:
                printStats(gamesPlayed, gamesWon, gamesLost, noWinners)
                print("Thanks for playing. Goodbye!")
                playing = False
            elif gamesPlayed == 0:
                print("No games were completed.")
                print("Thanks for playing. Goodbye!")
        else:
            print("Illegal play entered. Try again!")


main()