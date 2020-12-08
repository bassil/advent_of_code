def declarations(input_file):

	with open(input_file) as f:
		declarations = f.read().split("\n\n")
	
	return declarations

def group_declaration_count_1(group_declarations):
	
	group_declarations = group_declarations.split("\n")
	
	passenger_declarations_set = set()

	for passenger_declarations in group_declarations:
		for passenger_declaration in passenger_declarations:
			passenger_declarations_set.add(passenger_declaration)
	
	return len(passenger_declarations_set)


def part_1(declarations):

	return sum([group_declaration_count_1(group_declarations) \
		for group_declarations in declarations])


def group_declaration_count_2(group_declarations):
	
	group_declarations = [set(passenger_declarations) \
		for passenger_declarations in group_declarations.split("\n")]
	
	return len(set.intersection(*group_declarations))


def part_2(declarations):

	return sum([group_declaration_count_2(group_declarations) \
		for group_declarations in declarations])


if __name__ == '__main__':

	# declarations = declarations("sample_input.txt")
	declarations = declarations("input.txt")
	print("Part 1:", part_1(declarations))
	print("Part 2:", part_2(declarations))