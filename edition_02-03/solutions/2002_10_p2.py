# October 2002, Problem 2: INVESTMENT CALCULATOR
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_10_problem2.txt") as file_data:

	# Creating the lists of amounts, rates, and invested times
	data = file_data.read().split("\n")
	amounts = [float(data[i]) for i in range(len(data)) if i % 3 == 0]
	rates = [float(data[i]) for i in range(len(data)) if i % 3 == 1]
	times = [int(data[i]) for i in range(len(data)) if i % 3 == 2]

	for i in range(len(amounts)):
		final_amt = 0
		
		# Interest compounding per month
		for j in range(0, times[i]*12):
			final_amt += amounts[i]
			final_amt = round(final_amt * (1 + rates[i]/1200), 2)

		# Printing the result
		print(final_amt)
