#Practice Python
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

divisor = []
value = int(input("enter a number: \n"))
for i in range(value):
	if value%(i+1)==0:
		divisor.append(i+1)
print(divisor)


