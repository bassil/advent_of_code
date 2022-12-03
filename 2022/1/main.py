"""Day 1:  Calorie Counting"""

def parse_input(filename):

	with open(filename) as fp:
		data = [int(_)  if _ != "" else _ for _ in fp.read().split("\n")]

	parsed_input = []
	single_reindeer = []
	while len(data) > 0:
		entry = data.pop(0)
		if entry == "":
			parsed_input.append(single_reindeer)
			single_reindeer = []
		else:
			single_reindeer.append(entry)
	return parsed_input


def part_1(parsed_input):
	max_calories = 0
	for reindeer in parsed_input:
		calories = sum(reindeer)
		if calories > max_calories:
			max_calories = calories
	return max_calories


def part_2(parsed_input):
	sums = [sum(_) for _ in parsed_input]
	return sum(sorted(sums)[-3:])


if __name__ == '__main__':
	filename = "input.txt"
	parsed_input = parse_input(filename)
	print("part 1:", part_1(parsed_input))
	print("part 2:", part_2(parsed_input))