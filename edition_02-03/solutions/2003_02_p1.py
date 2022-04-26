# February 2003, Problem 1: LOGO
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_02_problem1.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# Get the upper right coordinates and create a map of direction changes
	upper_coords = tuple(int(i) for i in data[0].split(' '))
	dir_change = {'N': ['W', 'E'], 'S': ['E', 'W'], 'W': ['S', 'N'], 'E': ['N', 'S']}

	# Iterate through the cases
	for i in range(1, len(data)):
		
		# Check if a new case is encountered
		if i % 2 == 1:

			# Get the new starting coordinates and current facing directions
			vals = data[i].split(' ')
			curr_coords = [int(i) for i in vals[:2]]
			curr_dir = vals[2]

		# If new starting coordinates are already read
		else:
			flag = True

			# Iterate through list of operations
			for j in data[i]:
				prev_coords = [i for i in curr_coords]

				# Move the turtle and update the coordinates
				if j == 'F':
					if curr_dir == 'N':
						curr_coords[1] += 1
					elif curr_dir == 'S':
						curr_coords[1] -= 1
					elif curr_dir == 'W':
						curr_coords[0] -= 1
					elif curr_dir == 'E':
						curr_coords[0] += 1

				# Turn the turtle
				else:
					new_dir_index = 0 if j == 'L' else 1
					curr_dir = dir_change[curr_dir][new_dir_index]
				
				# Check if the turtle is still on the plane or not
				if curr_coords[0] > upper_coords[0] or curr_coords[1] > upper_coords[1]:
					print(prev_coords[0], prev_coords[1], curr_dir, "LOST")
					flag = False
					break
			
			# If the turtle is still on the plane
			if flag:
				print(curr_coords[0], curr_coords[1], curr_dir)
