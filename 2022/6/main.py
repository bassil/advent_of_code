def parse_input(filename):
	with open(filename) as fp:
		data = fp.read()
	return data


def detect_marker(data, len_marker=4):
	for i in range(len_marker, len(data)):
		chars = {ch for ch in data[i - len_marker: i]}
		if len(chars) == len_marker:
			return i
	return False


def part_1(data):
	return detect_marker(data, 4)


def part_2(data):
	return detect_marker(data, 14)


if __name__ == '__main__':
	data = parse_input("input.txt")
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))