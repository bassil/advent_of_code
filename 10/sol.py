
if __name__ == '__main__':
	
	with open('input.txt') as f:
		joltage_adapters = f.read().split('\n')

	joltage_ratings = sorted([int(_) for _ in joltage_adapters])
	
	device_joltage_rating = max(joltage_ratings) + 3

	joltage_ratings.insert(0, 0)
	joltage_ratings.append(device_joltage_rating)
	
	jolt_difference_1 = 0
	jolt_difference_3 = 0

	for i in range(1, len(joltage_ratings)):
		if joltage_ratings[i] - joltage_ratings[i-1] == 1:
			# print(1 ,joltage_ratings[i], joltage_ratings[i-1])
			jolt_difference_1 += 1
		elif joltage_ratings[i] - joltage_ratings[i-1] == 3:
			# print(3, joltage_ratings[i], joltage_ratings[i-1])
			jolt_difference_3 += 1
		else:
			print("not 1 or 3")

	# print("Part 1:", jolt_difference_1 * jolt_difference_3)

	
	memo = [0 for i in range(len(joltage_ratings))]
	
	memo[0] = 1
	
	for i in range(len(joltage_ratings)):
		if i == 0:
			continue
		arrangement = 0
		for j in range(1, 4):
			if i - j < 0:
				continue
			if joltage_ratings[i] - joltage_ratings[i - j] <= 3:
				arrangement += memo[i - j]
			memo[i] = arrangement
	print("Part 2:", memo[-1])
	
