with open("input.txt") as f:
	regulations = f.read().split("\n")

children_dict = dict()
parents_dict = dict()

for rules in regulations:
	rules_ = [_.strip(' .') for _ in rules.split("contain")]
	
	parent_bag = rules_[0].split(' ')
	parent_bag = "{} {}".format(parent_bag[0], parent_bag[1])

	children_bags = [_.strip().split(' ') for _ in rules_[1].split(",")]
	parsed_children_bags = ["{} {}".format(_[1], _[2]) for _ in children_bags]

	for child in parsed_children_bags:
		if child not in children_dict:
			children_dict[child] = []
		children_dict[child].append(parent_bag)

	if parent_bag not in parents_dict:
		parents_dict[parent_bag] = []

	parents_dict[parent_bag].extend([("{} {}".format(_[1], _[2]), _[0]) for _ in children_bags])



# Part 1
# def get_all_parents(child):
# 	parents_set = set()
# 	parents_stack = children_dict[child]
	
# 	while len(parents_stack) > 0:
# 		parent = parents_stack.pop()
# 		parents_set.add(parent)
# 		if parent in children_dict:
# 			parents_stack.extend(children_dict[parent])		
		
# 	return parents_set

# shiny_gold_parents = get_all_parents('shiny gold')

# print("Part 1:", len(shiny_gold_parents))

# Part 2
NUM_BAGS = 0

def get_all_children(parent):
	global NUM_BAGS

	if parents_dict[parent] == [('other bags', 'no')]:

		return 1

	for child in parents_dict[parent]:

		# how many children at this level?
		for num_twins in range(int(child[1])):
			NUM_BAGS += 1

			get_all_children(child[0])

		# return int(child[1])*get_all_children(child[0])

shiny_gold_children = get_all_children('shiny gold')

print("Part 2:", NUM_BAGS)