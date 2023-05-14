# FunctionExamples.py
# Noah Graham
# nlg838
# CS303E
#
# 2/16/23
# List numerous functions with different purposes

import math

# returns the sum of 3 different numbers
def sum3Numbers(x, y, z):
    return x + y + z

# returns the product of 3 different numbers
def multiply3Numbers(x, y, z):
    return x * y * z

# returns the sum of up to 3 different numbers, with the rest defaulting to zero
def sumUpTo3Numbers(x, y = 0, z = 0):
    return x + y + z

# returns the product of up to 3 different numbers, with the rest defaulting to 1
def multiplyUpTo3Numbers(x, y = 1, z = 1):
    return x * y * z

# prints 2 numbers in ascending order
def printInOrder(x, y):
    if x >= y:
        print(y, x)
    else:
        print(x, y)

# returns the area of a square when given a single positive side
def areaOfSquare(side):
    if side >= 0:
        return side ** 2
    else:
        print("Negative value entered")

# returns the perimeter of a square when given a single positive
def perimeterOfSquare(side):
    if side >= 0:
        return side * 4
    else:
        print("Negative value entered")

# returns the area of a circle when given a positive radius
def areaOfCircle(radius):
    if radius >= 0:
        return math.pi * radius**2
    else:
        print("Negative value entered")

# returns the circumference of a circle when given a positive radius
def circumferenceOfCircle(radius):
    if radius >= 0:
        return 2 * math.pi * radius
    else:
        print("Negative value entered")

# checks if 2 parameters can evenly divide the other and returns the answer
def bothFactors(d1, d2, x):
    if x% d1 == 0 and x% d2 == 0:
        return True
    else:
        return False

# returns the area and circumference of a circle along with the area and perimeter 
# of a square using previous functions.
def squareAndCircle(x):
    print("Circle with radius", x, "has:")
    print("   Area:", areaOfCircle(x))
    print("   Circumference:", circumferenceOfCircle(x))
    print("Square with side", x, "has:")
    print("   Area:", areaOfSquare(x))
    print("   Perimeter:", perimeterOfSquare(x))

# returns the factorial of a positive integer
def factorial(n):
    if n > 0:
        ans = 1
        for i in range(1,n+1):
            ans*= i
        return ans
    else:
        print("Input must be positive")

