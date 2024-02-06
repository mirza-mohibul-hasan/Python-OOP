class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("Student Created")
    def details(self):
        print("Name ",self.name)
        print("ID ",self.id)
#-----------------------------------

s1 = Student("Refat", 190119)
s2 = Student("Sakib", 190116)

# calling instance method-must have to called with object reference
s1.details()
s2.details()