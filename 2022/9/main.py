"""Day 9: Rope Bridge"""
from copy import deepcopy

def parse_input(filename):
	with open(filename) as fp:
		data = [line.split() for line in fp.read().split("\n")]
	return data


def part_1(data):
	head_coords = (0, 0)
	previous_head_coords = (0, 0)
	tail_visited = {(0, 0)}

	for direction, num_steps in data:
		num_steps = int(num_steps)
		for step in range(num_steps):
			move = deepcopy(head_coords)
			if direction == "R":
				move = (move[0] + 1, move[1])
			elif direction == "L":
				move = (move[0] - 1, move[1])
			elif direction == "U":
				move = (move[0], move[1] + 1)
			elif direction == "D":
				move = (move[0], move[1] - 1)
			else:
				raise Exception("Invalid direction")

			# if applying the move makes H more than dist:1 away from T, move T
			x_distance = abs(move[0] - previous_head_coords[0])
			y_distance = abs(move[1] - previous_head_coords[1])

			if x_distance > 1 or y_distance > 1:
				previous_head_coords = deepcopy(head_coords)
			tail_visited.add(previous_head_coords)
			head_coords = deepcopy(move)

	return len(tail_visited)

def part_2(data):
	previous_coords = [(0, 0)] * 10
	current_coords = [(0, 0)] * 10
	tail_visited = {(0, 0)}
	for direction, num_steps in data:
		num_steps = int(num_steps)

		print("------ instruction:", direction, num_steps)

		for step in range(num_steps):

			print("---- step:", step + 1)

			move = deepcopy(previous_coords[0])

			if direction == "R":
				move = (1, 0)
			elif direction == "L":
				move = (- 1, 0)
			elif direction == "U":
				move = (0, 1)
			elif direction == "D":
				move = (0, - 1)
			else:
				raise Exception("Invalid direction")

			for i in range(len(current_coords)):
				print("i", i)
				new_coords = (current_coords[i][0] + move[0], current_coords[i][1] + move[1])
				if i == 0:
					current_coords[i] = new_coords

				else:
					x_distance = abs(current_coords[i - 1][0] - current_coords[i][0])
					y_distance = abs(current_coords[i - 1][1] - current_coords[i][1])

					if max(x_distance, y_distance) > 1:
						print("--- update ---")
						current_coords[i] = new_coords

				
				print("current:", current_coords[i])
				print("previous:", previous_coords[i])
				print()			
			tail_visited.add(current_coords[9])
			previous_coords = deepcopy(current_coords)

		print()
		print()
	return len(tail_visited)


if __name__ == '__main__':
	filename = "sample_input.txt"
	data = parse_input(filename)
	# print("part 1:", part_1(data))
	print("part 2:", part_2(data))