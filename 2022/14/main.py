"""Day 14: Regolith Reservoir"""


def parse_input(filename):
    with open(filename) as fp:
        data = [[[int(___) for ___ in __.split(",")] for __ in _.split(" -> ")] for _ in fp.read().split("\n")]
    return data

class Cave:
    def __init__(self, data, start_position=(500, -1), floor=True):
        self.max_y = 0
        self.sand_count = 0
        self.sand_positions = []
        self.positions = self.get_positions(data)
        self.start_position = start_position
        

    def get_positions(self, data):
        # position_1: list[int, int], position_2: list[int,int]) -> set[tuple[int, int]]:
        positions = set()
        for line in data:
            for i in range(len(line) - 1):

                x_1, y_1 = line[i]
                x_2, y_2 = line[i + 1]

                if x_1 == x_2 and y_1 == y_2:
                    if y_1 > self.max_y:
                        self.max_y = y_1
                    positions.add((x_1, y_1))
                elif x_1 == x_2:
                    if y_1 > y_2:
                        start = y_2
                        end = y_1
                    else:
                        start = y_1
                        end = y_2
                    if end > self.max_y:
                        self.max_y = end
                    for y in range(start, end + 1):
                        positions.add((x_1, y))
                elif y_1 == y_2:
                    if x_1 > x_2:
                        start = x_2
                        end = x_1
                    else:
                        start = x_1
                        end = x_2
                    for x in range(start, end + 1):
                        positions.add((x, y_1))
        
        return positions

    def add_one_sand(self, floor=False):
        position = self.start_position
        current_position = self.start_position
        while True:
            # A unit of sand always falls:
            # 1) down one step, or
            # 2) diagonally one step down and to the left, or
            # 3) diagonally one step down and to the right

            current_position = (position[0], position[1]) # deep copy
            position = (position[0], position[1] + 1)

            # cannot move down one step
            if position in self.positions:
                # check diagonally one step down and to the left
                position = (current_position[0] - 1, current_position[1] + 1)
                if position not in self.positions:
                    continue

                # check diagonally one step down and to the right
                position = (current_position[0] + 1, current_position[1] + 1)
                if position not in self.positions:
                    continue

                # neither diagonally one step down and to the left or right
                self.positions.add(current_position)
                self.sand_positions.append(current_position)
                self.sand_count += 1
                if floor:
                    if current_position == (500, 0):
                        return True
                return False
            if not floor:
                if position[1] > self.max_y:
                    return True

    def add_sand_part_1(self):
        finished = False
        while not finished:
            finished = self.add_one_sand()

    def add_sand_part_2(self):
        floor = self.max_y + 2
        x, y = self.start_position
        y += floor + 1
        self.positions.add((x, y))
        for i in range(1, floor + 1):
            self.positions.add((x + i, y))
            self.positions.add((x - i, y))

        finished = False
        while not finished:
            finished = self.add_one_sand(floor=True)

def part_1(data):
    cave = Cave(data)
    cave.add_sand_part_1()
    return cave.sand_count


def part_2(data):
    cave = Cave(data)
    cave.add_sand_part_2()
    return cave.sand_count


if __name__ == "__main__":
    filename = "input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))
    print("part 2:", part_2(data))