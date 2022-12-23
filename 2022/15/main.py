"""Day 15: Beacon Exclusion Zone"""
import re

from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    def manhattan_distance(self, other):
        """returns the manhattan distance between two points:
        the manhattan distance between two points is 
        the sum of the x distance and the y distance
        see: https://en.wikipedia.org/wiki/Taxicab_geometry
        """
        distance = self - other
        return abs(distance.x) + abs(distance.y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Coordinate - (x: {self.x}, y:{self.y})"


class Cave:
    def __init__(self):
        self.sensors = {}
        self.beacons = set()

    @property
    def min_x(self):
        return min([sensor.x - distance for sensor, distance in self.sensors.items()]) 

    @property
    def max_x(self):
        return max([sensor.x + distance for sensor, distance in self.sensors.items()])
    
    def add_sensor(self, sensor, distance):
        if sensor in self.sensors:
            raise Exception(f"{sensor} cannot be added, already found")
        
        self.sensors[sensor] = distance

    def add_beacon(self, beacon):
        self.beacons.add(beacon)

    def is_occupied(self, position):
        for sensor, distance in self.sensors.items():
            if position not in self.beacons and position.manhattan_distance(sensor) <= distance:
                return True
        return False

    def check_row(self, y: int) -> int:
        # if the distance from a point to the sensor is <= distance (e.g., self.sensors[sensor]),
        # that position is not possible
        count = 0
        for x in range(self.min_x, self.max_x):
            position = Coordinate(x, y)
            if self.is_occupied(position):
                count += 1
        return count
    
    def find_beacon(self, lower=0, upper=20):
        for sensor, distance in self.sensors.items():
            # check the radius around a sensor
            for _x in range(distance + 2):
                _y = distance - _x + 1
                for dx, dy in ([1, 1], [1, -1], [-1, 1], [-1, -1]):
                    position = Coordinate(sensor.x + (_x * dx), sensor.y + (_y * dy))
                    if not (lower <= position.x <= upper and lower <= position.y <= upper):
                        continue
                    if not self.is_occupied(position) and position not in self.beacons:
                        return position

def parse_input(filename, pattern):
    with open(filename) as fp:
        data = [
            [
                [int(__.group(1)), int(__.group(2))], [int(__.group(3)), int(__.group(4))]
            ] 
            for __ in [
                re.search(pattern, _) for _ in fp.read().split("\n")
            ]
        ]
    return data


def instantiate_cave(data):
    cave = Cave()
    for [sensor_x, sensor_y], [beacon_x, beacon_y] in data:
        sensor = Coordinate(sensor_x, sensor_y)
        beacon = Coordinate(beacon_x, beacon_y)
        distance = sensor.manhattan_distance(beacon)
        cave.add_sensor(sensor, distance)
        cave.add_beacon(beacon)
    return cave


def part_1(cave, row=10):
    return cave.check_row(row)


def part_2(cave, lower=0, upper=20):
    beacon = cave.find_beacon(lower, upper)
    return beacon.x * 4000000 + beacon.y
    

if __name__ == "__main__":
    filename = "input.txt"
    pattern = r"^Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)$"
    data = parse_input(filename, pattern)
    cave = instantiate_cave(data)
    # print("part 1:", part_1(cave))
    print("part_2:", part_2(cave, upper=4000000))
