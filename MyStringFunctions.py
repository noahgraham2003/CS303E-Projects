# MyStringFunctions
# Noah Graham
# nlg838
# CS303E
# 
# 3/6/23
# This program is a rewritten version of all the functions in the "str" class

s1 = "abcd"
s2 = "efgh"

def myAppend( s, ch ):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for i in s:
        if i == ch:
            count += 1
    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    result = "Empty string: no min value"
    min = "z"
    for i in range(len(s)):
        if s[i] != " ":
            if ord(s[i]) < ord(min):
                min = s[i]
        else:
            print(result)
            return None
    return min

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if i > len(s):
        print("Invalid index")
        return None
    else:
        return s[0:i] + ch + s[i:]

def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    if i >= len(s):
        print("Invalid index")
        return s, None
    else:
        whole = s[0:i] + s[i+1:]
        return whole, s[i]


def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)-1, 0, -1):
        if s[i] == ch:
            return i
        else:
            return -1

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    for i in range(len(s)):
        if s[i] == ch:
            spot = i
            whole = s[0:i-1] + s[i+1:]
            return whole
    return s

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    whole = ""
    last = 0
    for i in range(len(s)):
        if s[i] == ch:
            whole = whole + s[last:i-1]
            last = i
    return s

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.
    newString = s[::-1]
    return newString

print(myAppend( s1, "e" ))
print(myCount( s1, "e"))
print(myCount( s1, "a"))
print(myCount( "abcabc", "a"))
print(myExtend( s1, s2 ))
print(myMin( "" ))
print(myMin( "zqralm" ))
print(myMin( "Hello World!" ))
print(myInsert( "abc", 0, "d"))
print(myInsert( "abc", 2, "d"))
print(myInsert( "abc", 4, "d"))
print(myPop( "abcd", 1 ))
print(myPop( "abcd", 0 ))
print(myPop( "abcd", 5))
print(myFind( "abcdabcd", "a"))
print(myFind( "abcdabcd", "c"))
print(myFind( "abcdabcd", "f"))
print(myRFind("abcdabcd", "d"))
print(myRFind("abcdabcd", "e"))
print(myRemove( "abcdabcd", "a"))
print(myRemove( "abcdabcd", "x"))
print(myRemove( "abcdabcd", "d"))
print(myRemoveAll("abcabcabca", "a"))
print(myReverse( "abcd" ))
print(myReverse( "" ))