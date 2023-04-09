# GuessingGame.py
# Noah Graham
# nlg838
# CS303E
# 
# Date: 2/5/2023
# Description of Program: Randomly selects a number between 1 - 1000 and gives the user 
# 10 guesses to find the random number.
import random
import math
def main():
    answer = int(random.randint(1,999))
    ready = "Y"
    numGuess = int(10)
    print("Welcome to the guessing game! Good luck!")
    while ready == "Y":
        while numGuess > 0:
            ready = input("Are you ready to play (Y/N): ")
            if ready == "N":
                print("\nWell, come again later. Goodbye!")
            elif ready == "Y":
                print("\nSee if you can guess the 'secret number'!")
                userGuess = int(input("\nEnter an integer from 1 to 999: "))
                if userGuess < 1 or userGuess > 999:
                    print("\nThat's an illegal guess.  Try again! You have", numGuess, "guesses left.")
                else:
                    numGuess -= 1
                    if userGuess > answer:
                        print("\nYour guess is too high. Try again! You have", numGuess, "guesses left.")
                    elif userGuess < answer:
                        print("\nYour guess is too low. Try again! You have", numGuess, "guesses left.")
                    else:
                        print("Congratulations, you got it! You took", (10-numGuess), "guesses!")
            else:
                print("\nSorry, I didn't recognize your answer. Try again!")
    if numGuess < 1:
        print("\nSorry! You took too many guesses. The answer was", answer, ". Better luck next time!")







main()