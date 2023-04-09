# Handicap.py
# Noah Graham
# nlg838
# CS303E
#
# 1/21/23
# This program takes the input of a bowler's name and their last 3 games to calculate their
# bowling averages. Then it calculates their handicap and displays the average and handicap
# in a clean format.

name = input("Enter bowler's name: ")
game1 = int(input("Enter Game 1: "))
game2 = int(input("Enter Game 2: "))
game3 = int(input("Enter Game 3: "))

average = int((game1 + game2 + game3)//3)
handicap = max(0, int((200 - average) * .8))

print()
print("Handicap report for ", name, ":", sep="")
print("  ", name,"'s average is: ", average, sep="")
print("  ", name,"'s handicap is: ", handicap, sep="")
print()
print("It's time to Bowl!")