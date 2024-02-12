import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper, scissors?: ")

if player == computer:
    print("You Won")
else:
    print("You lose")
print("Computer choose: "+computer)