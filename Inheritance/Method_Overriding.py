class Student:
    def __init__(self,name):
        self.name = name

    def attendClass(self):
        print(self.name+" has attended class.")

    def intro(self):
        print("I'm", self.name)

class PrimarySchoolStudent(Student):
    def __init__(self, name,attendingClass):
        super().__init__(name)
        self.attendingClass=attendingClass

    def toDo(self):
        print(self.name+" has nothing to do.")
        print("All day chill...!")

    def attendClass(self):
        print(self.name + " won't go to school")

    def intro(self):
        super().intro()
        print("I study in class",self.attendingClass)
        print()


class EngineeringStudent(Student): #method resolution order -> looks up in the child class first then moves to upper level classes
    def toDo(self):                     # looks for attr or method from left to right for mulitple inheritance
        print(self.name + " has 3 assignments, 2 presentations, 1 project and 2 CTs this week.")
        print("Cry More.....!")

s1 = PrimarySchoolStudent("Muhaimin",3)
s2 = EngineeringStudent("Ayat")

s1.intro()
s1.toDo()
s1.attendClass()
print()
s2.toDo()



