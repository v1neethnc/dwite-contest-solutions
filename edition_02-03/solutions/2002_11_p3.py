# November 2002, Problem 3: THE GAME OF LIFE
# https://github.com/v1neethnc/dwite-contest-solutions

from copy import deepcopy

with open("../inputs/2002_11_problem3.txt") as file_data:

	data = file_data.read().split("\n")
	ind = 0
	while ind < len(data):

		# Create the grid and update the index to find the next case
		v1, v2 = map(int, data[ind].split(' '))
		ind = v1+1
		grid = [[j for j in i] for i in data[1:]]
		grid = [['.' for i in range(v2)]] + grid + [['.' for i in range(v2)]]
		grid = [['.'] + i + ['.'] for i in grid]

		# List of directions to check in
		directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
		for i in range(1, 101):

			# Temporary copy to save the new grid
			tmp = deepcopy(grid)
			live_ctr = 0
			for row in range(1, v1 + 1):
				for col in range(1, v2 + 1):
					ctr = 0

					# Calculate the number of live neighbours
					for r, c in directions:
						if grid[row + r][col + c] == 'X':
							ctr += 1

					# Update the temporary grid to save the new grid state
					if grid[row][col] == '.' and ctr == 3:
						tmp[row][col] = 'X'
					elif grid[row][col] == 'X' and (ctr > 3 or ctr < 2):
						tmp[row][col] = '.'
				
				# Calculate the number of live cells
				live_ctr += tmp[row].count('X')
			
			# Update the grid using the temporary copy
			grid = deepcopy(tmp)

			# Print the results for the necessary iterations
			if i in [1, 5, 10, 50, 100]:
				print(live_ctr)