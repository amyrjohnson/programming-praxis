#first made basic funtionality--printing a board on screen that can be updated
# prompts users for names, asks players for input and prints and updates board
#then added ability to tell when a player wins
#then added coin flip, ability to play again
#finally, added dumb computer player, can be improved upon

#areas to improve: computer player (keep state of game?), refactoring, make startup cleaner--maybe tournament option, levels, 
#more robust to user input, better interface, tic tac toe-ception

import sys
import random


def print_board(a,b,c,d,e,f,g,h,i):
	# prints the tic tac toe board to the screen
	print "%s | %s | %s" % (a,b,c)
	print "----------"
	print "%s | %s | %s" % (d,e,f)
	print "----------"
	print "%s | %s | %s" % (g,h,i)
	
def startup():
	# this doesn't really have to be packaged as a function I guess, but it was looking kind of messy	 
	global player1 
	global player2
	global computer
	global d
	#packaging stuff into functions and moving it around caused some issues with variables 
	# and declaring them global seemed to fix it but I'm not sure it's all necessary
	print "Let's play tic tac toe"
	print "Type 'computer' to play against the computer and 'friend' to play against a friend"
	#choose between playing with a friend and against the computer
	gametype = raw_input("> ")
	if gametype.lower() == 'friend':
	# get player names
		computer = False
		print "Great, you're playing with a friend"
		print "Who is player 1?"
		p1 = raw_input("> ")
		print "Who is player 2?"
		p2 = raw_input("> ")
	if gametype.lower() == 'computer':
		#set a variable to True to be used later when differences between friend/machine arise
		computer = True
		print "Great, you're playing against me"
		print "What's your name?"
		p1 = raw_input("> ")
		p2 = 'machine'
	else:
		print "I don't understand"
		startup()
	# decide who goes first via virtual coin flip
	print "Let's flip a coin to see who goes first"
	# player 1 always gets to call it, could change this
	print "%s calls it--heads or tails?" % (p1)
	flip = raw_input("> ")
	while flip.lower() != 'heads' and flip.lower() != 'tails':
		print "Huh? try that again--'heads' or 'tails'?"
		flip = raw_input("> ")
	result = random.choice(['heads','tails'])
	#assign who goes first and second based on the results of the toss
	if flip.lower() == result:
		player1 = p1
		player2 = p2
	else:
		player1 = p2
		player2 = p1
	print "It was %s!" % result
	# the choice of machine/friend makes the syntax awkward but doesn't seem worth 
	#a whole different set of dialogue
	print "That means %s goes first and is X. %s goes second and is O. Let's play!" % (player1, player2)
	if computer == True:
		if player1 == 'machine':
			marker = 'X'
		if player2 == 'machine':
			marker = 'O'		
	print "Choose the number of the square where you'd like to place your marker." 
	 #create a dictionary entry placeholder for each gameboard space, could also use 
	 #letters to identify spaces but numbers seem more intuitive
	 #could also probably have created a list and used the index to look up elements 
	 #later on when updating the board
	d = dict(zip(['a','b','c','d','e','f','g','h','i'],range(1,10))) 
	print_board(d['a'],d['b'],d['c'],d['d'],d['e'],d['f'],d['g'],d['h'],d['i']) 
	# do I want to have the board always show the numbers? it's potentially distracting

#computer plays randomly for now, could be made smarter	
def computer_choice(d):
	#generate list of valid moves and choose one
	valid_moves = []
	for k in d:
		if d[k] != "X" and d[k] != "O":
			valid_moves.append(k)
	play = random.choice(valid_moves)
	return d[play]
	
