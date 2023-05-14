# Noah Graham
# noahgraham2003@gmail.com
# 940-447-4663
#
# This code is a buzzfeed quiz that determines wich Avenger you are 

def avenger():
    if ironMan > thor and ironMan > captainAmerica and ironMan > hulk and ironMan > blackWidow and ironMan > hawkeye:
        print("You are Iron Man")
    if thor > ironMan and thor > captainAmerica and thor > hulk and thor > blackWidow and thor > hawkeye:
        print("You are Thor")
    if captainAmerica > thor and captainAmerica > ironMan and captainAmerica > hulk and captainAmerica > blackWidow and captainAmerica > hawkeye:
        print("You are Captain America")
    if hulk > thor and hulk > captainAmerica and hulk > ironMan and hulk > blackWidow and hulk > hawkeye:
        print("You are Hulk")
    if blackWidow > thor and blackWidow > captainAmerica and blackWidow > hulk and blackWidow > ironMan and blackWidow > hawkeye:
        print("You are Black Widow")
    if hawkeye > thor and hawkeye > captainAmerica and hawkeye > hulk and hawkeye > blackWidow and hawkeye > ironMan:
        print("You are Hawkeye")

play = True
while play == True:
    ironMan = 0
    thor = 0
    captainAmerica = 0
    hulk = 0
    blackWidow = 0
    hawkeye = 0

    print("Welcome to 'Which Avenger Are You?'")
    print()
    ready = input("Are you ready to play? (Y/N)")
    if ready == "N":
        print("Have a great day!")
        break
    elif ready == "Y":
        print("Question 1:\nWhich weapon would you choose in a battle?\na. Suit of armor\nb. Magic Hammer\nc. Shield\nd. Your fists\ne. Martial arts\nf. Bow and Arrow")
        ans1 = input("")
        if ans1 == "a":
            ironMan += 1
        elif ans1 == "b":
            thor += 1
        elif ans1 == "c":
            captainAmerica += 1
        elif ans1 == "d":
            hulk += 1
        elif ans1 == "e":
            blackWidow +=1
        elif ans1 == "f":
            hawkeye += 1
        print("Question 2:\nThe battle is over. What home do you want to go back to?\na. Mansion in the hills\nb. A Golden Palace\nc. Cabin in the woods\nd. I live in the lab\ne. Somewhere new\nf. Wherever my family is")
        ans2 = input("")
        if ans2 == "a":
            ironMan += 1
        elif ans2 == "b":
            thor += 1
        elif ans2 == "c":
            captainAmerica += 1
        elif ans2 == "d":
            hulk += 1
        elif ans2 == "e":
            blackWidow +=1
        elif ans2 == "f":
            hawkeye += 1
        
        avenger()
        break
        
