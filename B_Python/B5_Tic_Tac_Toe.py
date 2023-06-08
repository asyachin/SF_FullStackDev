import pandas as pd

def gamer_auth():
#Gamers initialization
	gamer_x = str(input("Input in the name of a first gamer: "))
	print(f'Hello {gamer_x}, your inputs are signed as X')
	gamer_o = str(input("Input the name of a first gamer: "))
	print(f'Hello {gamer_o}, your inputs are signed as O')

	return gamer_x, gamer_o

def check_input(new_input, board):
	new_input_y = None
	new_input_x = None
 
	valid_inputs = ['a0','a1','a2',
								'b0','b1','b2',
								'c0','c1','c2']
 
	if new_input in valid_inputs:
		new_input_y = new_input[0].upper() #column
		new_input_x = int(new_input[1]) #index
  
		if board[new_input_y][new_input_x] == '.': #check neither has been put the value
			return new_input_y, new_input_x
		else:
			print(f'{new_input} is already exist, please make new input!')
			return False
	else:
		print(f'sorry, the value {str(new_input).upper()} is out of range')
		return False 




def get_winner(board):
	winner = '.'
	for i in range(3):
		if board.iloc[i][0] == board.iloc[i][1] == board.iloc[i][2] and board.iloc[i][1] != '.':
			winner = board.iloc[i][0]
		elif board.iloc[0][i] == board.iloc[1][i] == board.iloc[2][i] and board.iloc[2][i] != '.':
			winner = board.iloc[2][i]
		elif board.iloc[0][0] == board.iloc[1][1] == board.iloc[2][2] and board.iloc[1][1] != '.':
			winner = board.iloc[1][1]
		elif board.iloc[2][0] == board.iloc[1][1] == board.iloc[0][2] and board.iloc[1][1] != '.':
			winner = board.iloc[1][1]
		else:
			continue
	return winner	

def take_input(new_input, gamer, gamer_x, board):
	if check_input(new_input, board) is not False:
		new_input_y, new_input_x = check_input(new_input, board)

		if gamer == gamer_x:
			board[new_input_y][new_input_x] = 'X'
		else:
			board[new_input_y][new_input_x] = 'O'
		return board
	else:
		return take_input(str(input("Make your choice with Column + Row (for example' A0') ")).lower(), gamer, gamer_x, board)

winner = '.'
game_counter = 3


board = {	'A': (["."]*3),
					'B': (["."]*3),
					'C': (["."]*3)}
board = pd.DataFrame(board)

print("-" * 35, " Tic-tac-toe game for two players ", "-" * 35)
gamer_x, gamer_o = gamer_auth()

while winner != 'X':
	print(board)
	if game_counter % 2 == 1:
		print(f'{gamer_x},make your input!')
		gamer = gamer_x
	else:
		print(f'{gamer_o},make your input!')
		gamer = gamer_o

	take_input(str(input("Make your choice with Column + Row (for example' A0') ")).lower(), gamer, gamer_x, board)
	winner = get_winner(board)
	game_counter += 1
	
print(board)
if winner == 'X':
	print(f'{gamer_x}, congratulations, you won!')
else:
	print(f'{gamer_o}, congratulations, you won!')