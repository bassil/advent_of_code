"""Day 13: Distress Signal

Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.

When comparing two values, the first value is called left and the second value is called right. Then:

    If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
    If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
"""
import ast



def parse_input(filename):
    with open(filename) as fp:
        _data = [_.split("\n") for _ in fp.read().split("\n\n")]
    
    data = []
    for _packet_pair in _data:
        packet_pair = []
        for _packet in _packet_pair:
            packet = ast.literal_eval(_packet) # '[1, 2, 3]' -> [1, 2, 3]
            packet_pair.append(packet)
        data.append(packet_pair)
    return data


def in_correct_order(first_packet, second_packet):
    i = 0
    num_checks = min(len(first_packet), len(second_packet))
    for i in range(num_checks - 1):
        left = first_packet[i]
        right = second_packet[i]
        if type(left) == type(right) == int:
            if left < right:
                return True
            elif right < left:
                return False
            else:
                continue
        elif type(left) == type(right) == list:
            if in_correct_order(left, right):
                pass
    return False  


def part_1(data):
    for index, (first_packet, second_packet) in enumerate(data):
        print(in_correct_order(first_packet, second_packet))


if __name__ == "__main__":
    filename = "sample_input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))