def get_data(file_name):
	with open(file_name, "r") as f:
		data = f.read().split("\n\n")
	numbers = data[0].split(",")
	pre_parsed_boards = data[1:]
	boards = []
	for pre_parsed_board in pre_parsed_boards:
		board = pre_parsed_board.split("\n")
		parsed_board = []
		for pre_parsed_row in board:
			parsed_row = pre_parsed_row.split()
			parsed_board.append(parsed_row)
		boards.append(parsed_board)
	return numbers, boards


def update_board(board, number):
	for i, row in enumerate(board):
		for j, value in enumerate(row):
			if value == number:
				board[i][j] = 0
				break
	return board


def find_number_in_boards(playing_boards, number):
	updated_playing_boards = []
	for playing_board in playing_boards:
		updated_playing_boards.append(update_board(playing_board, number))
	return updated_playing_boards


def is_bingo(board):
	for row in board:
		num_marked = 0
		for num in row:
			if num == 0:
				num_marked += 1
		if num_marked == 5:
			return True

	for col_num in range(len(board[0])):
		num_marked = 0
		for row_num in range(len(board)):
			if board[row_num][col_num] == 0:
				num_marked += 1
		if num_marked == 5:
			return True

	return False


def score(board):
	return sum([int(_) for row in board for _ in row])


def part_1(numbers, boards):
	playing_boards = boards.copy()
	for number in numbers:
		playing_boards = find_number_in_boards(playing_boards, number)
		for playing_board in playing_boards:
			if is_bingo(playing_board):
				return score(playing_board) * int(number)

if __name__ == '__main__':
	test = False
	file_name = "sample.txt" if test else "input.txt"
	numbers, boards = get_data(file_name)

	print("Part 1:", part_1(numbers, boards))
