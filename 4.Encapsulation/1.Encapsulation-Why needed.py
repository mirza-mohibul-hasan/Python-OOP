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

# We don't want to update ID like this
s1.id = -524

s1.display()

# Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object.

# It essentially means binding variables and methods together into a single unit and preventing them from being accessed by other classes.
