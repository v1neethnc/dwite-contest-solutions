# October 2004, Problem 2: 24 Hour Clock
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_10_problem2.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')

	# Iterate through the timestamps
	for timestamp in data:
		
		# Get the hour and minute
		times = list(map(int, timestamp.split(':')))
		
		# Set the suffix
		res = ' AM' if times[0] < 12 else ' PM'
		times[0] = times[0] % 12
		
		# Calcualte and pring the result timestamp
		res = str(times[0]) + ':' + str(times[1]).zfill(2) + res
		print(res)
