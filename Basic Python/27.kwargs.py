# *kwargs is parameter thar will pack all arguments into a dictonary. It is useful so that a functiom can accept a varying amount of keyword arguments
def printHelloStructure(**kwargs):
    print("\nStructure\n**********")
    print(kwargs)

def printHelloKeyword(**kwargs):
    print("\nName normal way\n**********")
    print("Hello",kwargs['first'],kwargs['middle'],kwargs['last'])

def printHelloIterate(**kwargs):
    print("\nName normal way\n**********")
    print("Hello ", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

printHelloStructure(first = "Mirza", middle="Mohibul", last = "Hasan")

printHelloKeyword(first = "Mirza", middle="Mohibul", last = "Hasan")

printHelloIterate(first = "Mirza", middle="Mohibul", last = "Hasan")