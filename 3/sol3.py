def get_coords(length, slope_x, slope_y):
	"""return dictionary of coordinates in travel path 
	keyed on y distance from origin
	"""
	coords = {}
	coords[0] = (0, 0)
	y = 1

	while y < length:
	
		coords[y] = (slope_x*(y), slope_y*(y))
		y += 1
		
	return coords

def trees_encountered(travel_map, coords, slope_y):
	"""return count of trees encountered in travel map
	based on coordinates in coords
	"""
	num_trees = 0

	for y, grid_line in enumerate(travel_map[::slope_y]):

		if coords[y][1] > len(travel_map):
			
			break
		
		if grid_line[coords[y][0] % len(grid_line)] == '#':
			
			num_trees += 1

	return num_trees

if __name__ == "__main__":

	travel_map = []

	with open("./input3.txt") as file:

		for line in file:
			travel_map.append(line.strip())
	
	length = len(travel_map)
	# slope_x = 1
	# slope_y = 2	

	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

	num_trees = 1
	num_trees_list = []
	
	for slope_x, slope_y in slopes:

		coords = get_coords(length, slope_x, slope_y)

		num_trees_list.append(trees_encountered(travel_map, coords, slope_y))

	for _num_trees in num_trees_list:
		
		num_trees *= _num_trees

print(num_trees, num_trees_list)
	

	