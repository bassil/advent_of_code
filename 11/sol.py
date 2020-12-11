import copy

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

def part_2(seat_states):
	raise NotImplementedError

def main():

	with open("input.txt") as f:
		seat_states = f.read().split("\n")

	for i, line in enumerate(seat_states):
		seat_states[i] = list(line)


	# print(seat_states)
	# print(next_seat_states)
	# print(get_next_seat_state(seat_states) == next_seat_states)

	# print(seat_states[i][j])
	print("Part 1:", part_1(seat_states))

	


if __name__ == '__main__':
	main()