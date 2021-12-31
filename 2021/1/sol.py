def get_data(file_name):
    with open(file_name, "r") as f:
        data = f.read().split("\n")
    return data


def part_1(data):
    num_increasing = 0
    for i in range(1, len(data)):
        print(f"iteration {i}:", data[i], data[i-1])
        if data[i] > data[i - 1]:
            # print(f"iteration {i}:", data[i], data[i-1])
            num_increasing += 1
    return num_increasing


if __name__ == "__main__":
    test = False
    if test:
        data = get_data("sample.txt")
    else:
        data = get_data("input.txt")
    print(
        "Part 1: Number of measurements larger than the previous measurement -",
        part_1(data)
    )