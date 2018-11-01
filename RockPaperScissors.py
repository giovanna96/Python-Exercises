#Practice Python
#Make a two-player Rock-Paper-Scissors game. Compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.
def game(move1,move2):
	while (move1 != '1' and move1 != '2' and move1 != '3' and move2 != '1' and move2 != '2' and move2 != '3') :
		move1 = input("Player1: 1-Rock 2-Paper 3-Scissors ")
		move2 = input("Player2: 1-Rock 2-Paper 3-Scissors ")	
	if move1 == move2:
		print("It's a tie!")
	elif (move1=='1'and move2=='3'):
		print("Player 1 Win ")
	elif (move1 =='1' and move2=='2'):
		print("Player 2 Win ")
	elif (move1==	'2' and move2=='3') :
		print("Player 2 Win ")
	elif (move1=='2' and move2=='1') :
		print("Player 1 Win ")
	elif (move1=='3' and move2=='1'):
		print("Player 2 Win ")
	elif (move1=='3' and move2=='2') :
		print("Player 1 Win ")


		

player1 = True
player2 = True

while (player1==True and player2==True):
	
	move1 = input("Player1: 1-Rock 2-Paper 3-Scissors ")
	move2 = input("Player2: 1-Rock 2-Paper 3-Scissors ")
	game(move1,move2)

	play_again = input("Play again? 1-yes 2-no ")
	
	if(play_again=='1'):
		player1=True
		player2=True
		
	else:
		print("Game Over")
		player1=False
		player2=False
		
	
		
		
		
		