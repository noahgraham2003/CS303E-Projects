# Student.py
# Noah Graham
# nlg838
# CS303E
# 
# 2/29/23
# Description of Program: 

class Student:

    def __init__(self, exam1=None, exam2=None):
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
        return self.test1
    
    def print(self):
        print("Student:", self)
        print("   Exam1:", self.test1)
        print("   Exam2:", self.test2)
