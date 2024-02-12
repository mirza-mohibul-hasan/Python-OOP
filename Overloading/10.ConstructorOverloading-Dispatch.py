from multipledispatch import dispatch


class Student:
    @dispatch(str, int)
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    @dispatch(str, int, float)
    def __init__(self, name, Id, cgpa):
        self.name = name
        self.Id = Id
        self.cgpa = cgpa


s1 = Student("Refat", 190119)
print(s1.name, s1.Id)

s1 = Student("Refat", 190119, 3.07)
print(s1.name, s1.Id, s1.cgpa)
