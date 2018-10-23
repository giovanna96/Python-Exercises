# Practice Python
#-Create a program that asks the user to enter their name and their age. 
#-Print out a message addressed to them that tells them the year that they will turn 100 years old.


import datetime

def onehundred_birthday_year_calculator(age,name):
	now = datetime.datetime.now()
	year = str((100-age) + now.year)
	return print(name + " your 100th birthday will be in " + year)



print("What is your name and age?")	
name = input("Name: ")
age = int(input("Age: "))
onehundred_birthday_year_calculator(age,name)
