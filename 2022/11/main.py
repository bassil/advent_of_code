"""Day 11: Monkey in the Middle"""
import math


class Monkey:
    def __init__(self, number, items, operation, test, true, false):
        self._number = number
        self._items = items
        self._operation = operation
        self._test = test
        self._true = true
        self._false = false
        self._items_inspected = 0

    def add_item(self, item):
        self._items.append(item)

    def inspect_item(self, lcm=0):
        self._items_inspected += 1
        item = self._items.pop(0)
        operation, value = self._operation
        # convert value to int
        if value == "old":
            value = item
        else:
            value = int(value)
        # perform operation
        if operation == "+":
            worry = item + value
        elif operation == "*":
            worry = item * value
        # reduce worry after careful inspection
        worry = worry % lcm if lcm else worry // 3
        # determine next monkey
        if worry % self._test == 0:
            return worry, self._true
        else:
            return worry, self._false

    def __repr__(self):
        return f"Monkey: {self._number}, {self._items}"


class Monkeys:
    def __init__(self):
        self._monkeys = {}

    def get_items_inspected(self, number=2):
        items_inspected = []
        for monkey in self._monkeys.values():
            items_inspected.append(monkey._items_inspected)
        items_inspected = sorted(items_inspected, reverse=True)[:number]
        result = 1
        for item_inspected in items_inspected:
            result *= item_inspected
        return result

    def parse_monkey_from_definition_and_add_monkey(self, monkey_definition):
        monkey_definition = monkey_definition.split("\n")
        number = monkey_definition[0].split()[-1].split(":")[0]
        items = [int(item) for item in monkey_definition[1].split("Starting items:")[-1].strip().split(", ")]
        operation = monkey_definition[2].split("Operation: new = old ")[-1].split()
        test = int(monkey_definition[3].split("Test: divisible by ")[-1])
        true = monkey_definition[4].split("If true: throw to monkey ")[-1]
        false = monkey_definition[5].split("If false: throw to monkey ")[-1]
        monkey = Monkey(number, items, operation, test, true, false)
        self._monkeys[monkey._number] = monkey
    
    def __repr__(self):
        return str([monkey for monkey in self._monkeys.values()])


def parse_input(filename):
    with open(filename) as fp:
        data = fp.read().split("\n\n")
    return data


def execute(data, rounds=20, reduce_worry=False):
    monkeys = Monkeys()

    for monkey_definition in data:
        monkeys.parse_monkey_from_definition_and_add_monkey(monkey_definition)

    for round in range(rounds):
        lcm = 0
        if reduce_worry:
            integers = [monkey._test for monkey in monkeys._monkeys.values()]
            lcm = math.lcm(*integers)

        for monkey_key in monkeys._monkeys.keys():
            monkey = monkeys._monkeys[monkey_key]
            for _ in range(len(monkey._items)):
                item, next_monkey_key = monkey.inspect_item(lcm=lcm)
                monkeys._monkeys[next_monkey_key].add_item(item)
    return monkeys.get_items_inspected()


def part_1(data):
    return execute(data)


def part_2(data):
    return execute(data, rounds=10000, reduce_worry=True)


if __name__ == "__main__":
    filename = "input.txt"
    data = parse_input(filename)
    print("part 1:", part_1(data))
    print("part 2:", part_2(data))
