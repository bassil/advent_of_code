"""Day 9: Rope Bridge"""

class Knot:
	def __init__(self):
		self._x = 0
		self._y = 0

	@property
	def x(self) -> int:
		return self._x

	@property
	def y(self) -> int:
		return self._y

	def __add__(self, coords: list[int, int]) -> None:
		"""
		coords: [int, int]
		"""
		self._x = self.x + coords[0]
		self._y = self.y + coords[1]

	def __repr__(self) -> str:
		return f"Knot: x: {self.x}, y: {self.y}"


class Rope:
	def __init__(self, num_knots: int = 2):
		self._num_knots = num_knots
		self._knots = [Knot() for knot in range(self._num_knots)]
		self._direction_map = {
			"R": [1, 0],
			"L": [-1, 0],
			"U": [0, 1],
			"D": [0, -1]
		}
		self._tail_move_map = {
			(2, 0)	: [-1, 0],
			(-2, 0)	: [1, 0],
			(0, 2)	: [0, -1],
			(0, -2)	: [0, 1],
			(2, 1)	: [-1, -1],
			(2, -1) : [-1, 1], 
			(-2, 1) : [1, -1],
			(-2, -1): [1, 1],
			(1, 2)  : [-1, -1],
			(1, -2) : [-1, 1],
			(-1, 2) : [1, -1],
			(-1, -2): [1, 1],
			(2, 2)	: [-1, -1],
			(2, -2) : [-1, 1],
			(-2, 2) : [1, -1],
			(-2, -2): [1, 1]
		}
		self._tail_positions = set()

	@property
	def head(self) -> Knot:
		return self._knots[0]
	
	@head.setter
	def head(self, coords: list[int, int]) -> None:
		self._knots[0] = coords

	@property
	def tail(self) -> Knot:
		return self._knots[self._num_knots - 1]

	@tail.setter
	def tail(self, coords: list[int, int]) -> None:
		self._knots[len(self._num_knots) - 1] = coords

	@property
	def tail_position(self) -> tuple[int, int]:
		return (self.tail.x, self.tail.y)

	@property
	def num_tail_positions(self) -> int:
		return len(self._tail_positions)

	def move(self, direction: str) -> None:
		for i in range(self._num_knots):
			if i == 0:
				self._knots[i] + self._direction_map[direction]
			else:
				dx = self._knots[i].x - self._knots[i - 1].x
				dy = self._knots[i].y - self._knots[i - 1].y
				if abs(dx) > 1 or abs(dy) > 1:
					self._knots[i] + self._tail_move_map[(dx, dy)]


		self._tail_positions.add(self.tail_position)

	def execute(self, instruction: int) -> None:
		direction, steps = instruction
		for step in range(steps):
			self.move(direction)

	def __repr__(self) -> str:
		return f"Rope: (Head: {self.head}, Tail: {self.tail})"


def parse_input(filename: str) -> list[list[str, int]]:
	with open(filename) as fp:
		data = [[_[0], int(_[1])] for _ in [line.split() for line in fp.read().split("\n")]]
	return data


def part_1(data):
	rope = Rope()
	for instruction in data:
		rope.execute(instruction)
	return rope.num_tail_positions

def part_2(data):
	rope = Rope(num_knots=10)
	for instruction in data:
		rope.execute(instruction)
	return rope.num_tail_positions

if __name__ == '__main__':
	filename = "input.txt"
	data = parse_input(filename)
	print("part 1:", part_1(data))
	print("part 2:", part_2(data))