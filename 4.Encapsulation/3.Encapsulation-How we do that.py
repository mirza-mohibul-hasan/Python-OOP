# for making method private we use double _
# python doesn't have keyword to do that
# __something is called dunder, name mangling
class Student:
    def __init__(self, name, id, dept) -> None:
        self.name = name
        self.__id = id
        self.dept = dept

    def display(self):
        print(f"Student ID:{self.__id}")
        print(f"\tName:{self.name}")
        print(f"\tDept:{self.dept}")


# step-01
s1 = Student("Arafat", 190122, "CSE")
s1.display()

# step-02
# print(s1.name)
# print(s1.__id)

# step-03
# s1.__id = -524

# step-04
# s1.display()
# print(s1.__dict__)
