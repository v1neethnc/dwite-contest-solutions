# January 2004, Problem 4: Shortest Time in the Maze
# https://github.com/v1neethnc/dwite-contest-solutions


import math

def search(curr: tuple, dest: tuple, grid: list, visited: set) -> set:

	"""
	Recursive function that takes a current and destination node and finds a path.

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

	# Exit if the node is visited or if the current node is outside the grid or if the current element is 0
	if curr[0] not in range(0, len(grid)) or curr[1] not in range(0, len(grid[0])) or curr in visited or grid[curr[0]][curr[1]] == 0:
		return set()

	# Update visited and set result variables
	visited.add(curr)
	res_val, res_set = math.inf, set()

	# Go through four directions
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	for dir in directions:
		tmp_res = search((curr[0] + dir[0], curr[1] + dir[1]), dest, grid, visited)
		val = sum([grid[i[0]][i[1]] for i in tmp_res])
		# Check if the path is extensive and the cost of the path
		if val < res_val and len(tmp_res) > 0:
			res_val = val
			res_set = set([i for i in tmp_res])

	visited.remove(curr)
	return res_set


with open("../inputs/2004_01_problem4.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	ind = 0
	while ind < len(data):
		# Read the grid sizes and use that to read the grid
		r, c = map(int, data[ind].split(' '))
		grid = [list(map(int, data[i].split(' '))) for i in range(ind + 1, ind + r + 1)]

		# 0-index the start and end coordinates
		start = tuple(map(int, data[ind + r + 1].split(' ')))
		end = tuple(map(int, data[ind + r + 2].split(' ')))
		start = (start[0] - 1, start[1] - 1)
		end = (end[0] - 1, end[1] - 1)
		ind = ind + r + 3
		
		# Find a path and display the data as required
		res = search(start, end, grid, set())
		seconds = sum([grid[i[0]][i[1]] for i in res])
		hour, minute, second = seconds // 3600, (seconds % 3600) // 60, (seconds % 3600) % 60
		final_ans = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
		print(final_ans)
