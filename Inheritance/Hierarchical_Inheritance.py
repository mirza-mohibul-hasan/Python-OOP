class Student:
    def __init__(self,name):
        self.name = name

    def attendClass(self):
        print(self.name+" has attended class.")

class PrimarySchoolStudent(Student):
    def toDo(self):
        print(self.name+" has nothing to do.")
        print("All day chill...!")


class EngineeringStudent(Student): #method resolution order -> looks up in the child class first then moves to upper level classes
    def toDo(self):                     # looks for attr or method from left to right for mulitple inheritance
        print(self.name + " has 3 assignments, 2 presentations, 1 project and 2 CTs this week.")
        print("Cry More.....!")

s1 = PrimarySchoolStudent("Muhaimin")
s2 = EngineeringStudent("Ayat")

s1.toDo()
print()
s2.toDo()

