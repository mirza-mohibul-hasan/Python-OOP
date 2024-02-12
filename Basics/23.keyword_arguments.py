# There are two types of arguments
# 1. Order 2. Keyword
def printHello(first, middle, last):
    print("My name is", first, middle, last)

print("\nordered arguments\n*****************")
printHello("Hasan", "Mohibul", "Mirza")

print("\nkeyword arguments\n*****************")
printHello(last="Hasan", middle="Mohibul", first="Mirza")