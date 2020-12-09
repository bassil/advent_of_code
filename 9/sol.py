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




if __name__ == '__main__':

	with open("input.txt") as f:
		XMAS_data = f.read().split('\n')

	preamble = XMAS_data[:25]

	# Part 1 - find first number in XMAS data, after the preamble,
	# 		   that is not the sum of two numbers in the previous 25
	print(XMAS_data[25])
	
	print(is_sum_of_two(preamble, XMAS_data[25]))