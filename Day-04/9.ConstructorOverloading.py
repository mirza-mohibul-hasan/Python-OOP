class Student:
    def __init__(self, **info):  # dictonary
        if len(info) == 3:
            self.name = info['name']
            self.Id = info['Id']
            self.cgpa = info['cgpa']
        elif len(info) == 2:
            self.name = info['name']
            self.Id = info['Id']


s1 = Student(name="Refat", Id=190119)
print(s1.name, s1.Id)

s1 = Student(name="Refat", Id=190119, cgpa=3.07)
print(s1.name, s1.Id, s1.cgpa)
