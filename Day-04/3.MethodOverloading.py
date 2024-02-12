class mycalculator:
    def sum(self, num1=None, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1 + num2 + num3)
        elif num1 != None and num2 != None:
            print(num1 + num2)
        else:
            print(num1)


c1 = mycalculator()
c1.sum(1)
c1.sum(1, 2)
c1.sum(1, 2, 3)
