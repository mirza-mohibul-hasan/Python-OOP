class Student:
    def __init__(self, name) -> None:
        self.name = name

    def details(self):
        print("Name of the student is ", self.name)


student1 = Student("Aowal Aowal")
student1.details()
