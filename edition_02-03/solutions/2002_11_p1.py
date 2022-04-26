# November 2002, Problem 1: SALES! SALES! SALES!
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_11_problem1.txt") as file_data:

	# Create the pairs of actual price and selling proce
	data = file_data.read().split("\n")
	pairs = [[float(data[i]), float(data[i+1])] for i in range(0, len(data), 2)]

	for i in range(len(pairs)+1):
		if i % 3 == 0:
			# Print the previous case's result when a new case is encountered
			if i != 0:
				res = "{0:.3f}".format(res)
				print(f"{res:>7}")
			res = 0
		else: 
			# Update the result by calculating the discount rate and comparing with existing results
			res = round(max(res, (pairs[i][0] - pairs[i][1])*100/pairs[i][0]), 3)
