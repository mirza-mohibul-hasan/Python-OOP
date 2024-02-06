name = "mohibul Refat"

print("\nAccess Values: ")
print("**************************")
if(name[0].islower()):
    name = name.capitalize();
print(name)

print("\nCreate substring: ")
print("**************************")
first_name = name[0:7] # name[:7] is also ok
print(first_name)
print("**************************")
last_name = name[8:14] # name[8:] is also ok
print(last_name)

print("\nPrint from last: ")
print("**************************")
print(name[-1])
print(name[-2])
print(name[-3])