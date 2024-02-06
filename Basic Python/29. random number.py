import random

x  = random.randint(1,6)
y  = random.random()

print(" Random int number between 1 to 6:", x)
print(" Random float number between 0 to 1:", y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(" Random choice among list:", z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print("Shuffle cards:",cards)