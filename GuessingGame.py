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
    bigPlay = True
    print("Welcome to the guessing game! Good luck!")
    while bigPlay == True:
        numGuess = int(10)
        ready = input("\nAre you ready to play (Y/N): ")
        if ready == "N":
            print("\nWell, come again later. Goodbye!")
            bigPlay = False
        elif ready != "Y" and ready != "N":
            print("\nSorry, I didn't recognize your answer. Try again!")
        if ready == "Y":
            print("\nSee if you can guess the 'secret number'!")
            while ready == "Y" and numGuess > 0:
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
                        ready = "N"
            if numGuess < 1:
                print("\nSorry! You took too many guesses. The answer was", answer, ". Better luck next time!")



main()