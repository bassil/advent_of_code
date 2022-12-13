"""Day 12: Hill Climbing Algorithm"""

class Node:
    def __init__(self, position, value):
        self.position = position
        self.value = value
    
    def __hash__(self):
        return hash(tuple(self.position))

    def __repr__(self):
        return f"Node: - {self.value} - {self.position}"


class Grid:
    def __init__(self, data):
        self.num_rows = len(data)
        self.num_cols = len(data[0])
        self.grid = self.create_grid(data)
        self.memo = {self.end: 0}
        self.visited = set()

    def create_grid(self, data):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                position = [row, col]
                value = data[row][col]
                node = Node(position, value)
                if value == "S":
                    self.start = node
                elif value == "E":
                    self.end = node
                data[row][col] = node
        return data

    def get_neighbors(self, node):
        possible_neighbors = []
        neighbors = []
        row, col = node.position
        if node.value == "S":
            value = 96
        elif node.value == "E":
            value = 123
        else:
            value = ord(node.value)

        if row > 0:
            possible_neighbors.append(self.grid[row - 1][col])
        if row < self.num_rows - 1:
            possible_neighbors.append(self.grid[row + 1][col])
        if col > 0:
            possible_neighbors.append(self.grid[row][col - 1])
        if col < self.num_cols - 1:
            possible_neighbors.append(self.grid[row][col + 1])

        for neighbor in possible_neighbors:
            if (
                (value == ord(neighbor.value)) or
                (value == ord(neighbor.value) - 1)
            ):
                neighbors.append(neighbor)
        return neighbors

    def shortest_path(self, current_node, destination_node):
        self.visited.add(current_node)
        if current_node == destination_node:
            return 0
        elif current_node in self.memo:
            return self.memo[current_node]
        else:
            neighbors = self.get_neighbors(current_node)
            paths = []
            for neighbor in neighbors:
                if neighbor in self.visited:
                    continue
                path = self.shortest_path(neighbor, destination_node)
                paths.append(path)
            if len(paths) == 0:
                return 0
            _shortest_path = min(paths) + 1
            self.memo[current_node] = _shortest_path
            return _shortest_path


def parse_input(filename):
    with open(filename) as fp:
        data = [list(line) for line in fp.read().split("\n")]
    return data


def part_1(data):
    grid = Grid(data)
    print(grid.shortest_path(grid.start, grid.end))


if __name__ == "__main__":
    filename = ".\sample_input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))