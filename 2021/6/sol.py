def get_data(file_name):
    with open(file_name, "r") as f:
        data = [int(_) for _ in f.read().split(",")]
    return data


def simulate_day(data):
    new_fish = []
    for i, fish in enumerate(data):
        if fish == 0:
            data[i] = 6
            new_fish.append(8)
        else:
            data[i] -= 1
    data.extend(new_fish)
    return data


def part_1(data, days):
    for day in range(days):
        data = simulate_day(data)
    return len(data)


def part_2(data, days):
    counts = {i: 0 for i in range(9)}
    for fish in data:
        counts[fish] += 1
    for day in range(days):
        new_fish = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[6] += new_fish
        counts[8] = new_fish
    return sum(counts.values())


if __name__ == "__main__":
    test = False
    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)
    days_1 = 80
    data_1 = data.copy()
    print(f"Part 1: Number of lanternfish after {days_1} days", part_1(data_1, days_1))
    days_2 = 256
    data_2 = data.copy()
    print(f"Part 2: Number of lanternfish after {days_2} days", part_2(data_2, days_2))
