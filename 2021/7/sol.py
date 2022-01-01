def get_data(file_name):
    with open(file_name, "r") as f:
        data = [int(_) for _ in f.read().split(",")]
    return data

def part_1(data):
    min_cost = max(data) * len(data)
    for end_position in range(max(data)):
        cost = 0
        for crab_position in data:
            cost += abs(crab_position - end_position)
        if cost < min_cost:
            min_cost = cost 
    return min_cost

if __name__ == '__main__':
    test = False
    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)

    print("Part 1:", part_1(data))