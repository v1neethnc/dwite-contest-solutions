# October 2002, Problem 4: WORD SEARCH
# https://github.com/v1neethnc/dwite-contest-solutions


def search(word: str, ind: int, row: int, col: int, mat: list, visited: set) -> bool:

	"""
	Recursive function that takes a word and begins search at the (row, col) cell in matrix.

	Parameters:
		word: 		(string) the word to search for
		ind: 		(int) the index of the letter currently searched
		row: 		(int) the current row number
		col: 		(int) the current column number
		mat: 		(list[list]) 2D matrix where each cell is a single letter
		visited: 	(set) set of coordinates indicating the characters already checked
	
	Returns:
		tmp: (boolean) True if the word exists, False otherwise
	"""

	# Exit if the function has exhausted all the letters in the word
	if ind == len(word):
		return True

	# Check for cases where the result is false: 
	# if the (row, col) are not in range
	# if the letter in grid does not match the required letter
	# if the letter is already visited
	if row not in range(0, len(mat)) or col not in range(0, len(mat[0])) or word[ind] != mat[row][col] or (row, col) in visited:
		return False
	
	# Add the coordinates to the list of visited elements
	visited.add((row, col))

	# Boolean variable to see if the next letter is among the unvisited neighbors
	tmp = False

	# Check all eight directions
	directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [-1, -1], [1, 1]]
	for j in directions:
		tmp = tmp or search(word, ind+1, row + j[0], col + j[1], matrix, visited)

	# Clear the visited nodes
	visited.remove((row, col))
	return tmp


with open("../inputs/2002_10_problem4.txt") as file_data:

	# Read the grid of letters and the list of words
	data = file_data.read().split("\n")
	lines, length = map(int, data[0].strip().split(' '))
	matrix = [i.lower() for i in data[1:lines+1]]
	words = [i.lower() for i in data[lines+1:]]

	# Search each word
	for word in words:
		# Keep track of occurrences
		occurrences = []
		for r in range(len(matrix)):
			for c in range(len(matrix[0])):
				res = search(word, 0, r, c, matrix, set())
				# If the word is found, update the occurrences list
				if res:
					occurrences.append([r+1, c+1])

		# By default, the left most occurrence is the first pair in the list
		print(occurrences[0][0], occurrences[0][1])
