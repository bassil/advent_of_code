"""Day 14: Regolith Reservoir"""


def parse_input(filename):
    with open(filename) as fp:
        data = fp.read().split("\n")
    return data


def part_1(data):
    print(data)

if __name__ == "__main__":
    filename = "sample_input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))