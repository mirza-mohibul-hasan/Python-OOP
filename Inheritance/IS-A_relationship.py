class Student:
    def __init__(self,name):
        self.name = name

    def attendClass(self):
        print(self.name+" has attended class.")

class CSEStudent(Student): #method resolution order -> looks up in the child class first then moves to upper level classes
    def solveProblem(self):
        print(self.name + " is solving problem.")

s1 = CSEStudent("Mahmud")

s1.attendClass()
s1.solveProblem()

