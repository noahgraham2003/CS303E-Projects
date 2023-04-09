# CS 303E Quiz 1
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Fan Fiction Financials
def fanFictionFinancials():
    # write your solution to problem 1 here
    w = float(input(""))
    c = float(input(""))
    f = float(input(""))
    profit = (w/(50*c))**3 + math.sqrt(c**3 + f/5)
    print("Your friend will gain $", round(profit,2),sep="")
    pass


# Problem 2: Cake Baking
def cakeBaking():
    # write your solution to problem 2 here
    e = float(input(""))
    b = float(input(""))
    p = float(input(""))
    e2 = e / 3
    b2 = b / 1.4
    p2 = p / 2.3
    cake = e2
    if cake > b2:
        cake = b2
    if cake > p2:
        cake = p2
    cake = math.floor(cake)
    print(cake)
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # fanFictionFinancials()
    cakeBaking()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT