# tuple = collection which is ordered and unchangable used to group together related data
student = ("Refat", 21, "Male")
print(student)
print("\n Count = ", student.count("Refat"))
print("\n Index = ", student.index("Male"))

for stu in student:
    print(stu)

if "Refat" in student:
    print("Refat is here")