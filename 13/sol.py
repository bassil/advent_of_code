# Chinese remainder theorem algorithm from rosetta code:
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
#

def get_earliest_depart_time(time_stamp, bus_ids):
	bus_ids = [int(_) for _ in bus_ids if _ != 'x']
	earliest_depart_time = time_stamp + max(bus_ids)

	bus_id = 0
	for bus in bus_ids:
		earliest_bus_depart_time = bus * ((time_stamp // bus) + 1)
		if earliest_bus_depart_time < earliest_depart_time:
			earliest_depart_time = earliest_bus_depart_time
			bus_id = bus
	return earliest_depart_time, bus_id

def part_1(time_stamp, earliest_depart_time, bus_id):
	return (earliest_depart_time - time_stamp) * bus_id

def part_2(bus_ids):
	# time_stamp such that:
	#	  if bus_ids[i] != x:
	#	      bus_ids[0] departs at time_stamp
	#	      bus_ids[1] departs at time_stamp + 1
	#	      bus_ids[2] departs at time_stamp + 2
	#	      ...
	n = []
	a = []
	for i, bus in enumerate(bus_ids):
		if bus != 'x':
			n.append(int(bus))
			a.append(int(bus) - i)

	return chinese_remainder(n, a)

def main():
	with open("input.txt") as file:
		file_input = file.read()
		time_stamp = int(file_input.split("\n")[0])
		bus_ids = file_input.split("\n")[1].split(",")

	# earliest_depart_time , bus_id = get_earliest_depart_time(time_stamp, bus_ids)

	# print("Part 1:", part_1(time_stamp, earliest_depart_time , bus_id))



	print("Part 2:", part_2(bus_ids))

if __name__ == '__main__':
	main()