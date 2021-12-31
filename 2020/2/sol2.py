def get_letter_count(letter, string):
	letter_count = 0
	for char in string:
		if char == letter:
			letter_count += 1
	return letter_count



def valid_passwords(passwords):
	num_valid_passwords = 0
	for password in passwords:
		
		password_policy = password[0]
		password_letter = password[1]
		password = password[2]
		
		# password_letter_count = get_letter_count(password_letter, password)
		# lower, upper = [int(_) for _ in password_policy.split('-')]
		# if password_letter_count >= lower and password_letter_count <= upper:
			# num_valid_passwords += 1

		lower_index, upper_index = [(int(_) - 1) for _ in password_policy.split('-')]
		
		if (password[lower_index] == password_letter) ^ (password[upper_index] == password_letter):
			num_valid_passwords += 1
		

	return num_valid_passwords


if __name__ == "__main__":

	passwords= []

	with open("./input2.txt") as file:

		for line in file:
			line_list = line.split()
			passwords.append([line_list[0], 
							  line_list[1].strip(':'),
							  line_list[2]])

	print(valid_passwords(passwords))
