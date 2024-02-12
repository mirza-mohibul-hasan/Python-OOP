class mycalculator:
    def sum(self, *nums):  # nums is tuple here
        sum = 0
        for num in nums:
            sum += num
        print(sum)


c1 = mycalculator()
c1.sum(1)
c1.sum(1, 2)
c1.sum(1, 2, 3)
c1.sum(1, 2, 3, 4)
