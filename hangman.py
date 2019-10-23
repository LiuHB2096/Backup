# Henry Liu
# Period 4

print("Welcome to Hangman!")



myWord = "hello"


while True:
	choice = input("What do you think the word is? ")

	if choice == myWord:
		print("That's a match! ")
		break
	else:
		print("That isn't a match. ")

letter = input("Type in a letter. ")
if letter in myWord:
	print("The letter is in the word. ")	
else: 
	print("The letter isn't in the word. ")


count = 0
for l in myWord:
	if l == letter:
		print(count)
	count += 1




import time
import os

#how to turn a string in to a list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list _ where the letters go
guessList = []
for a in myList:
	guessList.append("_")

print(guessList)

# how to replace a specific item in list
# so say the user types r for a guess, you would 
guessList[1] = "r"
print(guessList)


secretWord = "christmas"
secretWord = list(secretWord)
hangmanList = ['''
   +==========+
   			  |
   			  |
   			  |
   			  |
	===========|''' , "second", "thrid" ]


misses = 0
while misses > 7:
	guess = input("Guess a letter. ")
	if guess in secretWord:
		# loop through secretWord and change my guessList at the correct indexes

	else:
		misses += 1
		print(hangmanList[misses])

		
print("game over")