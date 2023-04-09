# Zeller.py
# Noah Graham
# nlg838
# CS303E
#
# 2/5/23
# This program takes a calander date from a user input and shows the corresponding day of the week
import math

def main():

    # Accept the year from the user and convert it to an int.
    Y = int( input("\nEnter year (e.g., 2008): "))
    # If the year is not greater than 1752, print an error
    # message and exit the program. 
    if (Y < 1753):
        print("Year must be > 1752.  Illegal year entered: ", Y, "\n")
        return

    # handle the month similarly
    m = int(input("Enter month (1-12):"))
    if (m < 1 or m > 12):
        print("Month must be in [1..12]. Illegal month entered: ", m, "\n")
        return
    elif m == 1 or m == 2:
        m += 12
        Y -=1 
    
    # handle the day of the month similarly
    d = int(input("Enter day of the month (1-31):"))
    if (d < 1 or d > 31):
        print("\nDay must be in [1..31]. Illegal day entered: ", d, "\n")
        return

    # Compute the other variables, including h
    K = (Y % 100)
    J = (Y // 100)
    h = (( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7)

    # Compute the name of the day from h
    if h == 0:
        print("Day of the week is Saturday")
    elif h == 1:
        print("Day of the week is Sunday")
    elif h == 2:
        print("Day of the week is Monday")
    elif h == 3:
        print("Day of the week is Tuesday")
    elif h == 4:
        print("Day of the week is Wednesday")
    elif h == 5:
        print("Day of the week is Thursday")
    elif h == 6:
        print("Day of the week is Friday")
    else:
        print("Invalid Number")
        return
    # print the day of week message

main()
