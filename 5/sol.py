def get_ticket(input_name):
	
	with open(input_name) as f:
		tickets = [line.strip('\n') for line in f]

	return tickets


def get_row_and_col(ticket):
	row = ticket[:7].replace("F", "0").replace("B", "1")
	col = ticket[7:].replace("L", "0").replace("R", "1")

	row_num = int(row, 2)
	col_num = int(col, 2)
	
	return row_num, col_num


def get_seat_id(row_num, col_num, row_mult=8):
	return row_num * row_mult + col_num


def part_1(input_name):
	tickets = get_ticket('input.txt')
	return max([get_seat_id(row_num, col_num) for row_num, col_num in \
		[get_row_and_col(ticket) for ticket in tickets]])


def part_2(input_name):
	raise NotImplementedError

if __name__ == '__main__':

	print("Part 1:", part_1("input.txt"))