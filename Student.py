# Student.py
# Noah Graham
# nlg838
# CS303E
# 
# 2/29/23
# This program contains a Student class that allows the user to initialize a student object with two exam grades,
# a name, and an average and allows for the "getting" and "setting" of the test grades plus a formated print layout.

class Student:

    def __init__(self, name, exam1=None, exam2=None):
        self.name = name
        self.test1 = exam1
        self.test2 = exam2
    
    def getExam1Grade(self):
        return self.test1
    
    def setExam1Grade(self, exam1):
        self.test1 = exam1

    def getExam2Grade(self):
        return self.test2
    
    def setExam2Grade(self, exam2):
        self.test2 = exam2
    
    def getAverage(self):
        if self.test1 != None and self.test2 != None:
            return ((self.test1 + self.test2)/2)
        else:
            return "Some exam grades not available."
    
    def __str__(self):
        return "Student: "+ str(self.name)+ "\n   Exam 1 " + str(self.test1)+ "\n   Exam 2: " + str(self.test2)
