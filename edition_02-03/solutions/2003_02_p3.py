# February 2003, Problem 3: NICHOLAS LOVES TOBOGGANING
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_02_problem3.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]
	
	# Iterate through the cases
	for case in data:
		flag = True
		d, c, s, f = case[0], case[1], case[2], case[3]
		
		# Update with the first climbed data 
		climbed_dist = c - s
		fatigue_diff = round(c * f / 100, 3) 
		ctr = 1

		# Multiple climbs
		while climbed_dist < d and climbed_dist >= 0:
			ctr += 1
			
			# If fatigue makes climb distance negative
			if c - fatigue_diff < 0:
				climbed_dist -= s
				c = prev_c
				continue
			prev_c = c
			c = round(c - fatigue_diff, 3)
			climbed_dist += c
			
			# Check if reached peak before sliding
			if climbed_dist >= d:
				print(f"SUCCESS ON ATTEMPT {ctr}")
				flag = False
				break

			# Slide down
			climbed_dist -= s
			climbed_dist = round(climbed_dist, 3)
		
		if flag:

			# If climbed in first attempt
			if climbed_dist >= d:
				print(f"SUCCESS ON ATTEMPT {ctr}")
			else:
				print(f"FAILURE ON ATTEMPT {ctr}")
