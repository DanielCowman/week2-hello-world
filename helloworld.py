
# Daniel Cowman 

# assign variable resp with an array of responses
resp = ["Bonjour","Hola","Ciao"]

# greets the user and explains the objective
def startup():
	print "Hello World"
	print "Choose a language and I'll greet you in that language"

# define the mainLoop to prevent clutter
def mainLoop():
	# executes the startup function
	startup()
	# asks the user for their response to the question
	user_input = input("1. French \n2. Spanish \n3. Italian\n")
	# begin the search for the correct response based on the user input (Variable: user_input)
	# use the length of the resp array to determine when to end the for loop
	for i in range(0, len(resp)):
		# checks if the user_input variable matches with the current loop count
		if int(user_input) == i+1:
			# if the user_input variable matches the current loop count
			# print the response (the +1 is to account for the array starting at 0)
			print resp[i]
			exit # exit the for program
		else:
			continue # if users_input = false continue the loop

mainLoop()

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

