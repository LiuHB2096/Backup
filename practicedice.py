# Henry Liu
# Period 4
# Dice Rolling Simulator

import random

rollNumber = 0
1s = 0
2s = 0
3s = 0
4s = 0
5s = 0
6s = 0

print ("Welcome to the Dice Rolling Simulator!")
playerChoice = int(input("How many times would you like to roll the dice? "))

while True:
	rollNumber = rollNumber + 1
	randomNum = random.randint(1,6)
	