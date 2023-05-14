# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math
# Problem 1: Adjacent Differences
def adjacentDifferences(lst):
    newList = []
    for i in range(0, len(lst)-1, 1):
        newList.append(lst[i+1]-lst[i])
    return newList
    pass

# Problem 2: Unequal Midterms
def computeCourseGrade(m1, m2, m3):
    grade = 0
    list = [m1, m2, m3]
    for i in range(len(list)):
        if list[i] == max(list):
            grade += list[i] * .4
        else:
            grade += list[i] * .3
    grade = math.floor(grade)
    return grade
    pass


def getStudentGrades(lst):
    newList = []
    for i in range(len(lst)):
        newList += [(lst[i][0],computeCourseGrade(lst[i][1], lst[i][2], lst[i][3]))]
    return newList
    pass


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(adjacentDifferences([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, 6]))
    # print(adjacentDifferences([2, 3]))
    # print(adjacentDifferences([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]))

    print(computeCourseGrade(85, 79, 85))
    print(computeCourseGrade(85, 92, 83))
    print(getStudentGrades([["Hannah", 85, 79, 85], ["Eli", 85, 92, 83], ["Elena", 96, 95, 100]]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT