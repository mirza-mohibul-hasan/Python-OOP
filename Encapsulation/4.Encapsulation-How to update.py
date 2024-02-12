# Updating ID
class Student:
    def __init__(self, name, id, dept) -> None:
        self.name = name
        self.__id = id
        self.dept = dept

    def display(self):
        print(f"Student ID:{self.__id}")
        print(f"\tName:{self.name}")
        print(f"\tDept:{self.dept}")

    def update_Id(self, id):
        if (id > 0):
            self.__id = id
        else:
            print("Invalid ID")


# step-01
s1 = Student("Arafat", 190115, "CSE")
s1.display()

# step-02
s1.update_Id(-524)
s1.update_Id(190122)

# step-03
s1.display()
print(s1.__dict__)
