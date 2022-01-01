def get_data(file_name):
    with open(file_name, "r") as f:
        data = f.read().split("\n")
        return data


def get_bit_count_by_position(data):
    bit_count_by_position = {_: [0, 0] for _ in range(len(data[0]))}

    for binary_number in data:
        for i, bit in enumerate(binary_number):
            bit_count_by_position[i][int(bit)] += 1
    return bit_count_by_position


def get_gamma_rate(bit_count_by_position):
    gamma_rate = ""
    for i in range(len(bit_count_by_position)):
        if bit_count_by_position[i][0] > bit_count_by_position[i][1]:
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    gamma_rate = int(gamma_rate, 2)
    return gamma_rate


def get_epsilon_rate(bit_count_by_position):
    epsilon_rate = ""
    for i in range(len(bit_count_by_position)):
        if bit_count_by_position[i][0] < bit_count_by_position[i][1]:
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"
    epsilon_rate = int(epsilon_rate, 2)
    return epsilon_rate


def part_1(data):
    bit_count_by_position = get_bit_count_by_position(data)
    gamma_rate = get_gamma_rate(bit_count_by_position)
    epsilon_rate = get_epsilon_rate(bit_count_by_position)
    return gamma_rate * epsilon_rate


def get_most_common_bit(bit_count):
    return "0" if bit_count[0] > bit_count[1] else "1"


def get_least_common_bit(bit_count):
    return "0" if bit_count[0] <= bit_count[1] else "1"

def filter(data, position, bit):
	filtered_data = []
	for binary_number in data:
		if binary_number[position] == bit:
			filtered_data.append(binary_number)
	return filtered_data

def get_oxygen_generator_rating(data):
	digits = len(data[0])
	for position in range(digits):
		bit_count_by_position = get_bit_count_by_position(data)
		mcb = get_most_common_bit(bit_count_by_position[position])
		data = filter(data, position, mcb)
		if len(data) == 1:
			return int(data[0], 2)


def get_CO2_generator_rating(data):
	digits = len(data[0])
	for position in range(digits):
		bit_count_by_position = get_bit_count_by_position(data)
		lcb = get_least_common_bit(bit_count_by_position[position])
		data = filter(data, position, lcb)
		if len(data) == 1:
			return int(data[0], 2)


def part_2(data):
    oxygen_generator_rating = get_oxygen_generator_rating(data)
    CO2_generator_rating = get_CO2_generator_rating(data)
    return oxygen_generator_rating * CO2_generator_rating


if __name__ == "__main__":
    test = False

    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
