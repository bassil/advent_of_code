digit_map = {
	"one": "one1one",
	"two": "two2two",
	"three": "three3three",
	"four": "four4four",
	"five": "five5five",
	"six": "six6six",
	"seven": "seven7seven",
	"eight": "eight8eight",
	"nine": "nine9nine"
}


def translate(line):
	for digit in digit_map:
		if digit in line:
			line = line.replace(digit, digit_map[digit])
	return line


def parse_input(filename):
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip())
	translated_lines = []
	for line in lines:
		translated_line = translate(line)
		digits = []
		for ch in translated_line:
			if ch.isnumeric():
				digits.append(ch)
		translated_lines.append(digits)
	return translated_lines


def main(parsed_input):
	calibration_values = []
	for calibration_document in parsed_input:
		calibration_values.append(int(calibration_document[0] + calibration_document[-1]))
	return sum(calibration_values)


if __name__ == '__main__':
	# filename = "sample2.txt"
	filename = "input.txt"
	parsed_input = parse_input(filename)
	calibration_values = main(parsed_input)
	print(calibration_values)
