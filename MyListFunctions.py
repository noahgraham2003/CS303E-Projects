# MyListFunctions.py
# Noah Graham
# nlg838
#
# 3/23/23
# This program rewrites list functions

lst1 = ["a", "b", "c"]
lst2 = [1, 2, 3, 4]
lst3 = [1, 2, 3, 1, 2, 3, 1, 2]

def myAppend( lst, x ):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in order.
    newLst = lst1 + lst2
    return newLst


def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    if lst == []:
        print("Empty list: no max value")
        return None
    else:
        max = 0
        for i in range(len(lst)):
            if max < lst[i]:
                max = lst[i]
        return max

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    sum = 0
    for i in lst:
        sum += i
    return sum

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    newLst = []
    if i < 0 or i > len(lst):
        print("Invalid Index")
        return None
    else:
        newLst += lst[:i] + x + lst[i+1:]

def myPop( lst, i ):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    newLst = []
    value = 0
    if i >= len(lst) or i < 0:
        print("Invalid Index")
        return lst, None
    else:
        newLst += lst[:i] + lst[i+1:]
        value = lst[i]
        return newLst, value

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    index = 0
    for i in range(len(lst)):
        if lst[i] == x:
            index = i
            return index
    return -1

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    index = 0
    if x in lst:
        for i in range(len(lst)):
            if lst[i] == x:
                index = i
        return index
    else:
        return -1

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    newLst = []
    for i in range(len(lst)):
        if lst[i] == x:
            newLst += [i]
    return newLst

def myReverse( lst ):
    # Return a new list like lst but with the characters
    # in the reverse order.
    newLst = lst[::-1]
    return newLst

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    newLst = []
    for i in range(len(lst)):
        if lst[i] == x:
            newLst = lst[:i] + lst[i+1:]
            return newLst
    return newLst
    

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    newLst = []
    for i in range(len(lst)):
        if lst[i] != x:
            newLst += [lst[i]]
    if newLst == []:
        return lst
    else:
        return newLst
    

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves. 
    newLst = []
    if i not in lst and j not in lst:
        print("Illegal index value")
    else:
        newlst += "idk"

