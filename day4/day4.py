# https://adventofcode.com/2021/day/4
numbers = [int(n) for n in input().split(",")]
input() # get rid of the extra line break
boards = []
board = []

while True:
	try:
		line = input()
	except EOFError:
		break
	if (line == ""):
		boards.append(board)
		board = []
	else:
		nums = [int(n) for n in line.split()]
		board.append(nums)


### PART 1
# calculate steps to win for each board, if no win -1
import copy
def board_solved(board, sign=-1):
	# check all rows
	for r in board:
		if (r == len(r)*[sign]):
			return True
	# check all columns
	for c in range(len(board[0])):
		checkeds = 0
		for r in board:
			if r[c] == sign: checkeds += 1
		if checkeds == len(board):
			return True
	return False

# get score of board
def get_score(board):
	for n in numbers:
		# cancel num in board
		for i, r in enumerate(board):
			for j, c in enumerate(r):
				if c == n:
					board[i][j] = 0
		# check if already bingo
		if (board_solved(board, 0)):
			# sum all in board
			s = sum([ sum(r) for r in board ])
			# multiply by current n
			score = s*n
			return score
			break

steps_to_win = []
for board in copy.deepcopy(boards):
	# example board
	# [[50, 98, 65, 14, 47], 
	#  [ 0, 22,  3, 83, 46], 
	#  [87, 93, 81, 84, 58], 
	#  [40, 35, 28, 74, 48], 
	#  [45, 99, 59, 37, 64]]
	steps = 0

	# loop through numbers
	for n in numbers:
		# cancel num in board
		for i, r in enumerate(board):
			for j, c in enumerate(r):
				if c == n:
					board[i][j] = -1
		steps += 1
		# check if already bingo
		if (board_solved(board)):
			steps_to_win.append(steps)
			break
# print("all steps: ", steps_to_win)

fastest_board_index = steps_to_win.index(min(steps_to_win))
winning_board = boards[fastest_board_index]
print("fastest board: ", winning_board)
# print("steps in board: ", steps_to_win[fastest_board_index])
print(get_score(winning_board))
		

### PART 2
slowest_board_index = steps_to_win.index(max(steps_to_win))
losing_board = boards[slowest_board_index]
print("slowest board: ", losing_board)
# print("steps in board: ", steps_to_win[slowest_board_index])
print(get_score(losing_board))