# A decorator is a special type of function that can be used to modify the behavior of another function or method. Decorators are often used to extend or enhance the functionality of functions without modifying their actual code.
# A Dispatch decorator is used to select between different implementations of the same abstract method based on the signature, or list of types.
from multipledispatch import dispatch


class mycalculator:
    @dispatch(int, int)
    def sum(self, num1, num2):
        print(num1 + num2)

    @dispatch(int, int, int)
    def sum(self, num1, num2, num3):
        print(num1 + num2 + num3)

    @dispatch(float, float, float)
    def sum(self, num1, num2, num3):
        print(num1 + num2 + num3)

    @dispatch(str, str)
    def sum(self, str1, str2):
        print(str1 + " " + str2 + "!")


# Instance Creation
c1 = mycalculator()
c1.sum(1, 2)
c1.sum(1, 2, 3)
c1.sum(1.5, 2.5, 3.5)

c1.sum("Hello", "World")
