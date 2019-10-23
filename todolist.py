# Henry Liu
# Period 4

print("Welcome to the To Do List ")
todoList = []

while True:
	print()
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")

	choice = input("Make your choice: ")
	if choice == "q":
		break

	elif choice == "a":
		todo = input("What would you like to add to your To Do List? ")
		todoList.append(todo)

	elif choice == "r":
		takeout = input("What would you like to remove from your To Do List? ")
		todoList.remove(takeout)

	elif choice == "p":
		print("Here is your To Do List: " + str(todoList))

	else:
		print("Please enter one of the letters listed above ")







