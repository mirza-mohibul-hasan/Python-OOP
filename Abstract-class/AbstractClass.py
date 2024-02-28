# Abstract Class -> class that contains one or more abstract method
from abc import ABC, abstractmethod

class Student(ABC): # abstract class -> can't be instantiated
    def __init__(self,name):
        self.name=name
        self.major=None

    @abstractmethod
    def setMajor():
        pass

class CSEStudent(Student): # concrete class
    def __init__(self, name):
        super().__init__(name)
    
    # def setMajor(self):
    #     self.major="CSE"
        
class BBAStudent(Student): # concrete class
    def __init__(self, name):
        super().__init__(name)
    
    # def setMajor(self):
    #     # self.major="BBA"
    #     pass
    
s1=CSEStudent("Ubaid")
# s1.setMajor()
print(s1.major)
s2=BBAStudent("Uthman")
print(s2.major)