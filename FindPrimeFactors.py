# FindPrimeFactors
# Noah Graham
# nlg838
# CS303E
#
# 3/16/23
# This program detects if an integer is a prime number and lists all of it's prime 
# factors
import math

def isPrime(digit):
    if (digit < 2 or digit % 2 == 0):
        return (digit == 2)
    divisor = 3
    while (divisor <= math.sqrt(digit)):
        if (digit % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findNextPrime(digit):
    if (digit < 2):
        return 2
    if (digit % 2 == 0):
        digit -= 1
    guess = digit + 2
    while (not isPrime(guess)):
        guess += 2
    return guess

print("Find Prime Factors")
while True:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    originalNum = num
    if num == 0:
        print("Goodbye!")
        break
    elif num == 1:
        print("   1 has no prime factorization.")
        print()
    elif num < 0:
        print("   Negative integer entered. Try again.")
        print()
    elif num > 1:
        factors = []
        if isPrime(num) == True:
            factors.append(num)
        else:
            d = 2
            while num > 1:
                while num % d == 0:
                    factors.append(d)
                    num = num / d
                d = findNextPrime(d)
        print("   The prime factorization of", originalNum, "is:", factors)
                