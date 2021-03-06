import copy

# part 1 helpers
def get_adjacent_seats(seat_states, i, j):
	adjacent_seats = []
	if  i > 0:
		adjacent_seats.append(seat_states[i-1][j])
		if j > 0:
			adjacent_seats.append(seat_states[i-1][j-1])
		if j + 1 < len(seat_states[i]):
			adjacent_seats.append(seat_states[i-1][j+1])

	if i + 1 < len(seat_states):
		adjacent_seats.append(seat_states[i+1][j])
		if j > 0:
			adjacent_seats.append(seat_states[i+1][j-1])
		if j + 1 < len(seat_states[i]):
			adjacent_seats.append(seat_states[i+1][j+1])

	if j > 0:
		adjacent_seats.append(seat_states[i][j-1])

	if j + 1 < len(seat_states[i]):
		adjacent_seats.append(seat_states[i][j+1])

	return adjacent_seats

def has_no_occupied_seats(seat_states, i, j):
	"""returns bool indicating whether 8 adjacent seats are empty"""
	adjacent_seats = get_adjacent_seats(seat_states, i, j)
	adjacent_seat_count = len(adjacent_seats)
	empty_adjacent_seat_count = 0

	for adjacent_seat in adjacent_seats:
		if adjacent_seat != "#":
			empty_adjacent_seat_count += 1

	return empty_adjacent_seat_count == adjacent_seat_count

def has_four_or_more_occupied(seat_states, i, j):
	"""returns bool indicating whether >= 4 adjacent seats are occupied"""
	adjacent_seats = get_adjacent_seats(seat_states, i, j)
	occupied_adjacent_seat_count = 0

	for adjacent_seat in adjacent_seats:
		if adjacent_seat == '#':
			occupied_adjacent_seat_count += 1

	return occupied_adjacent_seat_count >= 4

def get_next_seat_state(seat_states):
	# seat_states: 'L' - empty seat; '#' - occupied seat; '.' - floor

	# O(m*n) ~ is there a better way?
	next_seat_states = copy.deepcopy(seat_states)
	for i, row_state in enumerate(seat_states): # y-axis
		for j, seat_state in enumerate(row_state): # x-axis
			if seat_states[i][j] == '.':
				continue

			no_occupied_seats = has_no_occupied_seats(seat_states, i, j)
			four_or_more_occupied = has_four_or_more_occupied(seat_states, i, j)

			if seat_states[i][j] == 'L' and no_occupied_seats:
				next_seat_states[i][j] = '#'
			elif seat_states[i][j] == '#' and four_or_more_occupied:
				next_seat_states[i][j] = 'L'

	return next_seat_states

def part_1(seat_states):
	# rule - if a seat is empty (L) and no adjacent seats are occupied,
	# 		 in the next iteration it is occupied (#)
	#	   - if a seat is occupied (#) and >= 4 adjacent seats are occupied,
	#		 in the next iteration it is empty
	#	   - otherwise, the seat state doesn't change.
	current_seat_states = seat_states
	next_seat_states = get_next_seat_state(seat_states)
	occupied_seat_count = 0

	while next_seat_states != current_seat_states:
		
		current_seat_states = next_seat_states
		next_seat_states = get_next_seat_state(current_seat_states)

	return sum([_.count('#') for _ in next_seat_states])

