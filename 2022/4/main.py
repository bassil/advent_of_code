"""Day 4: Camp Cleanup"""


def parse_input(filename):
	data = []
	with open(filename) as fp:
		_data = [_.split(",") for _ in fp.read().split("\n")]
	for assignment_pair in _data:
		parsed_assignment_pair = [ _.split("-") for _ in assignment_pair]
		assignment_pair_set = [
			set(range(int(_1), int(_2) + 1)) for _1, _2 in parsed_assignment_pair
		]
		data.append(assignment_pair_set)
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