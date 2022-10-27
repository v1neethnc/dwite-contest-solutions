# February 2004, Problem 3: Multiplying Fractions
# https://github.com/v1neethnc/dwite-contest-solutions


def fraction_simplifier(a: int, b: int) -> list:

	"""
	Function to return a mixed fraction for a given numerator and denominator.

	Parameters:
		a:				(int) numerator
		b:				(int) denominator

	Returns:
		list:			(list) list containing three elements of mixed fraction 
	"""

	nm, dn = a, b
	# Iterate through the factors
	for i in range(2, min(a, b)+1):
		# Simplify as long as the current factor divides both numbers
		while nm % i == dn % i == 0:
			nm = nm // i
			dn = dn // i
	return [nm // dn, nm % dn, dn]

with open("../inputs/2004_02_problem3.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')

	# Iterate through the fractions
	for line in data:
		fractions = line.split('*')
		num, den = 1, 1
		# Create product of numerators and denominators
		for frac in fractions:
			temp = frac.split('/')
			num *= int(temp[0])
			den *= int(temp[1])
		
		# Get the mixed fraction and print the result
		res = fraction_simplifier(num, den)
		if res[0] == 0:
			if res[1] == 0:			
				print('0')
			else:
				print(f"{res[1]}/{res[2]}")
		else:
			print(f"{res[0]} {res[1]}/{res[2]}")
