class Test:
    def __init__(self) -> None: # __init__ is a reserved method for python classes
        pass

class Student:
    count=0
    detailsCount=0
    def __init__(self,name,id): # constructor params
        print(self)
        self.name=name
        self.id=id
        
        Student.count+=1

    def details(self):
        print("Name -> ",self.name)
        print("ID -> ",self.id)
        Student.detailsCount+=1

    def getName(self):
        return self.name

if __name__ == "__main__":

    testObject = Test()

    #Create Object
    s1 = Student("Mashrafi", 190116) # constructor arguments
    s2 = Student("Refat", 190119)

    # calling instance method-must have to called with object reference
    s1.details()
    # s2.details()
    print(s1.getName())
    print(Student.count)
    print(Student.detailsCount)

    # print(s1.__dict__) # shows all attributes as a dictionary{key, value}
    # print(dir(s1)) # shows all attributes and methods in a list
