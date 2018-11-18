#Practice Pyhton
#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random

def guessing(answer):
  while(answer!='exit'):
  	
    if int(answer) == random_number:
        return print("exactly right")
    if int(answer) < random_number and int(answer)>=1 and int(answer)<=9:
         print("too low")
    if int(answer) > random_number and int(answer)>=1 and int(answer)<=9:
         print("too high")
    if int(answer)<1 or int(answer)>9 :
      print("type a number from 1 to 9 or exit")
    answer = input("Guess the rigth number ")

random_number = random.randint(1,9)
answer = input("Guess the rigth number ")
guessing(answer)