# part 2 helpers
def get_first_seats(seat_states, i, j):
	first_seats = []
	# 8 directions - N S E W NE NW SE SW
	# N - i - 1, i - 2, ..., 0
	for _i in range(i-1, -1, -1):
		if seat_states[_i][j] != ".":
			first_seats.append(seat_states[_i][j])
			break
	# S - i + 1, i + 2, ..., len(seat_states)
	for _i in range(i+1, len(seat_states)):
		if seat_states[_i][j] != ".":
			first_seats.append(seat_states[_i][j])
			break
	# E - j + 1, j + 2, ..., len(seat_states[i])
	for _j in range(j+1, len(seat_states[i])):
		if seat_states[i][_j] != ".":
			first_seats.append(seat_states[i][_j])
			break
	# W - j - 1, j - 2, ..., 0
	for _j in range(j-1, -1, -1):
		if seat_states[i][_j] != ".":
			first_seats.append(seat_states[i][_j])
			break
	# NE (i - 1, j + 1), (i - 2, j + 2), ..., (i - k, j + k)
	for k in range(1, min(len(seat_states), len(seat_states[i]))):
		if i-k < 0 or j+k+1 > len(seat_states[i]):
			break
		if seat_states[i-k][j+k] != ".":
			first_seats.append(seat_states[i-k][j+k])
			break
	# NW (i - 1, j - 1), (i - 2, j - 2), ..., (i - k, j - k)
	for k in range(1, min(len(seat_states), len(seat_states[i]))):
		if i-k < 0 or j-k < 0:
			break
		if seat_states[i-k][j-k] != ".":
			first_seats.append(seat_states[i-k][j-k])
			break
	# SE (i + 1, j + 1), (i + 2, j + 2), ..., (i + k, j + k)
	for k in range(1, min(len(seat_states), len(seat_states[i]))):
		if i+k+1 > len(seat_states) or j+k+1 > len(seat_states[i]):
			break
		if seat_states[i+k][j+k] != ".":
			first_seats.append(seat_states[i+k][j+k])
			break
	# SW (i + 1, j - 1), (i + 2, j - 2), ..., (i + k, j - k)
	for k in range(1, min(len(seat_states), len(seat_states[i]))):
		if i+k+1 > len(seat_states) or j-k < 0:
			break
		if seat_states[i+k][j-k] != ".":
			first_seats.append(seat_states[i+k][j-k])
			break
	return first_seats

def has_no_occupied_seats_2(seat_states, i, j):
	"""returns bool indicating whether 8 adjacent seats are empty"""
	first_seats = get_first_seats(seat_states, i, j)
	first_seat_count = len(first_seats)
	empty_first_seat_count = 0

	for first_seat in first_seats:
		if first_seat != "#":
			empty_first_seat_count += 1

	return empty_first_seat_count == first_seat_count

def has_five_or_more_occupied(seat_states, i, j):
	first_seats = get_first_seats(seat_states, i, j)
	occupied_first_seat_count = 0

	for first_seat in first_seats:
		if first_seat == '#':
			occupied_first_seat_count += 1

	return occupied_first_seat_count >= 5

def get_next_seat_state_2(seat_states):
	# seat_states: 'L' - empty seat; '#' - occupied seat; '.' - floor

	# O(m*n) ~ is there a better way?
	next_seat_states = copy.deepcopy(seat_states)
	for i, row_state in enumerate(seat_states): # y-axis
		for j, seat_state in enumerate(row_state): # x-axis
			if seat_states[i][j] == '.':
				continue

			no_occupied_seats = has_no_occupied_seats_2(seat_states, i, j)
			five_or_more_occupied = has_five_or_more_occupied(seat_states, i, j)

			if seat_states[i][j] == 'L' and no_occupied_seats:
				next_seat_states[i][j] = '#'
			elif seat_states[i][j] == '#' and five_or_more_occupied:
				next_seat_states[i][j] = 'L'

	return next_seat_states

def part_2(seat_states):
	current_seat_states = seat_states
	next_seat_states = get_next_seat_state_2(seat_states)
	occupied_seat_count = 0

	while next_seat_states != current_seat_states:
		
		current_seat_states = next_seat_states
		next_seat_states = get_next_seat_state_2(current_seat_states)
	return sum([_.count('#') for _ in next_seat_states])

def main():

	with open("input.txt") as f:
		seat_states = f.read().split("\n")

	for i, line in enumerate(seat_states):
		seat_states[i] = list(line)
	
	print("Part 1:", part_1(seat_states))
	print("Part 2:", part_2(seat_states))
	


if __name__ == '__main__':
	main()