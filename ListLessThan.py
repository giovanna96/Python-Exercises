#Practice Python
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
#Make a new list that has all the elements less than the number given by the user from this list in it and print out this new list.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
value = int(input("enter a number: \n"))
less_than = []
for i in range(len(numbers)):
	if numbers[i]<value:
		less_than.append(numbers[i])

print(less_than)