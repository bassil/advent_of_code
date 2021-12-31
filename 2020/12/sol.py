def manhattan_distance(x, y):
	return abs(x) + abs(y)

def part_1(instructions):
	coords = [0, 0]
	bearing = 0
	for instruction in instructions:
		if instruction[0] == 'N':
			coords[1] += instruction[1]
		elif instruction[0] == 'S':
			coords[1] -= instruction[1]
		elif instruction[0] == 'E':
			coords[0] += instruction[1]
		elif instruction[0] == 'W':
			coords[0] -= instruction[1]
		elif instruction[0] == 'L':
			bearing = (bearing - instruction[1]) % 360
		elif instruction[0] == 'R':
			bearing = (bearing + instruction[1]) % 360
		elif instruction[0] == 'F':
			if bearing == 0:
				# E
				coords[0] += instruction[1]
			elif bearing == 90:
				# S
				coords[1] -= instruction[1]
			elif bearing == 180:
				# W
				coords[0] -= instruction[1]
			elif bearing == 270:
				# N
				coords[1] += instruction[1]

	return manhattan_distance(coords[0], coords[1])

def part_2(instructions):
	coords = [0, 0]
	waypoint = [10, 1]

	for instruction in instructions:
		if instruction[0] == 'N':
			waypoint[1] += instruction[1]
		elif instruction[0] == 'S':
			waypoint[1] -= instruction[1]
		elif instruction[0] == 'E':
			waypoint[0] += instruction[1]
		elif instruction[0] == 'W':
			waypoint[0] -= instruction[1]
		elif instruction[0] == 'L':
			if instruction[1] == 90:
				waypoint = [-waypoint[1], waypoint[0]]
			elif instruction[1] == 180:
				waypoint = [-waypoint[0], -waypoint[1]]
			elif instruction[1] == 270:
				waypoint = [waypoint[1], -waypoint[0]]
		elif instruction[0] == 'R':
			if instruction[1] == 90:
				waypoint = [waypoint[1], -waypoint[0]]
			elif instruction[1] == 180:
				waypoint = [-waypoint[0], -waypoint[1]]
			elif instruction[1] == 270:
				waypoint = [-waypoint[1], waypoint[0]]
		elif instruction[0] == 'F':
			coords[0] += instruction[1]*waypoint[0]
			coords[1] += instruction[1]*waypoint[1]

	return manhattan_distance(coords[0], coords[1])

def main():
	with open("input.txt") as f:
		instructions = [(_[0], int(_[1:])) for _ in f.read().split("\n")]
	
	# print("Part 1:", part_1(instructions))
	print("Part 2:", part_2(instructions))


if __name__ == '__main__':
	main()