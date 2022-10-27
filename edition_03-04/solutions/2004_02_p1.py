# February 2004, Problem 1: Least Number of Bills and Coins
# https://github.com/v1neethnc/dwite-contest-solutions

import sys

with open("../inputs/2004_02_problem1.txt") as file_data:

	# Create list from file
	data = [int(i*100) for i in list(map(float, file_data.read().split('\n')))]
	
	# Finding maximum to build a dynamic programming array
	max_val = max(data)
	
	# Creating array and initializing the base case to 0
	vals = [sys.maxsize for i in range(0, max_val+1)]
	vals[0] = 0
	
	# Array of coins
	coins = [1, 5, 10, 25, 100, 200, 500, 1000, 2000]
	# Iterating through the dynamic programming array
	for i in range(len(vals)):
		# Iterating through the coins
		for j in coins:
			# If the current coin value is lesser than the current value
			if j <= i:
				temp_val = vals[i - j]
				# Check for smaller solution validity
				if temp_val + 1 < vals[i] and temp_val != sys.maxsize:
					vals[i] = temp_val + 1
	
	# Printing the results
	for i in data:
		print(vals[i])
