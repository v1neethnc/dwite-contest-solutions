# October 2003, Problem 1: Area of Rectangle
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_10_problem1.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]

	# Iterate through the cases
	for line in data:
		
		# Get the points
		p1, p2 = tuple([line[0], line[1]]), tuple([line[2], line[3]])
		
		# Length = difference of x-coordinates, height = difference of y-coordinates
		print((p2[0] - p1[0]) * (p2[1] - p1[1]))
