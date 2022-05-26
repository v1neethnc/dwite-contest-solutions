# November 2003, Problem 3: Count Shapes II
# https://github.com/v1neethnc/dwite-contest-solutions



def search(curr: tuple, grid: list, visited: set) -> int:

	"""
	Recursive function that begins search at the (row, col) cell in matrix.

	Parameters:
		curr: 		(tuple) current coordinates
		grid: 		(list[list]) 2D matrix where each cell is a single letter
		visited: 	(set) set of coordinates indicating the characters already checked
	
	Returns:
		visited: 	(set) set of visited nodes where the character is an 'X'
	"""


	# Check for cases where the result is false: 
	# if current coordinates are not in range
	# if the current character is a "."
	# if the character is already visited
	if curr[0] not in range(0, len(grid)) or curr[1] not in range(0, len(grid[0])) or grid[curr[0]][curr[1]] == "." or curr in visited:
		return set()
	
	# Add the coordinates to the list of visited elements
	visited.add(curr)

	# Arbitary path length value
	res = -1

	# Check all four directions
	directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	for j in directions:

		# Get the list of visited nodes and updated visited if a larger path is found
		tmp = search((curr[0] + j[0], curr[1] + j[1]), grid, visited)
		if len(tmp) < res:
			res = len(tmp)
			visited = tmp

	# Return the set of visited nodes
	return visited


with open("2003_11_problem3.txt") as file_data:

	# Create list from file and initialize the index to read from data
	data = file_data.read().split('\n')
	ind = 0

	while ind < len(data):

		# Read the number of columns and rows and the grid
		cols = int(data[ind])
		rows = int(data[ind + 1])
		grid = data[ind + 2: ind + rows + 2]

		# Initialize an empty set, counter of sets, and max and min lengths
		visited = set()
		ctr = 0
		max_len, min_len = -1, rows * cols

		# Iterate through the grid to start searching
		for row in range(rows):
			for col in range(cols):

				# If a node is already visited then there's no need to visit it again
				if grid[row][col] == 'X' and (row, col) not in visited:
					tmp_visited = search((row, col), grid, set())

					# Update the maximum and minimum path lengths
					max_len = max(max_len, len(tmp_visited))
					min_len = min(min_len, len(tmp_visited))
					for i in tmp_visited:
						visited.add(i)
					ctr += 1
					
		ind += rows + 2
		print(ctr, max_len, min_len)
