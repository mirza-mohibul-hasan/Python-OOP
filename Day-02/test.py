class Student:

    def __init__(self,id,name) -> None:
        self.name=name
        self.id=id

    def details(self):
        print("Name ",self.name)
        print("ID ",self.id)
        return self.name

    def getName(self):
        return self.name

#Create Object
s1 = Student("Mashrafi", 190116)
s2 = Student("Refat", 190119)

# calling instance method-must have to called with object reference
s1.details()
s2.details()
print(s1.getName())
