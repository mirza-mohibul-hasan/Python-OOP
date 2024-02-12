#break, continue, pass
while True:
    name = input("Enter your name: ")
    if name != "":
        break

contact = "+88019-9134-7811"
for digit in contact:
    if digit == "-":
        continue
    print(digit, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)