def parse_input(filename):
	_input = []
	with open(filename) as f:
		for line in f:
			_input.append(line.strip("\n"))
	all_digits = []
	for s in _input:
		digits = []
		for ch in s:
			if ch.isnumeric():
				digits.append(ch)
		all_digits.append(digits)
	return all_digits


def main(parsed_input):
	# part 1:
	calibration_values = []
	for calibration_document in parsed_input:
		calibration_values.append(int(calibration_document[0] + calibration_document[-1]))
	return sum(calibration_values)



if __name__ == '__main__':
	# filename = "sample1.txt"
	filename = "input.txt"
	parsed_input = parse_input(filename)
	calibration_values = main(parsed_input)
	print(calibration_values)
