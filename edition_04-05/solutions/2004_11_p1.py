# November 2004, Problem 1: Credit Card Check Digit
# https://github.com/v1neethnc/dwite-contest-solutions


def digit_sum(n: int) -> int:

	"""
	Returns sum of digits of number.

	Parameters:
		n: 		(int) number to calculate sum of digits of
	
	Returns:
		num: 	(int) sum of digits
	"""

	return sum([int(i) for i in str(n)])


with open("../inputs/2004_11_problem1.txt") as file_data:

	# Create list from file
	dt = file_data.read().split('\n')

	# Iterate through input
	for number in dt:

		# Store check, calculate alternate digit sums, final sum
		check = int(number[-1])
		alt_digits = [digit_sum(int(i)*2) for i in number[-2::-2]]
		sum_val = sum([int(i) for i in number[-1::-2]]) + sum(alt_digits)

		# Check validity
		if sum_val % 10 == 0:
			print("VALID")
		else:
			new_check = abs(check - sum_val % 10)
			print(f"INVALID {new_check}")
