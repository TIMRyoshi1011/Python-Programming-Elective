while True:

	a = input("Would you like to continue?")
	if a == "yes":
		b = str(input("Continuing....\nComplete!"))
		print(b)
		break 
	elif a == "y":
		b = str(input("Continuing....\nComplete!"))
		print(b)
		break 
	elif a == "no":
		b = input("Exiting")
		break
	elif a == "n":
		b = input("Exiting")
		break
	else:
		print("Please try again and respond with yes or no")