# January 2004, Problem 2: Digital Clocks
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_01_problem2.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	configs = {"0": "1110111", "1": "0010010", "2": "1011101", "3": "1011011", "4": "0111010", "5": "1101011", "6": "1101111", "7": "1010010", "8": "1111111", "9": "1111011"}
	# Iterate through the cases
	for line in data:
		start, end = line.split(' ')
		on_ctr, off_ctr = 0, 0
		temp = [i.zfill(2) for i in start.split(':')]
		# Get the clock configuration
		if temp[0][0] == '0':
			start_config = ["0000000", configs[temp[0][1]], configs[temp[1][0]], configs[temp[1][1]]]
		else:
			start_config = [configs[temp[0][0]], configs[temp[0][1]], configs[temp[1][0]], configs[temp[1][1]]]
		# Iterate through to the end
		while start != end:
			# Go ahead one minute
			hour, minu = map(int, start.split(":"))
			minu = (minu + 1) % 60
			if minu == 0:
				hour = ((hour + 1) % 12 )
				if hour == 0:
					hour = 12
			# Get the current configuration
			start = [str(hour).zfill(2), str(minu).zfill(2)]
			if start[0][0] == '0':
				curr_config = ["0000000", configs[start[0][1]], configs[start[1][0]], configs[start[1][1]]]
			else:
				curr_config = [configs[start[0][0]], configs[start[0][1]], configs[start[1][0]], configs[start[1][1]]]
			# Iterate through the configurations
			on_c, off_c = 0, 0
			for ind in range(4):
				val1, val2 = start_config[ind], curr_config[ind]
				# Iterate through each configuration to update counters
				for i in range(7):
					if int(val1[i]) - int(val2[i]) == 1:
						off_c += 1
					elif int(val1[i]) - int(val2[i]) == -1:
						on_c += 1
			on_ctr += on_c
			off_ctr += off_c
			start = str(int(start[0])) + ":" + start[1]
			start_config = [i for i in curr_config]
		# Print the result
		print(on_ctr, off_ctr)
