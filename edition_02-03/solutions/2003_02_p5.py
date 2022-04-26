# February 2003, Problem 5: BASE CONVERTER
# https://github.com/v1neethnc/dwite-contest-solutions


# Convert any number in base 2-16 to base 10
def get_base10_val(num: str, base: int) -> int:

	"""
	Function to take a number in a given base in the range [2, 16] and convert to decimal

	Parameters:
		num: (str) the number string in the given base
		base: (int) the base of the given number
	
	Returns:
		res: (int) decimal value of the given number in the given base
	"""

	vals = '0123456789ABCDEF'
	res, exp = 0, 0

	# Iterate from right to left and calculate decimal value
	for i in num[::-1]:
		res += (base ** exp) * vals.find(i) 
		exp += 1
	return res


# Convert decimal number to any base between 2-16
def convert_base10_val(num: int, base: int) -> str:

	"""
	Function to take a decimal number and convert to the given base in the range [2, 16]

	Parameters:
		num: (int) the decimal number
		base: (int) the base to convert to
	
	Returns:
		res: (str) the number in the target base
	"""

	res = ''
	vals = '0123456789ABCDEF'
	while num > 0:
		res = vals[num % base] + res
		num = num // base
	return res


with open("../inputs/2003_02_problem5.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# Iterate through the cases
	for i in data:
		vals = i.split(' ')
		v1 = get_base10_val(vals[0], int(vals[1]))
		res = convert_base10_val(v1, int(vals[2]))
		print(res)
