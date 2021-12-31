def get_passports_from_input(input_name):
	"""returns list of passports parsed from input file input_name

	Args:

		input_name - str -  path to file name
	"""

	passports = []

	with open(input_name) as f:

		passport = []

		for line in f:

			if line == '\n':
				passports.append(passport)
				passport = []

			else:
				passport.append(line)

		# edge case of last passport not ending with newline
		if len(passport) != 0:
			passports.append(passport)

	return passports


def get_parameters_from_passports(passports):
	"""returns list of passport dictionaries

	Args:

		passports - list - list of strings, each string including passport parameters
	"""

	passport_dicts_list = []

	for passport in passports:
		passport_str = ""
		
		for elt in passport:
			passport_str += elt

		parsed_passport = passport_str.split()
		passport_dict = {}

		for parameter in parsed_passport:
			key, value = parameter.split(':')
			passport_dict[key] = value

		passport_dicts_list.append(passport_dict)

	return passport_dicts_list


def is_passport_valid(passport_dict):
	"""returns bool indicating whether a passport is valid or not"""

	if len(passport_dict) == 8:
	
		return True

	elif len(passport_dict) == 7 and 'cid' not in passport_dict.keys():
	
		return True

	return False


def is_valid_int(input_int, at_least, at_most):
	"""returns bool indicating input_int falls within the interval [at_least, at_most] (inclusive)

	Args:

		input_int - str - input integer
		at_least - int - the input_int should be at least this value
		at_most - int - the input_int should be at most this value

	Example Usage:

	>>> is_valid_int('1989', 1920, 2020)
	True
	>>> is_valid_int('203', 2010, 2020)
	False
	"""
	input_int = int(input_int)

	return input_int >= at_least and input_int <= at_most


def is_valid_hgt(input_hgt):
	"""returns bool indicating input_hgt consists of 
	a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76
	
	Args:

	input_hgt - str - height (in or cm) and unit
    """
	# Parse for unit (in or cm) and set cm flag
	try:

		_hgt, units = input_hgt[:-2], input_hgt[-2:]
		
		cm = True if units == 'cm' else False
		
		return is_valid_int(_hgt, 150, 193) if cm else is_valid_int(_hgt, 59, 76) 

	except:

		return False

def is_valid_hcl(input_hcl):
	"""returns bool indicating input_hcl consists of 
	a # followed by exactly six characters 0-9 or a-f e.g., '#142ad3'.
	
	Args:

		input_hcl - str - color in hex
	"""

	valid_chars = '0123456789abcdef'

	if len(input_hcl) == 7:

		if input_hcl[0] == '#':

			for char in input_hcl[1:]:

				if char not in valid_chars:

					return False

			return True

	return False


def is_valid_ecl(input_ecl):
	"""returns bool indicating input_ecl consists of 
	exactly one of: amb blu brn gry grn hzl oth

	Args:

		input_ecl - str - three digit description of hair color
	"""

	valid_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

	return input_ecl in valid_colors


def is_valid_pid(input_pid):
	"""returns bool indicating whether input_pid consists of
	a nine-digit number, including leading zeroes

	Args:

		input_pid - str - a nine-digit number (passport id), including leading zeroes
	"""

	valid_chars = '0123456789'

	if len(input_pid) == 9:

		for char in input_pid:

			if char not in valid_chars:

				return False

		return True

	return False


def is_passport_valid_2(passport_dict):
	"""returns bool indicating validity for additional validation of part 2"""

	if is_passport_valid(passport_dict):

		# Additional validation

		# Birth Year: four digits; at least 1920 and at most 2002
		byr = is_valid_int(passport_dict['byr'] , 1920, 2020)

		# Issue Year: four digits; at least 2010 and at most 2020
		iyr = is_valid_int(passport_dict['iyr'], 2010, 2020)

		# Expiration Year: four digits; at least 2020 and at most 2030
		eyr = is_valid_int(passport_dict['eyr'], 2020, 2030)

		# Height: a number followed by either cm or in
		    # If cm, the number must be at least 150 and at most 193.
		    # If in, the number must be at least 59 and at most 76.
		hgt = is_valid_hgt(passport_dict['hgt'])

		# Hair Color: a # followed by exactly six characters 0-9 or a-f.
		hcl = is_valid_hcl(passport_dict['hcl'])
		
		# Eye Color
		ecl = is_valid_ecl(passport_dict['ecl'])

		# Passport ID
		pid = is_valid_pid(passport_dict['pid'])

		if byr and iyr and eyr and hgt and hcl and ecl and pid:

			return True

	return False


def get_valid_passport_count(passport_dicts_list, part):
	"""returns count of valid passports

	Args:
	
		passport_dicts_list - list - list of passport dictionaries
		part - int - number indicating part number of question
	"""
	valid_password_count = 0

	# Determine part number and assign validation function to keyword valid

	if part == 1:
		
		valid = is_passport_valid

	elif part == 2:
		
		valid = is_passport_valid_2

	else:

		raise NotImplementedError("Part must be in [1, 2]")

	for passport_dict in passport_dicts_list:
		
		if valid(passport_dict):
			
			valid_password_count += 1

	return valid_password_count


if __name__ == '__main__':

	passports = get_passports_from_input('input.txt')
	passport_dicts_list = get_parameters_from_passports(passports)
	
	# # PART 1
	# # Detecting which passports have all required fields.
	# # fields: byr, iyr, eyr, hgt, hcl, ecl, pid, cid (8 fields)
	# # Each passport is represented as a key:value pairs seperated by space/new line
	# # Passports are separated by blank lines
	# # Treat cid as optional
	# # Count number of valid passports.

	
	valid_passport_count_1 = get_valid_passport_count(passport_dicts_list, 1)
	print("Part 1 valid passport count:", valid_passport_count_1)

	# # PART 2
	# # Count number of valid passports with the added validation parameters

	valid_passport_count_2 = get_valid_passport_count(passport_dicts_list, 2)
	print("Part 2 valid passport count:", valid_passport_count_2)