class Student:
    dept_name = "CSE"

    @classmethod
    def dept_details(cls):
        print("Dept of the student is ", cls.dept_name)
    @classmethod
    def updateDeptName(cls, name):
        cls.dept_name = name


Student.dept_details()
Student.updateDeptName("Computer Science and Engineering")
Student.dept_details()

ob=Student()
print(ob.dept_name)
ob.updateDeptName("CS") #changing class variable for one object effects all the object of that class
ob.dept_details()
Student.dept_details()
