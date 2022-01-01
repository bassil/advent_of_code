def get_data(file_name):
	with open(file_name, "r") as f:
		data = f.read().split("\n")
	data = [_.split(" -> ") for _ in data]
	parsed_data = []
	for entry in data:
		coords = []
		for pair in entry:
			parsed_pair = pair.split(",")
			coords.append(parsed_pair)
		parsed_data.append(coords)
	return parsed_data

if __name__ == '__main__':
	test = True
	file_name = "sample.txt" if test else "input.txt"
	data = get_data(file_name)
	