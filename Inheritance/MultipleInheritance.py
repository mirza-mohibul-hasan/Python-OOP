class Student:
    def __init__(self,name):
        self.name = name

    def attendClass(self):
        print(self.name+" has attended class.")

class EngineeringStudent():
    def __init__(self,name):
        self.name=name
    def attendLab(self):
        print(self.name+" has attended lab.")


class CSEStudent(Student,EngineeringStudent): #method resolution order -> looks up in the child class first then moves to upper level classes
    def solveProblem(self):                     # looks for attr or method from left to right for mulitple inheritance
        print(self.name + " is solving problem.")

s1 = CSEStudent("Mahmud")

s1.attendLab()

