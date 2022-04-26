# December 2002, Problem 4: AREA OF A TRIANGLE
# https://github.com/v1neethnc/dwite-contest-solutions


from math import sqrt

# Function to calculate the triangle sides given the points
def sides_calc(p1: list, p2: list, p3: list) -> tuple(float, float, float):

	"""
	Takes three coordinates, treats them as a triangle and returns the side lengths

	Parameters:
		p1: (list[int, int]) coordinates of the first vertex
		p2: (list[int, int]) coordinates of the second vertex
		p3: (list[int, int]) coordinates of the third vertex

	Returns:
		l1, l2, l3: (float, float, float) the lengths of the lines connecting every pair of vertices
	"""

	return round(sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2), 3), \
	 	   round(sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2), 3), \
		   round(sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2), 3)


with open("../inputs/2002_12_problem4.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]

	# Iterate through the cases
	for line in data:

		# Get the points and calculate the sides
		p1, p2, p3 = line[0:2], line[2:4], line[4:]
		d1, d2, d3 = sides_calc(p1, p2, p3)
		
		# Check for triangle inequality violations
		if d1 + d2 <= d3 or d2 + d3 <= d1 or d3 + d1 <= d2:
			print("NOT POSSIBLE")
			
		else:
			# Calculate area using Heron's formula
			s = (d1 + d2 + d3) / 2
			area = round(sqrt(s * (s-d1) * (s-d2) * (s-d3)), 1)
			print(f"{area:.2f}")
