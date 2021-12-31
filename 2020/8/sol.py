import copy

# input text file is boot code with one instruction per line

with open('input.txt') as f:
	instructions = [_.split(' ') for _ in f.read().split('\n')]


# Part 1 - Find infinite loop in boot code, 
# return value of accumulator before second iteration of infinite loop

# This is equivalent to recording the index of each operation. 
# If the operation has been executed before, return value of accumulator

def part_1(instructions, current_instruction_index, indices_of_executed_instructions, accumulator=0):
	
	if current_instruction_index == 633:
		print("Part 2 - Accumulator", accumulator)

	elif current_instruction_index not in indices_of_executed_instructions:
		
		indices_of_executed_instructions.add(current_instruction_index)

		next_instruction_index = 0

		# execute current instruction
		operation, argument = instructions[current_instruction_index]
		if operation == "acc":
			accumulator += int(argument)

			# What happens when index out of bounds?
			next_instruction_index = current_instruction_index + 1
			
		elif operation == "jmp":
			# what happens when index out of bounds?
			next_instruction_index = current_instruction_index + int(argument)

		else:
			next_instruction_index = current_instruction_index + 1
	
		part_1(instructions, next_instruction_index, indices_of_executed_instructions, accumulator)
	
	else:
		
		# print("Part 1 - Accumulator:", accumulator)
		return 

def part_2(instructions):
	# idea - change one instruction (jmp -> nop or nop -> jmp)
	# 	   - see if the program terminates
	#	   - if it terminates, return Accumulator value for that instruction change
	for instruction_index, instruction in enumerate(instructions):
		if len(instruction) > 1:
			operation, argument = instruction
			
			# deep copy of instructions for changing one instruction
			instructions_copy = copy.deepcopy(instructions)

			indices_of_executed_instructions = set()
			if operation == 'jmp':
				instructions_copy[instruction_index][0] = 'nop'
				part_1(instructions_copy, 0, indices_of_executed_instructions)

			elif operation == 'nop':
				instructions_copy[instruction_index][0] = 'jmp'
				part_1(instructions_copy, 0, indices_of_executed_instructions)


		else: 
			print("boot program terminated as we wanted")

indices_of_executed_instructions = set()

# part_1(instructions, 0, indices_of_executed_instructions)
print(part_2(instructions))

