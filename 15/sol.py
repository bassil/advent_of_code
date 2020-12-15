def part_1(starting_nums, turns):
	# instantiate turn_last_spoken, fill with starting nums, and
	# maintain number of times spoken
	turn_last_spoken = {}

	for i, starting_num in enumerate(starting_nums):
		if starting_num in turn_last_spoken:
			turn_last_spoken[starting_num][0].append(i + 1) 
			turn_last_spoken[starting_num][1] += 1
		else:
			turn_last_spoken[starting_num] = [[i + 1], 1]
	
	most_recently_spoken = starting_nums[-1]
	
	turn = len(starting_nums)

	while turn < turns:
		turn += 1
		
		if turn_last_spoken[most_recently_spoken] and \
			turn_last_spoken[most_recently_spoken][1] > 1:

			number_spoken = turn_last_spoken[most_recently_spoken][0][-1] - \
				turn_last_spoken[most_recently_spoken][0][-2]
			
		else:
			number_spoken = 0
		
		if number_spoken in turn_last_spoken:
			turn_last_spoken[number_spoken][0].append(turn)
			turn_last_spoken[number_spoken][1] += 1
		else:
			turn_last_spoken[number_spoken] = [[turn], 1]

		starting_nums.append(number_spoken)
		most_recently_spoken = number_spoken
	return starting_nums

def main():
	with open("input.txt") as f:
		starting_nums = [int(_) for _ in f.read().split(',')]

	turns_1 = 2020
	print("Part 1:", part_1(starting_nums, turns_1)[-1])
	turns_2 = 30000000
	print("Part 2:", part_1(starting_nums, turns_2)[-1])

if __name__ == '__main__':
	main()