# October 2002, Problem 3: SIMPLE ARITHMETIC?
# https://github.com/v1neethnc/dwite-contest-solutions


import operator as op

with open("../inputs/2002_10_problem3.txt") as file_data:

	# Reading the data and creating an operator map
	data = file_data.read().split("\n")
	op_map = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

	for val in data:
		found_operator = False
		v1, v2, opr = '', '', ''
		for i in val:
			# Update the first operand if the operator is not found
			if not found_operator:
				if i in "+-*/":
					opr = i
					found_operator = True
					continue
				v1 += i
			# Update the second operand if the operator is found
			else:
				v2 += i
				
		# Use the map to calculate the result and print it
		print(op_map[opr](float(v1), float(v2)))
