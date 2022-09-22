# December 2003, Problem 3: Money Prize II
# https://github.com/v1neethnc/dwite-contest-solutions


def search(curr: tuple, dest: tuple, grid: list, visited: set) -> set:

	"""
	Recursive function that takes a word and begins search at the (row, col) cell in matrix.

	Parameters:
		curr: 		(tuple) current coordinates
		dest: 		(tuple) destination coordinates
		grid: 		(list[list]) 2D matrix where each cell is a single letter
		visited: 	(set) set of coordinates indicating the characters already checked
	
	Returns:
		res_set: 	(set) return the nodes in the optimal path
	"""

	# Exit if the destination is reached
	if curr == dest:
		visited.add(dest)
		return visited
	
	# Exit if the node is visited or if the current node is outside the grid
	if curr[0] not in range(0, len(grid)) or curr[1] not in range(0, len(grid)) or curr in visited:
		return []
	
	# Update visited and set result variables
	visited.add(curr)
	res_val, res_set = 0, set()

	# Traverse the grid by either going right or up
	directions = [[0, 1], [-1, 0]]
	for dir in directions:
		tmp_res = search((curr[0] + dir[0], curr[1] + dir[1]), dest, grid, visited)
		val = sum([grid[i[0]][i[1]] for i in tmp_res])

		# Check if the path is extensive and the cost of the path
		if val > res_val and len(tmp_res) == len(grid) * 2 - 1:
			res_val = val
			res_set = set([i for i in tmp_res])

	visited.remove(curr)
	return res_set


with open("2003_12_problem3.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	ind = 0
	while ind < len(data):
		val = int(data[ind])
		sm = 0
		grid = [list(map(int, i.split(' '))) for i in data[ind + 1: ind + val + 1]]
		for iter in range(0, 2):
			pass_grid = search((val - 1, 0), (0, val - 1), grid, set())
			sm += sum([grid[i[0]][i[1]] for i in pass_grid])
			for i in pass_grid:
				grid[i[0]][i[1]] = 0
		print(sm)
		ind += val + 1
