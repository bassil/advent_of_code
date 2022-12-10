"""Day 7: No Space Left On Device"""

class File():
	def __init__(self, name, size):
		self.name = name
		self.size = size


class Directory():
	def __init__(self, name, parent, root=None):
		self.root = self if name == "/" else root
		self.name = name
		self.parent = parent
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	@property
	def size(self):
		size = 0
		for child in self.children:
			size += child.size
		return size

	def cd(self, target_directory):
		if target_directory == "..":
			if self.parent is not None:
				return self.parent
		elif target_directory == "/":
			return self.root
		else:
			for child in self.children:
				if type(child) == Directory and child.name == target_directory:
					return child

	def find_directories(self, found=None):
		if not found:
			found = []
		for child in self.children:
			if type(child) == Directory:
				found.append((child, child.size))
				child.find_directories(found)
		return found

	def __repr__(self):
		return self.name


def parse_input(filename):
	with open(filename) as fp:
		data = fp.read().split("\n")
	return data


def create_fs(data):
	root = Directory("/", None)
	cwd = root
	
	while data:
		line = data.pop(0).split()
		if line[0] == "$":
			if line[1] == "cd":
				cwd = cwd.cd(line[2])
			else:
				while True:
					if not data:
						break
					if data[0].startswith("$"):
						break
					size, name = data.pop(0).split()
					if size == "dir":
						child_directory = Directory(name, cwd, root)
						cwd.add_child(child_directory)
					else:
						child_file = File(name, int(size))
						cwd.add_child(child_file)
	return root


def get_directory_sizes(data):
	root = create_fs(data)
	directories = root.find_directories()
	return root.size, directories


def part_1(directories):
	max_size = 100000
	values = [size for directory, size in directories if size < max_size]
	return sum(values)


def part_2(root_size, directories):
	total_disk_space = 70000000
	needed_disk_space = 30000000
	available_disk_space = total_disk_space - root_size

	values = sorted([size for directory, size in directories])

	for value in values:
		if available_disk_space + value >= needed_disk_space:
			return value
	return None



if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	root_size, directories = get_directory_sizes(data)
	print("part 1:", part_1(directories))
	print("part 2:", part_2(root_size, directories))