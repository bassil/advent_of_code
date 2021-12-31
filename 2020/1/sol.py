def fix_expense_report(expense_report):
	expense_report_set = set(expense_report)
	product_of_three_entries = 0
	for expense_1 in expense_report_set:
		for expense_2 in expense_report_set:
			if expense_2 != expense_1:
				if (2020 - (expense_1 + expense_2)) in expense_report_set:
					product_of_three_entries = \
						(2020 - (expense_1 + expense_2)) * expense_1 * expense_2
					print(expense_1, expense_2, (2020 - (expense_1 + expense_2)))
					break
			
			
	return product_of_three_entries

if __name__ == "__main__":

	expense_report = []

	with open("./input1.txt") as file:

		for line in file:
			expense_report.append(int(line))

	print(fix_expense_report(expense_report))