# We use Getter and Setter to access private like instances
class Student:
    def __init__(self, name, id, dept) -> None:
        self.__name = name
        self.__id = id
        self.__dept = dept

    def display(self):
        print(f"Student ID:{self.__id}")
        print(f"\tName:{self.__name}")
        print(f"\tDept:{self.__dept}")

    def set_Id(self, id):
        if (id > 0):
            self.__id = id
        else:
            print("Invalid ID")

    def get_Id(self):
        return self.__id

    def set_Name(self, name):
        self.__name = name

    def get_Name(self):
        return self.__name

    def set_Dept(self, dept):
        self.__dept = dept

    def get_Dept(self):
        return self.__dept


# step-01
s1 = Student("Arafat", 190115, "CSE")
s1.display()

# step-02
# s1.set_Id(-524)
# s1.set_Id(190116)

# step-03
# s1.set_Name("Masrafe")

# step-04
# s1.set_Dept("NHS")

# step-05
# print(s1.get_Id())
# print(s1.get_Name())
# print(s1.get_Dept())

# step - 06
# s1.display()
