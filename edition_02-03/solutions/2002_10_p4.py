# October 2002, Problem 4: WORD SEARCH
# https://github.com/v1neethnc/dwite-contest-solutions

def search(word, ind, row, col, mat, visited):
	if ind == len(word):
		return True

	if row not in range(0, len(mat)) or col not in range(0, len(mat[0])) or word[ind] != mat[row][col] or (row, col) in visited:
		return False
	
	visited.add((row, col))
	tmp = False
	directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [-1, -1], [1, 1]]
	for j in directions:
		tmp = tmp or search(word, ind+1, row + j[0], col + j[1], matrix, visited)
	visited.remove((row, col))
	return tmp

with open("../inputs/2002_10_problem4.txt") as file_data:
	data = file_data.read().split("\n")
	lines, length = map(int, data[0].strip().split(' '))
	matrix = [i.lower() for i in data[1:lines+1]]
	words = [i.lower() for i in data[lines+1:]]
	for word in words:
		occurrences = []
		for r in range(len(matrix)):
			for c in range(len(matrix[0])):
				res = search(word, 0, r, c, matrix, set())
				if res:
					occurrences.append([r+1, c+1])

		print(occurrences[0][0], occurrences[0][1])