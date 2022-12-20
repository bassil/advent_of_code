"""Day 12: Hill Climbing Algorithm"""


from heapq import heappop, heappush


class Node:
    def __init__(self, position, value):
        self.position = position
        self.value = value
    
    @property
    def height(self):
        if self.value == "S":
            _height = 97
        elif self.value == "E":
            _height = 122
        else:
            _height = ord(self.value)
        return _height

    def __lt__(self, other):
        return self.position < other.position

    def __hash__(self):
        return hash(tuple(self.position))

    def __repr__(self):
        return f"Node: - {self.value} - {self.position}"


class Grid:
    def __init__(self, data):
        self.num_rows = len(data)
        self.num_cols = len(data[0])
        self.grid = self.create_grid(data)

    def create_grid(self, data):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                position = [row, col]
                value = data[row][col]
                node = Node(position, value)
                if value == "E":
                    self.start = node
                elif value == "S":
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
            if neighbor.height >= node.height - 1:
                neighbors.append(neighbor)
        return neighbors

    def shortest_path(self, end_value = None):
        visited = [[False] * self.num_cols for _ in range(self.num_rows)]
        steps = 0
        heap = [(steps, self.start)]
        while True:
            steps, node = heappop(heap)
            row, col = node.position
            
            if visited[row][col]:
                continue
            
            visited[row][col] = True

            if end_value:
                if node.value == end_value:
                    break

            if node == self.end:
                break
            
            for neighbor in self.get_neighbors(node):
                heappush(heap, (steps + 1, neighbor))
        return steps
        


def parse_input(filename):
    with open(filename) as fp:
        data = [list(line) for line in fp.read().split("\n")]
    return data


def part_1(data):
    grid_1 = Grid(data)
    shortest_path = grid_1.shortest_path()
    return shortest_path

def part_2(data):
    grid_2 = Grid(data)
    shortest_path = grid_2.shortest_path(end_value="a")
    return shortest_path


if __name__ == "__main__":
    filename = "input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))
    print("part 2:", part_2(data))
