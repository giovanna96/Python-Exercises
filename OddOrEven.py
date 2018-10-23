# Practice Python 
#-Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
#-if the number is a multiple of 4, print out a different message.
def odd_or_even():
	if number%2 == 0:
		return print("this is an even number")
	else:
		return print("this is an odd number")

def multiple_of_four():
	if number%4 == 0:
		return True
	else:
		return False


number = int(input("enter a number: "))
if multiple_of_four():
	print(str(number) + " is a multiple of 4")

else:
	odd_or_even()






