def get_intervals_from_fields(fields):
	intervals = {}
	valid_values = set()
	for field in fields:
		field_name, field_intervals = field.split(": ")
		intervals[field_name] = set()
		field_intervals = field_intervals.split(" or ")
		for field_interval in field_intervals:
			start, stop = field_interval.split("-")
			for interval_value in range(int(start), int(stop) + 1):
				intervals[field_name].add(interval_value)
				valid_values.add(interval_value)
	return intervals, valid_values

def part_1(notes):
	fields, ticket, nearby_tickets = notes
	intervals, valid_values = get_intervals_from_fields(fields)
	invalid_values = []
	for nearby_ticket in nearby_tickets[1:]:
		for value in nearby_ticket.split(","):
			if int(value) not in valid_values:
				invalid_values.append(int(value)) 
	return sum(invalid_values)

def get_valid_tickets(nearby_tickets, valid_values):
	valid_tickets = []
	for nearby_ticket in nearby_tickets:
		valid_ticket = True
		for value in nearby_ticket.split(","):
			if int(value) not in valid_values:
				valid_ticket = False
		if valid_ticket:
			valid_tickets.append([int(_) for _ in nearby_ticket.split(",")])
	return valid_tickets

def value_in_interval(value, interval_set):
	return value in interval_set

def get_mapped_fields(notes):
	fields, ticket, nearby_tickets = notes
	intervals, valid_values = get_intervals_from_fields(fields)
	valid_tickets = get_valid_tickets(nearby_tickets[1:], valid_values)
	# This is the transpose of the valid tickets:
	# e.g., valid_tickets_t[0] is a list of all values in the first column, ...
	valid_tickets_t = list(map(list, zip(*valid_tickets)))
	fields_map = {}
	for i in range(len(valid_tickets_t)):
		for field in intervals:
			if all([value_in_interval(value, intervals[field]) \
			       for value in valid_tickets_t[i]]): 
				if field in fields_map:
					fields_map[field].append(i)
				else:
					fields_map[field] = [i]
	max_length = 2
	mapped_fields = {}
	while max_length > 1:
		max_length = 0
		for field in fields_map:
			if len(fields_map[field]) > max_length:
				max_length = len(fields_map[field])
		for field in fields_map:
			if len(fields_map[field]) == 1 and field not in mapped_fields:
				mapped_fields[field] = fields_map[field][0]
		for mapped_field in mapped_fields:
			for field in fields_map:
				if field != mapped_field and mapped_fields[mapped_field] in fields_map[field]:
					fields_map[field].remove(mapped_fields[mapped_field])
	return mapped_fields
		
def part_2(notes):
	ticket = [int(_) for _ in notes[1][1].split(',')]
	departure_values = 1
	departure_indices = []
	mapped_fields = get_mapped_fields(notes)
	for mapped_field in mapped_fields:
		if mapped_field.split()[0] == 'departure':
			departure_indices.append(mapped_fields[mapped_field])
	for departure_index in departure_indices:
		departure_values *= ticket[departure_index]
	return departure_values

def main():
	with open("input.txt") as f:
		notes = [_.split("\n") for _ in f.read().split("\n\n")]


	# print("Part 1:", part_1(notes))
	print("Part 2:", part_2(notes))

if __name__ == '__main__':
	main()