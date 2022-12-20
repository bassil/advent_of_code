"""Day 13: Distress Signal"""

from functools import cmp_to_key

def parse_input(filename):
    with open(filename) as fp:
        _data = [_.split("\n") for _ in fp.read().split("\n\n")]
    
    data = []
    for _packet_pair in _data:
        packet_pair = []
        for _packet in _packet_pair:
            packet = eval(_packet) # '[1, 2, 3]' -> [1, 2, 3]
            packet_pair.append(packet)
        data.append(packet_pair)
    return data


def in_correct_order(first_packet, second_packet):
    if isinstance(first_packet, list) and isinstance(second_packet, int):
        second_packet = [second_packet]
    
    if isinstance(first_packet, int) and isinstance(second_packet, list):
        first_packet = [first_packet]

    if isinstance(first_packet, int) and isinstance(second_packet, int):
        if first_packet < second_packet:
            return 1
        elif first_packet > second_packet:
            return -1
        else:
            return 0
    
    if isinstance(first_packet, list) and isinstance(second_packet, list):
        num_checks = min(len(first_packet), len(second_packet))
        for i in range(num_checks):
            order = in_correct_order(first_packet[i], second_packet[i])
            if order == 1:
                return 1
            elif order == -1:
                return -1
        
        # reached the end of one of the packet lists!
        # need to check which one is longer
        if num_checks == len(first_packet):
            if len(first_packet) == len(second_packet):
                return 0
            return 1
       
        if num_checks == len(second_packet):
            return -1


def part_1(data):
    ret = 0
    for index, (first_packet, second_packet) in enumerate(data):
        if in_correct_order(first_packet, second_packet) == 1:
            ret += index + 1
    return ret

def part_2(data):
    packets = [[2], [6]]
    for packet_pair in data:
        for packet in packet_pair:
            packets.append(packet)
    packets.sort(key=cmp_to_key(in_correct_order), reverse=True)
    decoder_key = 1
    for i, packet in enumerate(packets):
        if packet in [[2], [6]]:
            decoder_key *= i + 1
    
    return decoder_key


if __name__ == "__main__":
    filename = "input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))
    print("part 2:", part_2(data))