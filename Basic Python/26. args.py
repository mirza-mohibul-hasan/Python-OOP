# *args is parameter thar will pack all arguments into a tuple. It is useful so that a functiom can accept a varying amount of arguments
# if you want to change touples then typecast it into list

def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))