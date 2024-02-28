# Abstract Class -> class that contains one or more abstract method
from abc import ABC, abstractmethod

class Student(ABC): # abstract class -> can't be instantiated
    def __init__(self,name):
        self.name=name
        self.major=None
        self.faculty=None

    @abstractmethod
    def setFaculty():
        pass

class EngineeringStudent(Student): # abstract class
    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def setFaculty(self):
        pass
        
class CSEStudent(EngineeringStudent): # concrete class
    def __init__(self, name):
        super().__init__(name)
    
    def setMajor(self):
        self.major="CSE"
    def setFaculty(self):
        self.faculty="Engineering"
        
    
s1=CSEStudent("Ubaid")
# s1.setMajor()
s1.setFaculty()
print(s1.faculty)