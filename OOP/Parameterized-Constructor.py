class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("Student Created")
#-----------------------------------

s1 = Student("Refat", 190119)
s2 = Student("Sakib", 190116)
# Accessing Property
print("s1 name",s1.name)
print("s2 name",s2.name)
s2.name = "Masrafe"
print("s2 name",s2.name)
