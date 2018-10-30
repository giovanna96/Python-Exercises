#Practice Python
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def palindrome_reverse(word):
	reverse = word[::-1]
	if(reverse==word):
		return True

def palindrome_loop(word):
	word_range = len(word)
	count = 0
	for i in range(len(word)):
		if (word[(word_range-1)] == word[i]):
			count+=1
			word_range-=1
	if(count == len(word)):
		return True

word = input("enter a word:")
if(palindrome_reverse(word) == True): #or if(palindrome_loop==True)
	print(word + " is a palindrome")
else:
	print(word + " is NOT a palindrome" )

