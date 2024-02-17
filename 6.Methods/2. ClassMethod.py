class Student:
    dept_name = "CSE"

    @classmethod
    def dept_details(cls):
        print("Dept of the student is ", cls.dept_name)


Student.dept_details()
