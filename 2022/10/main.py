"""Day 10: Cathode-Ray Tube"""


def parse_input(filename):
    with open(filename) as fp:
        data = fp.read().split("\n")
    return data


class CPU:
    def __init__(self):
        self._current_cycle = 0
        self._register = 1
        self._signal_strength = {0: {"cycle": 0, "instruction": None, "register": 1}}
        self._command_map = {"noop": self.noop, "addx": self.addx}

    @property
    def current_cycle(self):
        return self._current_cycle

    @property
    def register(self):
        return self._register 

    def signal_strength(self, cycle=None):
        if cycle:
                # the signal strength is that of the previously computed cycle
                previous_cycle = 0
                for possible_previous_cycle in self._signal_strength.keys():
                    if possible_previous_cycle >= cycle:
                        break
                    previous_cycle = possible_previous_cycle
                return self._signal_strength[previous_cycle]["register"]
        return self._signal_strength

    def noop(self):
        self._current_cycle += 1
    
    def addx(self, value):
        self._current_cycle += 2
        self._register += value
    
    def execute(self, instruction):
        parsed_instruction = instruction.split()
        if len(parsed_instruction) == 1:
            self._command_map[parsed_instruction[0]]()
        else:
            self._command_map[parsed_instruction[0]](int(parsed_instruction[1]))

        # update signal strength
        self._signal_strength[self._current_cycle] = {"cycle": self._current_cycle, "register": self.register, "instruction": instruction}


def part_1(data):
    cpu = CPU()
    for instruction in data:
        cpu.execute(instruction)
    cycles = [20, 60, 100, 140, 180, 220]
    return sum([cpu.signal_strength(cycle=cycle) * cycle for cycle in cycles])

def part_2(data, height=6, width=40):
    cpu = CPU()
    for instruction in data:
        cpu.execute(instruction)

    CRT = [[" "] * width for i in range(height)]

    for cycle in range(1, (height * width) + 1):
        register = cpu.signal_strength(cycle=cycle)
        sprite = [register - 1, register, register + 1]
        pixel = cycle - 1
        row = pixel // width
        column = pixel % width
        if column in sprite:
            CRT[row][column]= "#"

    return "\n".join(["".join(row) for row in CRT])


if __name__ == "__main__":
    # filename = "sample_input.txt"
    filename = "input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))
    print("part 2:") 
    print(part_2(data))