# February 2003, Problem 4: Estimating Pi
# https://github.com/v1neethnc/dwite-contest-solutions


from math import sqrt

# Function to calculate the GCD
def gcd(a: int, b: int) -> int:

	"""
	Iterative function to calculate the GCD of two numbers

	Parameters:
		a: (int) the larger number
		b: (int) the smaller number
	
	Returns:
		a: (int) the greatest common divisor of (a, b)
	"""

	while b:
		a, b = b, a % b
	return a


with open("../inputs/2003_02_problem4.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# Iterate through the data two lines at a time
	for i in range(0, len(data), 2):

		# Get the list of values
		lst = [int(j) for j in data[i + 1].split(' ')]
		ctr, n_ctr = 0, 0

		# Check GCDs of all possible pairs
		for j in range(0, len(lst) - 1):
			for k in range(j + 1, len(lst)):
				n_ctr += 1
				
				# If the pairs are co-primes 
				if gcd(lst[j], lst[k]) == 1:
					ctr += 1
		
		# Round the results to five digits
		res = round(sqrt(n_ctr * 6 / ctr), 5)
		print(f"{res:.5f}")
