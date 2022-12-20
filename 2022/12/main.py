"""Day 12: Hill Climbing Algorithm"""
import pprint
class Node:
    def __init__(self, position, value):
        self.position = position
        self.value = value
    
    @property
    def height(self):
        if self.value == "S":
            _height = 96
        elif self.value == "E":
            _height = 100
        else:
            _height = ord(self.value)
        return _height

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

        if row > 0:
            possible_neighbors.append(self.grid[row - 1][col])
        if row < self.num_rows - 1:
            possible_neighbors.append(self.grid[row + 1][col])
        if col > 0:
            possible_neighbors.append(self.grid[row][col - 1])
        if col < self.num_cols - 1:
            possible_neighbors.append(self.grid[row][col + 1])
        for neighbor in possible_neighbors:
            if ((node.height == neighbor.height) or (node.height == neighbor.height - 1)):
                neighbors.append(neighbor)
        return neighbors

    def shortest_path(self, current_node, destination_node):
        self.visited.add(current_node)
        # print("current node:", current_node)
        # print("destination node:", destination_node)
        # print("Memo:")
        # for item in self.memo:
        #     print(item, "shortest path:", self.memo[item])
            
        if current_node == destination_node:
            return 0
        elif current_node in self.memo:
            return self.memo[current_node]
        else:
            neighbors = self.get_neighbors(current_node)
            paths = []
            # Seems like we iterate through the neighbors 
            # and only call shortest path on the neighbors we haven't seen before...
            # this seems to make sense, why should we make 2 recursive calls for the same node?
            # I guess, could it be the case that the shortest path from one recursive call is different
            # from the shortest path from another recursive call?
            for neighbor in neighbors:
                if neighbor in self.visited:
                    # TODO - Is it true that we should continue here?
                    # if we don't we get maximum recursion depth exceeded...
                    # What is really going on here?
                    continue
                path = self.shortest_path(neighbor, destination_node)
                paths.append(path)
                print(paths)
            if len(paths) == 0:
                return 0
            # TODO - The logic here needs improving. The
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
    filename = "sample_input2.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))