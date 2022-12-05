"""Day 5: """


def parse_input(filename):
	with open(filename) as fp:
		data = fp.read().split("\n")
	return data


def part_1(data):
	pass


def part_2(data):
	pass


if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part_1:", part_1(data))
	print("part_2:", part_2(data))
