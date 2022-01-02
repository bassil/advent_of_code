def get_data(file_name):
    data = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            data.append([_.split() for _ in line.split(" | ")])
            line = f.readline()
    return data

def part_1(data):
    pass


if __name__ == '__main__':
    test = True
    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)

    print("Part 1:", part_1(data))