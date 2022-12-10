"""Day 5: Supply Stacks"""


def parse_input(filename):
	with open(filename) as fp:
		data = fp.read().split("\n\n")
	return [_.split("\n") for _ in data]


def parse_crates(data, num_cols=9):
	crates = {_: [] for _ in data[-1].split()}
	for row in data[:-1]:
		for i in range(num_cols):
			col_key = str(i + 1)
			crate = row[i * 4 : (i + 1) * 4].split("[")[-1].split("]")[0]
			if crate != "    " and crate != "   ":
				crates[col_key].insert(0, crate)
	return crates


def parse_moves(data):
	moves = []
	for instruction in data:
		moves.append([int(s) for s in instruction.split() if s.isdigit()])
	return moves


def move_crates_1(crates, num, src, dest):
	while num > 0:
		crate = crates[src].pop()
		crates[dest].append(crate)
		num -= 1
	return crates


def move_crates_2(crates, num, src, dest):
	_crates = []
	while num > 0:
		crate = crates[src].pop()
		_crates.append(crate)
		num -= 1
	_crates.reverse()
	crates[dest].extend(_crates)
	return crates
	

def execute(data, move_fn):
	crates = parse_crates(data[0])
	moves = parse_moves(data[1])

	for num, src, dest in moves:
		src = str(src)
		dest = str(dest)
		crates = move_fn(crates, num, src, dest)
	top = ""
	for i in range(1, 10):
		top += crates[str(i)].pop()
	return top


def part_1(data):
	return execute(data, move_crates_1)


def part_2(data):
	return execute(data, move_crates_2)


if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part_1:", part_1(data))
	print("part_2:", part_2(data))
