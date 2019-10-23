# Henry Liu
# Period 4
# variable declaration and assignment
# examples
myNum = 12 # integer type
myString = "12" # string type
myNum + 3 # ok
print(myString + "3") # not ok


# make a variable and assign it the value of your favorite movie
# print "my favorite movie is " followed by the variable
favMovie = "Benchwarmers"
print("My favorite movie is " + favMovie + " .")


# while loops
# example - print from 1 to 10
x = 1
while x <= 10:
	print(x)
	x = x + 1
print()
# count down from 100 using a while loop
x=100
while x >= 1:
	print(x)
	x = x - 1


# string concatenation
# means putting two strings together
# example
myName = "Henry"
print("Hello " + myName)


# input
# example
yourName = input("What is your name? ")
print("Hello " + yourName + " have a nice day. ")

number = input("Enter a number: ")
#number = number + 10                   # this won't work bc number is in a string another int
number = int(number) +10
print("The number is " + str(number))



# ask for two numbers, add them and print the sum
yourNum = input("Give me a number ")
yourNum2 = input("Give me another number ")
sumofnumbers = int(yourNum) + int(yourNum2)
print("The sum of the two numbers is " + str(sumofnumbers) + ".")

# if / else statements
# example
num = int(input("Enter a number: "))
if num > 100: 
	print("Your number is more than 100")
elif num == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than or equal to 100")


# ask if today is your birthday
# if yes print Happy Birthday
birthday = input("Is today your birthday? ")
if birthday == "yes":
	print("Happy Birthday!!!")
else:
	print ("Have a nice day!")