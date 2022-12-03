"""Day 3: """


def parse_input(filename):
	with open(filename) as fp:
		data = fp.read().split("\n")
	return data


def priorities():
	_priorities = {}
	for i in range(97, 123):
		_priorities[chr(i)] = i - 96
	for i in range (65, 91):
		_priorities[chr(i)] = i - 38
	return _priorities


def part_1(data):
	_priorities = priorities()
	ret = 0
	for items in data:
		mid = len(items) // 2
		first_compartment = set(items[:mid])
		second_compartment = set(items[mid:])
		error = first_compartment.intersection(second_compartment).pop()
		ret += _priorities[error]
	return ret


def part_2(data):
	_priorities = priorities()
	ret = 0
	for i in range(len(data) // 3):
		set_1 = set(data[i * 3])
		set_2 = set(data[i * 3 + 1])
		set_3 = set(data[i * 3 + 2])
		error = set_1.intersection(set_2).intersection(set_3).pop()
		ret += _priorities[error]
	return ret

if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))