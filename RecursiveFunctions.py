# File: RecursiveFunctions.py
# Student: Noah Graham
# UT EID: nlg838
# Course Name: CS303E
# 
# Date: 4/7/23
# Description of Program: List of functions that use recursion

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
      return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   if n == 0:
      return 0
   else:
      return n + addToN(n-1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n < 10:
      return n
   else:
      lastDigit = n%10
      updateNumber = n//10
      return lastDigit + findSumOfDigits(updateNumber)

def integerToBinary( n ): # doesn't work correctly
   """ Given a nonnegative integer n, return the 
   binary representation as a string. """
   if n == 0:
      return "0"
   elif n == 1:
      return "1"
   else:
      return integerToBinary(n//2) + str(n%2)

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the 
   digits (as strings). """
   if n < 10:
      return [str(n)]
   else:
      lastDigit = n%10
      updateNumber = integerToList(n//10)
      return updateNumber + [lastDigit]


def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if len(s) < 2:
      return True
   if s[0] == s[-1]:
      return isPalindrome(s[1:-1])
   else:
      return False

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if len(s) == 0:
      return None
   elif s[0].isupper() == True:
      return s[0]
   else:
      return findFirstUppercase(s[1:])


# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if len(s) == 0:
      return None
   elif s[-1].isupper() == True:
      return s[-1]
   else: 
      return findLastUppercase(s[:-1])


def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the index of the first uppercase letter;
   assume you are starting at index. Return -1 
   if there is none."""
   if len(s) == 0:
      return -1
   elif s[0].isupper():
      return index
   else:
      return findFirstUppercaseIndexHelper(s[1:], index + 1)

# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )

print(addToN( 10 ))
print(addToN( 100 ))
print(addToN( 0 ))
print(findSumOfDigits( 0 ))
print(findSumOfDigits( 12345 ))
print(integerToBinary( 25 ))
print(integerToBinary( 100 ))
print(integerToBinary( 0 ))
print(integerToList( 123 ))
print(integerToList( 348914 ))
print(integerToList( 0 ))
print(isPalindrome( "abcDcba" ))
print(isPalindrome( "abcDcbaF" ))
print(isPalindrome( "" ))
print(isPalindrome( "X" ))
print(findFirstUppercase( "ab c  dEFg hi" ))
print(findFirstUppercase( "ab c  defg hi" ))
print(findLastUppercase("ABcdE Fghi"))
print(findLastUppercase(""))
print(findLastUppercase("abcdefghi"))
print(findFirstUppercaseIndexHelper("abCd", 7))
print(findFirstUppercaseIndexHelper("abCd", 10))
print(findFirstUppercaseIndexHelper("abcd", 10))
print(findFirstUppercaseIndexHelper("abCd", 0))
print(findFirstUppercaseIndex("abCd"))
print(findFirstUppercaseIndex( "ab c  dEFg hi" ))
print(findFirstUppercaseIndex( "ab c  defg hi" ))
print(findFirstUppercaseIndex( "" ))
