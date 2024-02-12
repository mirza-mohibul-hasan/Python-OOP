# For GreaterThan operator overloading
class sum:
    def __init__(self, x, y):
        self.num = x + y

    def __gt__(self, another):
        return self.num > another.num


num1 = sum(50, 20)
num2 = sum(20, 30)
print(num1 > num2)  # num1.__gt__(num2)
