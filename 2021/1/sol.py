def get_data(file_name):
    with open(file_name, "r") as f:
        data = [int(_) for _ in f.read().split("\n")]
    return data


def part_1(data):
    num_increasing = 0
    for i in range(1, len(data)):
        current_depth = data[i]
        previous_depth = data[i - 1]
        if current_depth > previous_depth:
            # print(f"iteration {i}:", data[i], data[i-1])
            num_increasing += 1
    return num_increasing


def part_2(data):
    # create sums of sliding window
    windowed_data = []
    for i in range(len(data) - 2):
        windowed_data.append(data[i] + data[i+1] + data[i+2])
    return part_1(windowed_data)


if __name__ == "__main__":
    test = False
    if test:
        data = get_data("sample.txt")
    else:
        data = get_data("input.txt")
    print(
        "Part 1: Number of measurements larger than previous -",
        part_1(data),
    )

    print(
        "Part 2: Number of measurements in a sliding window of 3 that are "
        + "larger than previous -",
        part_2(data),
    )
