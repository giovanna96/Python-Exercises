#Practice Python
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates)

import random

a=[random.randint(0,20) for r in range(random.randint(1,20))]
b=[random.randint(0,20) for r in range(random.randint(1,20))]
intersection = []

print(a)
print("\n")
print(b)

for x in range(len(a)):
	if a[x] in b and a[x] not in intersection:
		intersection.append(a[x])
	
print(intersection) 
