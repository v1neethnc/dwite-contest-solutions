# October 2003, Problem 5: The Maze
# https://github.com/v1neethnc/dwite-contest-solutions


def search(curr: tuple, dest: tuple, grid: list, visited: list) -> int:

	"""
	Recursive function that takes a word and begins search at the (row, col) cell in matrix.

	Parameters:
		curr: 		(tuple) current coordinates
		dest: 		(tuple) destination coordinates
		grid: 		(list[list]) 2D matrix where each cell is a single letter
		visited: 	(set) set of coordinates indicating the characters already checked
	
	Returns:
		res: 		(int) shortest path length
	"""

	# Exit if the destination is reached
	if curr == dest:
		return len(visited) - 1

	# Check for cases where the result is false: 
	# if current coordinates are not in range
	# if the current character is a "#"
	# if the character is already visited
	if curr[0] not in range(0, len(grid)) or curr[1] not in range(0, len(grid[0])) or grid[curr[0]][curr[1]] == "#" or curr in visited:
		return -1
	
	# Add the coordinates to the list of visited elements
	visited.append(curr)

	# Arbitary path length value
	res = 2500

	# Check all four directions
	directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	for j in directions:
		tmp = search((curr[0] + j[0], curr[1] + j[1]), dest, grid, visited)

		# If a path is possible, then update the minimum distance
		if tmp != -1:
			res = min(res, tmp)

	# Clear the visited nodes
	visited.remove(curr)
	return res


with open("../inputs/2003_10_problem5.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")
	ind = 0

	# Iterate through the cases
	while ind < len(data):

		# Get the values and create the grid
		lines, length = map(int, data[ind].strip().split(' '))
		matrix = [[j for j in i] for i in data[ind+1:ind+lines+1]]

		# Iterate through the matrix to find the starting and ending coordinates
		for i in range(len(matrix)):
			if 'A' in matrix[i]:
				start_coords = tuple([i, matrix[i].index('A')])
			if 'B' in matrix[i]:
				end_coords = tuple([i, matrix[i].index('B')])

		# Search for shortest path from start to end
		path_len = search(start_coords, end_coords, matrix, [])
		print(path_len)

		# Update the index to get to the next case
		ind += lines + 1
