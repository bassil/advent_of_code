"""Day 8: Treetop Tree House"""

def parse_input(filename):
	with open(filename) as fp:
		data = [list(line) for line in fp.read().split("\n")]
	return data

def part_1(data):
	num_rows = len(data)
	num_cols = len(data[0])
	count = 0
	for r in range(1, num_rows - 1):
		for c in range(1, num_cols - 1):
			tree = data[r][c]
			trees_left = []
			for _c in range(c):
				trees_left.append(data[r][_c])
			trees_right = []
			for _c in range(c + 1, num_cols):
				trees_right.append(data[r][_c])
			trees_above = []
			for _r in range(r):
				trees_above.append(data[_r][c])
			trees_below = []
			for _r in range(r + 1, num_rows):
				trees_below.append(data[_r][c])

			if (
				all([tree > neighbor for neighbor in trees_left]) or
				all([tree > neighbor for neighbor in trees_right]) or
				all([tree > neighbor for neighbor in trees_above]) or
				all([tree > neighbor for neighbor in trees_below]) 
			):
				count += 1
	return count + (2 * num_rows) + (2 * num_cols) - 4

def part_2(data):
	num_rows = len(data)
	num_cols = len(data[0])
	max_score = 0
	for r in range(1, num_rows - 1):
		for c in range(1, num_cols - 1):
			tree = data[r][c]

			left_score = 0
			right_score = 0
			above_score = 0
			below_score = 0

			for _c in range(c - 1, -1, -1):
				left_score += 1
				if data[r][_c] >= tree:
					break
			for _c in range(c + 1, num_cols):
				right_score += 1
				if data[r][_c] >= tree:
					break
			for _r in range(r - 1, -1, -1):
				above_score += 1
				if data[_r][c] >= tree:
					break
			for _r in range(r + 1, num_rows):
				below_score += 1
				if data[_r][c] >= tree:
					break
			score = left_score * right_score * above_score * below_score
			if score > max_score:
				max_score = score
	return max_score


if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))