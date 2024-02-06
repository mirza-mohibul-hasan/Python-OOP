rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol: ")

for row in range(0, rows):
    for col in range(0, columns):
        print(symbol, end="")
    print()