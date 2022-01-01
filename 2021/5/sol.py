def get_data(file_name):
    with open(file_name, "r") as f:
        data = f.read().split("\n")
    data = [_.split(" -> ") for _ in data]
    parsed_data = []
    for entry in data:
        coords = []
        for pair in entry:
            parsed_pair = pair.split(",")
            coords.append([int(_) for _ in parsed_pair])
        parsed_data.append(coords)
    return parsed_data


def get_lines(data):
    straight_lines = []
    diagonal_lines = []
    for vent_line in data:
        [x1, y1], [x2, y2] = vent_line
        if x1 == x2 or y1 == y2:
            straight_lines.append(vent_line)
        else:
            # diagonal line conditions
            if abs(x1 - x2) == abs(y1 - y2):
                diagonal_lines.append(vent_line)
    return straight_lines, diagonal_lines


def get_vents_from_straight_line(straight_line):
    vents = []
    [_x1, _y1], [_x2, _y2] = straight_line
    if _x1 > _x2:
        x1 = _x2
        x2 = _x1
    else:
        x1 = _x1
        x2 = _x2
    if _y1 > _y2:
        y1 = _y2
        y2 = _y1
    else:
        y1 = _y1
        y2 = _y2
    if x1 == x2:
        for y in range(y1, y2 + 1):
            vents.append((x1, y))
    else:
        for x in range(x1, x2 + 1):
            vents.append((x, y1))
    return vents


def get_vents_from_diagonal_line(diagonal_line):
    vents = []
    [x1, y1], [x2, y2] = diagonal_line
    if x1 > x2:
        if y1 > y2:
            for i in range(x1 - x2 + 1):
                vents.append((x1 - i, y1 - i))
        else:
            for i in range(x1 - x2 + 1):
                vents.append((x1 - i, y1 + i))
    else:
        if y1 > y2:
            for i in range(x2 - x1 + 1):
                vents.append((x1 + i, y1 - i))
        else:
            for i in range(x2 - x1 + 1):
                vents.append((x1 + i, y1 + i))
    return vents


def get_count(straight_lines, diagonal_lines=None):
    ocean_floor = {}
    vents = []
    for straight_line in straight_lines:
        vents += get_vents_from_straight_line(straight_line)
    if diagonal_lines is not None and len(diagonal_lines) != 0:
        for diagonal_line in diagonal_lines:
            vents += get_vents_from_diagonal_line(diagonal_line)
    for vent in vents:
        if vent in ocean_floor:
            ocean_floor[vent] += 1
        else:
            ocean_floor[vent] = 1
    count = 0
    for value in ocean_floor.values():
        if value >= 2:
            count += 1
    return count


def part_1(data):
    straight_lines, diagonal_lines = get_lines(data)
    return get_count(straight_lines)


def part_2(data):
    straight_lines, diagonal_lines = get_lines(data)
    return get_count(straight_lines, diagonal_lines=diagonal_lines)


if __name__ == "__main__":
    test = False
    file_name = "sample.txt" if test else "input.txt"
    data = get_data(file_name)
    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
