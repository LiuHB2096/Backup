# # Henry Liu
# Period 4

# list for computer to pick from
import random
myWords = ['socks', 'turtle', 'shelf', 'boxes', 'books', 'screw']
secretWord = random.choice(myWords)

# introduction
print("Welcome to HANGMAN! ")
print()
while True:
  print()
  try:
    misses = int(input("How many chances would you like to guess the word? "))
  except ValueError:
    print()
    print("Please enter a number. ")
  else:
    break
print()
print("Try to guess the word in under " + str(misses) + " guesses! ")
print()
print("The word has " + str(len(secretWord)) + " letters. ")
print()


# to print secretWord blank spaces
blanks = ' [_] ' * len(secretWord)
print(blanks)

# correctLetters code
# wrongLetters Code
# number of guesses code


while True:
  print()
  playerLetter = input("Guess a letter from the alphabet. ")
  playerLetter = playerLetter.lower()
  if playerLetter not in 'abcdefghijklmnopqrstuvwxyz':
    print()
    print("Please pick one letter from the alphabet. ")
  elif len(playerLetter) > 1:
    print()
    print("Please pick only one letter from the alphabet. ")
  elif playerLetter in secretWord:
    print()
    print("That letter is in the word! ")
  elif playerLetter not in secretWord:
    print()
    print("That letter is not in the word. ")