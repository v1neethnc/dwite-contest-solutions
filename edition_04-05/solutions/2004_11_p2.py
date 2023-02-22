# November 2004, Problem 2: Squareland
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2004_11_problem2.txt") as file_data:

	# Create list from file
	dt = list(map(int, file_data.read().split('\n')))
	
	# Iterate through pairs
	for ind in range(0, len(dt), 2):

		# The result is given by (large side - small side + 1)^2
		res = (int(dt[ind]**0.5) - int(dt[ind+1]**0.5) + 1)**2
		print(res)
