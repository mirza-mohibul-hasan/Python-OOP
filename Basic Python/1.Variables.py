name = "Refat" #we can use '' too
print(name)

print('\n'+"*********String********")
print(type(name)) # print data type
first_name = 'Mohibul'
last_name = 'Refat'
print("My name is "+first_name +" "+ last_name)

print('\n'+"*********Integer********")
age = 21
age += 1
print(age)
print(type(age))

print('My age is',age) # dont use + because of concatanation
print('My age is '+str(age)) # Here we are changing data type of integer


print('\n'+"*********Float********")
height = 249.5
height += 1
print(height)
print(type(height))

print("Yout height is",height)
print("Yout height is "+str(height))


print('\n'+"*********Boolean********")

is_true = False
print(is_true)
print(type(is_true))
print("Is true "+str(is_true))

print('\n'+"*********Multiple assignment********")
x = y = z = 40;
print(x, y, z)