"""Day 4: Camp Cleanup"""


def parse_input(filename):
	"""
		Returns:
			data: list[list[set[int]]
				A list of lists (sublists),
				Each sublist consists of a pair of sets of integers.
	"""
	data = []
	with open(filename) as fp:
		_data = [ _.split(",") for _ in fp.read().split("\n") ]
	for assignment_pairs in _data:
		parsed_assignment_pairs = [ _.split("-") for _ in assignment_pairs ]
		assignment_set_pairs = [
			set(range(int(_1), int(_2) + 1)) for _1, _2 in parsed_assignment_pairs
		]
		data.append(assignment_set_pairs)
	return data


def part_1(data):
	count = 0
	for assignment_1, assignment_2 in data:
		if (
			assignment_1.union(assignment_2) == assignment_1 or 
			assignment_1.union(assignment_2) == assignment_2
		):
			count += 1
	return count


def part_2(data):
	count = 0
	for assignment_1, assignment_2 in data:
		if assignment_1.intersection(assignment_2):
			count += 1
	return count


if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))