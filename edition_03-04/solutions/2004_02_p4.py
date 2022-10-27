# February 2004, Problem 4: Simple Transposition Cipher
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_02_problem4.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')

	# Iterate through the encrypted texts
	for line in data:
		
		# Dictionary defining the factors
		factor_dict = {'TWO': 2, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'NINE': 9, 'TEN': 10}
		res = ''

		# Reading the last three and four characters
		v1, v2 = line[-3:], line[-4:]
		v1, v2 = v1[::-1], v2[::-1]
		
		# Alloting the factor and trimming the line accordingly
		if v1 in factor_dict.keys():
			factor = factor_dict[v1]
			ln = line[:-3]
		else:
			factor = factor_dict[v2]
			ln = line[:-4]
		
		# Number of rows in the grid
		row_lim = len(ln) // factor if len(ln) % factor == 0 else len(ln) // factor + 1
		
		# Getting the indices in each row and building the result
		for row in range(row_lim):
			indices = [row + i*row_lim for i in range(factor)]
			res += ''.join([ln[ind] for ind in indices if ind < len(ln)])

		print(res)
