# Python doesn't have access modifier
# we need to use conventional ways
class Student:
    def __init__(self, name, id, dept) -> None:
        self.name = name
        self.id = id
        self.dept = dept

    def display(self):
        print(f"Student ID:{self.id}")
        print(f"\tName:{self.name}")
        print(f"\tDept:{self.dept}")


s1 = Student("Arafat", 190122, "CSE")
s1.display()

s1.id = -524

s1.display()
