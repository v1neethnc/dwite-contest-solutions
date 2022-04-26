# January 2003, Problem 2: SIN Check Digit
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_01_problem2.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [i for i in file_data.read().split("\n")]

	# Go through different cases
	for ssn in data:

		# Get the check sum
		check = int(ssn[8])

		# Calculate the odd and even position sums
		odd_sum = sum([int(i) for i in ssn[:8:2]])
		even_sum = 0
		for i in ssn[1:8:2]:
			val = int(i) * 2
			even_sum += sum([int(i) for i in str(val)])
		total_sum = even_sum + odd_sum

		# Calculate the actual check value
		calc_check = ((total_sum // 10 + 1) * 10) - total_sum
		if calc_check == check:
			print("VALID")
		else:
			print(f"INVALID-{calc_check}")
