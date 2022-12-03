"""Day 2: Rock Paper Scissors"""


def parse_input(filename):
	with open(filename) as fp:
		data = [_.split(" ") for _ in fp.read().split("\n")]
	return data


def score(round_moves):
	"""
	A, X: 1 - rock
	B, Y: 2 - paper
	C, Z: 3 - scissors
	"""
	other_move, move = round_moves
	win = 6
	tie = 3
	loss = 0
	scores = {
		"X": 1,
		"Y": 2,
		"Z": 3
	}
	_score = scores[move]
	if other_move == "A":
		if move == "X":
			_score += tie
		elif move == "Y":
			_score += win
	elif other_move == "B":
		if move == "Y":
			_score += tie
		elif move == "Z":
			_score += win
	elif other_move == "C":
		if move == "X":
			_score += win
		elif move == "Z":
			_score += tie
	return _score


def part_1(data):
	return sum([score(round_moves) for round_moves in data])


def part_2(data):
	_score = 0
	for round_moves in data:
		other_move, outcome = round_moves
		if other_move == "A":
			if outcome == "X":
				move = "Z"	
			elif outcome == "Y":
				move = "X"
			elif outcome == "Z":
				move = "Y"
		elif other_move == "B":
			if outcome == "X":
				move = "X"	
			elif outcome == "Y":
				move = "Y"
			elif outcome == "Z":
				move = "Z"
		elif other_move == "C":
			if outcome == "X":
				move = "Y"	
			elif outcome == "Y":
				move = "Z"
			elif outcome == "Z":
				move = "X"

		_score += score([other_move, move])
	return _score


if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))
