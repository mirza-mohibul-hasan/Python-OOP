# For Less Than operator overloading
class sum:
    def __init__(self, x, y):
        self.num = x + y


num1 = sum(50, 20)
num2 = sum(20, 30)
print(num1 < num2)
