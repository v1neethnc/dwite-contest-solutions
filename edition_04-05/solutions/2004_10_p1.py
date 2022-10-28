# October 2004, Problem 1: Area of Circle
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_10_problem1.txt") as file_data:

	# Create list from file
	data = [list(map(float, i.split(' '))) for i in file_data.read().split('\n')]

	# Iterate through the circles
	for circle in data:
		# Calculate the radius and the area and print result
		radius = ((circle[2] - circle[0])**2 + (circle[3] - circle[1])**2)**0.5
		print(round(3.14159 * radius * radius, 3))
