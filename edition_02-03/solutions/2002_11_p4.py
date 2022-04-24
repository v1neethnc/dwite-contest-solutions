# November 2002, Problem 4: MONEY PRIZE
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_11_problem4.txt") as file_data:

	# Read the data and create the grid
	data = file_data.read().split("\n")
	grid = [[int(j) for j in i.split(' ')] for i in data]

	# The final grid consists of the top 5 costs to reach each element
	# Calculate the vertical and horizontal costs from the start element
	final = [[[sum(grid[len(grid)-1][:i])] for i in range(1, len(grid[0])+1)]]
	prev = final[0][0][0]
	for i in range(len(grid[0])-2, -1, -1):
		final = [[[prev + grid[i][0]]]] + final
		prev = prev + grid[i][0]

	# Calculate the costs at each step
	for row in range(len(grid)-2, -1, -1):
		for col in range(1, len(grid[0])):
			new_val = []

			# Add the cell value to the path costs and update the array of costs
			for i in [final[row+1][col], final[row][col-1]]:
				tmp = [x + grid[row][col] for x in i]
				new_val.extend(tmp)
			new_val.sort()
			
			# Save the top five costs
			final[row].append(new_val[-5:])
	
	# Sort and print the cost list at the destination 
	final[0][7].sort()
	for i in final[0][7][::-1]:
		print(i)