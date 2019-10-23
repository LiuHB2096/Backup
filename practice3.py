day = input("What is the day today? ")

if (day == "monday" or day == "Monday"): 
	print("It's Monday, the weekend is over.")

elif(day == "friday" or day == "Friday"):
	print("It's Friday, the weekend is close.") 

elif(day == "saturday" or day == "Saturday" or day == "sunday" or day == "Sunday"):
	print("It's the weekend, time to relax." )

else: 
	print("It's not the weekend yet.")