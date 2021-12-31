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


def contiguous_sub_sequence(XMAS_data, invalid_number):
	
	invalid_number = int(invalid_number)
	for i, number in enumerate(XMAS_data):
		contiguous_sum = int(number)
		for j in range(i+1, len(XMAS_data)):
			if contiguous_sum == invalid_number:
				return XMAS_data[i:j]
			elif contiguous_sum > invalid_number:
				break
			contiguous_sum += int(XMAS_data[j])

def part_2(contiguous_sub_sequence):

	return int(min(contiguous_sub_sequence)) + int(max(contiguous_sub_sequence))


if __name__ == '__main__':

	with open("input.txt") as f:
		XMAS_data = f.read().split('\n')

	# Part 1 - find first number in XMAS data, after the preamble,
	# 		   that is not the sum of two numbers in the previous 25

	invalid_number = part_1(XMAS_data)
	print("Part 1:", invalid_number)
	
	# Part 2 - find contiguous set of at least two numbers in XMAS data
	# 		   that sum to invalid number from part 1

	contiguous_sub_sequence = contiguous_sub_sequence(XMAS_data, invalid_number)
	encryption_weakness = part_2(contiguous_sub_sequence)
	print("Part 2:", encryption_weakness)