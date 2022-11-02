# October 2004, Problem 4: CD-ROM Files
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2004_10_problem4.txt") as file_data:

	# Create list from file
	dt = file_data.read().split('\n')
	
	# Iterate through the cases and create the list of elements
	for line in dt:
		vals = list(map(int, line.split(' ')))
		flags = [False for i in range(vals[0] + 1)]
		flags[0] = True
		
		# Create sorted list of CDs within range
		temp_vals = [i for i in vals[2:] if i < vals[0]]
		temp_vals.sort()
		
		# Iterate through the CDs
		for i in temp_vals:
			exclude = []
			
			# If another CD with same capacity doesn't exist
			if not flags[i]:
				flags[i] = True
				exclude = [i]
		
			# List of possible sums so far
			indices = [ind for ind, val in enumerate(flags) if val]

			# Set flags to true for all possible sums so far
			for j in indices:
				if flags[j] and i+j < len(flags) and j not in exclude:
					flags[i+j] = True

		# Print max value as result
		res = max([ind for ind, val in enumerate(flags) if val])
		print(res)
