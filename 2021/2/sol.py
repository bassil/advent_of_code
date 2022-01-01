def get_data(file_name):
	with open(file_name, "r") as f:
		unparsed_data = f.read().split("\n")
		data = []
		for unparsed_pair in unparsed_data:
			parsed_pair = unparsed_pair.split(" ")
			parsed_pair[1] = int(parsed_pair[1])
			data.append(parsed_pair)
	return data


def move_part_1(h, d, command):
	direction, units = command
	if direction == "forward":
		h += units
	elif direction == "up":
		d -= units
	elif direction == "down":
		d += units
	return h, d


def part_1(data):
	# horizontal, depth
	h, d = 0, 0
	for command in data:
		h, d = move_part_1(h, d, command)
	return h * d


def move_part_2(h, d, a, command):
	direction, units = command
	if direction == "forward":
		h += units
		d += a * units
	else:
		if direction == "up":
			a -= units
		elif direction == "down":
			a += units
	return h, d, a


def part_2(data):
	# horizontal, depth, aim
	h, d, a = (0, 0, 0)
	for command in data:
		h, d, a = move_part_2(h, d, a, command)
	return h * d


if __name__ == "__main__":
	test = False

	file_name = "sample.txt" if test else "input.txt"
	data = get_data(file_name)
	
	print("Part 1:", part_1(data))
	print("Part 2:", part_2(data))