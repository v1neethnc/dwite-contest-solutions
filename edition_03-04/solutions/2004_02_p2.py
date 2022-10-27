# February 2004, Problem 2: Number of Combinations of Bills and Coins
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_02_problem2.txt") as file_data:

	# Create list from file
	data = [int(i*100) for i in list(map(float, file_data.read().split('\n')))]
	
	# Finding maximum to build a dynamic programming array
	max_val = max(data)
	
	# Creating array and initializing the base case to 0
	vals = [0 for i in range(0, max_val+1)]
	vals[0] = 1
	
	# Array of coins
	coins = [1, 5, 10, 25, 100, 200, 500, 1000, 2000]
	# Iterating through the dynamic programming array
	for coin in coins:
		# Build solution bottom-up
		for i in range(coin, len(vals)):
			vals[i] += vals[i - coin]
	
	# Printing the results
	for i in data:
		print(vals[i])
