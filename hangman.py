# Henry Liu# Henry Liu
# Period 4


import random
mysteryWord = ['boxes', 'france', 'frogs','mouse', 'black', 'table']
secretWord = random.choice(mysteryWord)

myList = list(secretWord)


guesses = []
correctLetters = []
wrongLetters = []

correct = 0
wrong = 0

print("WELCOME TO HANGMAN! ")
print()

while True:
    print()
    try:
        misses = int(input("How many wrong chances would you like to guess the word? "))
    except ValueError:
        print("Please pick an integer. ")
        continue
    else:
        break



print("Try to guess the word in under " + str(misses) + " wrong guesses!")
print("The word has " + str(len(secretWord)) + " letters. ")

for letter in myList:
  correctLetters.append("_")
print(correctLetters)


while True:
  playerLetter = input("Please pick one letter from the alphabet that would be your guess. ")

  if playerLetter in myList:
    index = myList.index(str(playerLetter))
    correctLetters.pop(int(index))
    correctLetters.insert(int(index), playerLetter)
    print(correctLetters)
    
    print("The letter " + str(playerLetter) + " is in the word! ")
    print("Wrong guess #" + str(wrong))
    print("These are your wrong guesses: " + str(wrongLetters))


  if playerLetter not in myList:
    print()
    print(correctLetters)
    print("The letter " + str(playerLetter) + " is not in the word. ")
    wrong = wrong + 1
    print()
    print("Wrong guess #" + str(wrong))
    wrongLetters.append(playerLetter)
    print("These are your wrong guesses: " + str(wrongLetters))
  if correctLetters[0] == myList[0] and correctLetters[1] == myList[1] and correctLetters[2] == myList[2] and correctLetters[3] == myList[3] and correctLetters[4] == myList[4]:
    print("CONGRATULATIONS!!! ")
    print("You have guessed the word " + str(secretWord) + "!")
    break
  
  if int(wrong) == int(misses):
    print()
    print("GAME OVER!!!") 
    print("You have ran out of got ran out of wrong guesses. The correct word was " + secretWord + ". ")
    break
