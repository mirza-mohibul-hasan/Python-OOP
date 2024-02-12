"""
Method overloading is a concept that allows a class to define multiple methods with the same name, but different signatures. This means that different methods can respond to different messages sent to an instance of the class.
"""


class mycalculator:
    def sum(self, num1, num2):
        print(num1 + num2)

    def sum(self, num1, num2, num3):
        print(num1 + num2 + num3)


# Instance Creation
c1 = mycalculator()
c1.sum(1, 2)
c1.sum(1, 2, 3)
