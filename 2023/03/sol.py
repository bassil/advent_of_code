from typing import List, Set, Tuple

class Part:
    def __init__(self, part_number: int, coordinates: List[Tuple[int, int]]) -> None:
        """Initialize an instance of the Part class
        Args: 
            part_number: int. The part number of the part
            coordinates: List[Tuple[int]]. Coordinates of the part in the schematic. [(row, col), ...]
        """
        self.part_number: int = part_number
        self.coordinates: List[Tuple[int, int]] = coordinates

    def __repr__(self) -> str:
        return f"part number: {self.part_number}\n coordinates: {self.coordinates}\n"


def parse_input(input_filename: str) -> Tuple[List[Part], Set[Tuple[int, int]]]:
    with open(input_filename) as fp:
        lines = fp.readlines()
    lines = [line.strip() for line in lines]
    parts: List[Part] = []
    for row_coordinate, row in enumerate(lines):
        part_number = ""
        coordinates = []
        for column_coordinate, column in enumerate(row):
            if column.isnumeric():
                coordinates.append((row_coordinate, column_coordinate))
                part_number += column
                if column_coordinate == len(row) - 1:
                    part = Part(int(part_number), coordinates)
                    parts.append(part)
                    part_number = ""
                    coordinates = []
            else:
                if part_number and coordinates:
                    part = Part(int(part_number), coordinates)
                    parts.append(part)
                    part_number = ""
                    coordinates = []

    symbol_coordinates: Set[Tuple[int, int]] = set()
    for row_coordinate, row in enumerate(lines):
        part_number = ""
        coordinates = []
        for column_coordinate, column in enumerate(row):
            if not column.isnumeric():
                 if column != ".":
                    symbol_coordinates.add((row_coordinate, column_coordinate))
    return parts, symbol_coordinates


def _get_adjacent_coordinates(part: Part) -> Set[Tuple[int, int]]:
    adjacent_coordinates = set()
    for row_coordinate, column_coordinate in part.coordinates:
        # up
        adjacent_coordinates.add((row_coordinate - 1, column_coordinate))
        # down
        adjacent_coordinates.add((row_coordinate + 1, column_coordinate))
        # left
        adjacent_coordinates.add((row_coordinate, column_coordinate - 1))
        # right
        adjacent_coordinates.add((row_coordinate, column_coordinate + 1))
        # up left
        adjacent_coordinates.add((row_coordinate - 1, column_coordinate - 1))
        # up right
        adjacent_coordinates.add((row_coordinate - 1, column_coordinate + 1))
        # down left
        adjacent_coordinates.add((row_coordinate + 1, column_coordinate - 1))
        # down right
        adjacent_coordinates.add((row_coordinate + 1, column_coordinate + 1))
    return adjacent_coordinates


def part_1(parts: List[Part], symbols: Set[Tuple[int, int]]) -> int:
    # print(parts)
    result = 0
    for part in parts:
        adjacent_coordinates: Set = _get_adjacent_coordinates(part)
        if symbols.intersection(adjacent_coordinates):
            result += part.part_number
    return result


def main():
    input_filename = "input.txt"
    parts, symbols = parse_input(input_filename)
    print("part 1:", part_1(parts, symbols))

if __name__ == "__main__":
    main()
