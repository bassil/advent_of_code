from itertools import product

def binary_digits_to_int(binary_digits):
	binary_string = ""
	for bin_digit in binary_digits:
		binary_string += bin_digit
	return int(binary_string, 2)

def apply_mask_to_value(mask, binary_string):
	"""returns int of mask applied to binary string"""
	bin_digits = []
	mask_digits = [char for char in mask if char != ' ']
	output_digits = []
	for digit in binary_string.split("0b")[1]:
		bin_digits.append(digit)
	
	front_pad = ['0' for _ in range(len(mask_digits)-len(bin_digits))]
	bin_digits = front_pad + bin_digits

	for i, bin_digit in enumerate(bin_digits):
		if mask_digits[i] != 'X':
			bin_digits[i] = mask_digits[i]

	return binary_digits_to_int(bin_digits)

def part_1(initialization_program):
	mem = {}
	mask = ""

	for line in initialization_program:
		var, inp = line.split("=")
		if var == "mask ":
			mask = inp
		else:
			address = int(var.split("[")[1].split("]")[0])
			binary_string = bin(int(inp))

			mem[address] = apply_mask_to_value(mask, binary_string)

	return sum(mem.values())


def apply_mask_to_address(mask, address):
	"""return list of addresses for floating bits applied to address"""
	mask_digits = [char for char in mask if char != " "]
	address_digits = []
	address = bin(address)
	for address_bit in address.split('0b')[1]:
		address_digits.append(address_bit)
	# pad address digits with leading 0's
	front_pad = ['0' for _ in range(len(mask_digits) - len(address_digits))]
	address_digits = front_pad + address_digits

	addresses = []

	# first apply '1' digits from mask to address
	for i, mask_digit in enumerate(mask_digits):
		if mask_digit == '1':
			address_digits[i] = mask_digit

	if 'X' not in mask_digits:
		return binary_digits_to_int(address_digits)

	# determine combination of addresses for the number of floating bits in mask
	# e.g., 3 floating bits -> 8 addresses
	floating_bits = 0
	floating_bit_indices = []
	for i, mask_digit in enumerate(mask_digits):
		if mask_digit == 'X':
			floating_bits += 1
			floating_bit_indices.append(i)

	# add replacement bits to address at floating bit positions and append the address
	for replacement_bits in product('01', repeat=floating_bits):
		for i, replacement_bit in enumerate(replacement_bits):
			address_digits[floating_bit_indices[i]] = replacement_bit
		addresses.append(binary_digits_to_int(address_digits))
	
	return addresses
	
	

def part_2(initialization_program):
	mem = {}
	mask = ""

	for line in initialization_program:
		var, inp = line.split("=")
		if var == "mask ":
			mask = inp
		else:
			address = int(var.split("[")[1].split("]")[0])
			addresses = apply_mask_to_address(mask, address)
			for _address in addresses:
				mem[_address] = int(inp)

	return sum(mem.values())
				

def main():
	with open("input.txt") as f:
		initialization_program = f.read().split("\n")

	print("Part 1:", part_1(initialization_program))
	print("Part 2:", part_2(initialization_program))

if __name__ == '__main__':
	main()