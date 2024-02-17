class Test:
    def __init__(self) -> None:
        pass

class Student:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def details(self):
        print("Name -> ",self.name)
        print("ID -> ",self.id)

    def getName(self):
        return self.name

testObject = Test()

if __name__ == "__main__": # __name__ is a special built-in variable in Python that holds the name of the current module
    #Create Object
    s1 = Student("Mashrafi", 190116)
    s2 = Student("Refat", 190119)

    # calling instance method-must have to called with object reference
    s1.details()
    s2.details()
    print(s1.getName())
