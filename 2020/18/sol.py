import string
def binary_operation(operator, A, B):
	if operator == "*":
		return A * B
	elif operator == "+":
		return A + B

def evaluate_expression(expression):

	expression = expression.replace(" ", "")
	values = []
	operators = []

	for char in expression:

		if char in string.digits:
			values.append(int(char))
		elif char in "+*":
			operators.append(char)
		elif char == "(":
			operators.append(char)
		elif char == ")":
			_operators = []
			_values = []
			operator = operators.pop()

			while operator != "(":
				_values.append(values.pop())
				_operators.append(operator)
				operator = operators.pop()
		
			_values.append(values.pop())

			while len(_operators) > 0:
				operator = _operators.pop()
				A = _values.pop()
				B = _values.pop()
				_values.append(binary_operation(operator, A, B))

			values.append(_values[0])
	_operators = []
	_values = []
	for value in values:
		_values.insert(0, value)

	for operator in operators:
		_operators.insert(0, operator)

	while len(_operators) > 0:
		operator = _operators.pop()
		A = _values.pop()
		B = _values.pop()
		_values.append(binary_operation(operator, A, B))
	return _values[0]

def part_1(expressions):
	results = []
	for expression in expressions:
		result = evaluate_expression(expression)
		results.append(result)
	return results

def operator_precedence(operator):
	if operator == "*":
		return 1
	elif operator == "+":
		return 2
	elif operator == "(" or operator == ")":
		return 0

def evaluate_expression_with_precedence(expression):
	expression = expression.replace(" ", "")
	values = []
	operators = []

	for char in expression:

		if char in string.digits:
			values.append(int(char))
		elif char == "(":
			operators.append(char)
		elif char == ")":
			while len(operators) != 0 and operators[-1] != "(":
				A = values.pop()
				B = values.pop()
				operator = operators.pop()
				values.append(binary_operation(operator, A, B))
			operators.pop()
		else:
			while len(operators) != 0 and \
				operator_precedence(operators[-1]) >= operator_precedence(char):

				A = values.pop()
				B = values.pop()
				operator = operators.pop()
				values.append(binary_operation(operator, A, B))

			operators.append(char)
	
	# reconstruct expression
	expression = [values[0]]

	for i, operator in enumerate(operators):
		expression.append(operator)
		expression.append(values[i+1])

	# evaluate expression
	_values = []
	_operators = []
	for char in reversed(expression):
		if type(char) == int:
			_values.append(char)
		else:
			while len(_operators) != 0 and \
				operator_precedence(_operators[-1]) >= operator_precedence(char):

				A = _values.pop()
				B = _values.pop()
				operator = _operators.pop()
				_values.append(binary_operation(operator, A, B))
			
			_operators.append(char)
	return binary_operation(_operators[0], _values[0], _values[1])


def part_2(expressions):
	results = []
	for expression in expressions:
		result = evaluate_expression_with_precedence(expression)
		results.append(result)
	return results

def main():
	with open("input.txt") as f:
		expressions = f.read().split("\n")
	
	print("Part 1:", sum(part_1(expressions)))
	print("Part 2:", sum(part_2(expressions)))
if __name__ == '__main__':
	main()