# October 2004, Problem 5: Super Long Sums
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2004_10_problem5.txt") as file_data:

	# Create list from file
	dt = list(map(int, file_data.read().split('\n')))

	# Iterate through pairs and calculate sum
	for ind in range(0, len(dt), 2):
		print(dt[ind] + dt[ind+1])
