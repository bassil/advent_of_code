def is_sum_of_two(preamble, n):
	n = int(n)
	preamble_set = set()

	for number in preamble:
		preamble_set.add(int(number))

	for number in preamble_set:

		if n > number:
			if (n - number) in preamble_set and number != (n - number):
				return True
		else:
			if (number - n) in preamble_set and number != (number - n):
				return True
	
	return False


def part_1(XMAS_data):
	for i, n in enumerate(XMAS_data[25:]):
		preamble = XMAS_data[i:i + 25]
		if not is_sum_of_two(preamble, n):
			return n


if __name__ == '__main__':

	with open("input.txt") as f:
		XMAS_data = f.read().split('\n')

	# Part 1 - find first number in XMAS data, after the preamble,
	# 		   that is not the sum of two numbers in the previous 25

	print(part_1(XMAS_data))
	