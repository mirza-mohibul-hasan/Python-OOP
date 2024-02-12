class Student:
    def __init__(self, *info):  # tuple, index should be remembered
        if len(info) == 3:
            self.name = info[0]
            self.Id = info[1]
            self.cgpa = info[1]
        elif len(info) == 2:
            self.name = info[0]
            self.Id = info[1]


s1 = Student("Refat", 190119)
print(s1.name, s1.Id)

s1 = Student("Refat", 190119, 3.07)
print(s1.name, s1.Id, s1.c)
