def get_data(file_name):
	with open(file_name, "r") as f:
		data = f.read().split("\n")
	data = [_.split(" -> ") for _ in data]
	parsed_data = []
	for entry in data:
		coords = []
		for pair in entry:
			parsed_pair = pair.split(",")
			coords.append([int(_) for _ in parsed_pair])
		parsed_data.append(coords)
	return parsed_data


def get_straight_lines(data):
	straight_lines = []
	for vent_line in data:
		[x1, y1], [x2, y2] = vent_line
		if x1 == x2 or y1 == y2:
			straight_lines.append(vent_line)
	return straight_lines


def get_vents_from_line(line):
	vents = []
	[_x1, _y1], [_x2, _y2] = line
	if _x1 > _x2:
		x1 = _x2
		x2 = _x1
	else:
		x1 = _x1
		x2 = _x2
	if _y1 > _y2:
		y1 = _y2
		y2 = _y1
	else:
		y1 = _y1
		y2 = _y2
	if x1 == x2:
		for y in range(y1, y2 + 1):
			vents.append((x1, y))
	else:
		for x in range(x1, x2 + 1):
			vents.append((x, y1))
	return vents


def part_1(data):
	ocean_floor = {}
	straight_lines = get_straight_lines(data)
	for straight_line in straight_lines:
		vents = get_vents_from_line(straight_line)
		for vent in vents:
			if vent in ocean_floor:
				ocean_floor[vent] += 1
			else:
				ocean_floor[vent] = 1
	count = 0
	for value in ocean_floor.values():
		if value >= 2:
			count += 1
	return count

if __name__ == '__main__':
	test = False
	file_name = "sample.txt" if test else "input.txt"
	data = get_data(file_name)
	print("Part 1:", part_1(data))
