print("\n########## Input as string by default ##########")
name = input("What is your name?: ")
age = input("What is your age?: ")
height = input("What is your height?: ")

print("Name", name)
print("Age", age)
print("Height", height)

print("Name type", type(name))
print("Age type", type(age))
print("Height type", type(height))

print("\n"+"########## Input as string by type ##########")
name = input("What is your name?: ")
age = int(input("What is your age?: "))
height = float(input("What is your height?: "))

print("Name", name)
print("Age", age)
print("Height", height)

print("Name type", type(name))
print("Age type", type(age))
print("Height type", type(height))