def move(player, marker, turn):
	#gets move choice from player/computer, checks validity, and updates board
	global choice
	if player != 'machine':
		print "Your move, %s" % (player)
		#player selects move
		try:
			choice = int(raw_input("> "))
		except:
			print "Invalid choice, next time type a number"
			quit()
	elif player == 'machine':
		print "My turn!"
		choice = computer_choice(d)
	if choice in d.values():
		for k in d.keys():  # doing a reverse lookup here--maybe a dict wasn't the best choice?
			if d[k] == choice:
				d[k] = marker #update the gameboard
		print_board(d['a'],d['b'],d['c'],d['d'],d['e'],d['f'],d['g'],d['h'],d['i'])
	else:
		print "Invalid number, try again"
		move(player, marker, turn)
		
def is_win(d):     
#checks for all possible tic tac toes
#it would probably be more efficient to keep track of the 'win' state as the game 
#progresses rather than checking every time but for now this is simpler
	#check across
	if d['a'] == d['b'] and d['a'] == d['c']:
		return True
	if d['d'] == d['e'] and d['d'] == d['f']:
		return True
	if d['g'] == d['h'] and d['g'] == d['i']:
		return True
	#check diagonal
	if d['a'] == d['e'] and d['a']==d['i']:
		return True
	if d['c'] == d['e'] and d['c'] == d['g']:
		return True
	#check vertical
	if d['a'] == d['d'] and d['a'] == d['g']:
		return True
	if d['b'] == d['e'] and d['b'] == d['h']:
		return True
	if d['c'] == d['f'] and d['c'] == d['i']:
		return True
	return False
	
def startover():
	# give the player the option to play again
	print "Would you like to play again? Y/N?"
	x = raw_input("> ")
	if x.lower() == 'y':
		tic_tac_toe()
	if x.lower() == 'n':
		quit()
	else:
		print "Please type 'Y' or 'N'"
		startover()
			
def tic_tac_toe():
	global turn
	startup()
 	turn = 1
 	while turn < 10: 
 		if turn %2 ==1:  #alternate players based on turn count
 			move(player1, 'X', turn)
 			#check if the player won
 			if turn >= 5:
 				win = is_win(d)
 				if win == True:
 					print "%s wins!!" % (player1)
 					startover()
 			turn += 1
 		elif turn %2 == 0 :
 			move(player2, 'O', turn)
 			if turn >= 5:
 				win = is_win(d)
 				if win == True:
 					print "%s wins!!" % (player2)
 					startover()
 			turn += 1
 	print "It's a tie!" 
 	startover()

tic_tac_toe()



# below is stuff for trying to create a smarter computer player, very unfinished


	#identify possible moves
	#check if opponent can win on next move
	#check if self could win on next move
	#block if necessary
	#otherwise choose randomly from strategic moves? 
# def next_win(marker):
# 	if d['a'] == d['b'] or d['a'] == d['c'] or d['b'] == d['c']:
# 		for item in ['a','b','c']:
# 			#check if valid move
# 			if item in valid_moves: # need to check if two items are X's or O's
# 				block_moves.append(item)
# 	if d['d'] == d['e'] or d['d'] == d['f'] or d['e'] = d['f']:
# 		for item in ['d','e','f']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	if d['g'] == d['h'] or d['g'] == d['i'] or d['h'] == d['i']:
# 		for item in ['g','h','i']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	#check diagonal
# 	if d['a'] == d['e'] or d['a']==d['i'] or d['e'] == d['i']:
# 		for item in ['a','e','i']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	if d['c'] == d['e'] or d['c'] == d['g'] or d['e'] == d['g']:
# 		for item in ['c','e','g']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	#check vertical
# 	if d['a'] == d['d'] or d['a'] == d['g'] or d['d'] == d['g']:
# 		for item in ['a','d','g']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	if d['b'] == d['e'] or d['b'] == d['h'] or d['e'] == d['h']:
# 		for item in ['a','d','g']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	if d['c'] == d['f'] or d['c'] == d['i'] or d['f'] == d['i']:
# 		for item in ['c','f','i']:
# 			if item in valid_moves:
# 				block_moves.append(item)
# 	return block_moves
	
	