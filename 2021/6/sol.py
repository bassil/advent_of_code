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


if __name__ == "__main__":
    test = False
    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)
    days = 80
    print(f"Part 1: Number of lanternfish after {days} days", part_1(data, days))
