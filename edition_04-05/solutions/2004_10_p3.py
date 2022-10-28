# October 2004, Problem 3: The Tallest in the Class
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_10_problem3.txt") as file_data:

	# Create list from file
	dt = file_data.read().split('\n')
	data = [i.split(' ') for i in dt[1:]]

	# Dictionary of factors to normalize height
	factor_dict = {'m': 1, 'dm': 10, 'cm': 100, 'mm': 1000}
	for i in range(len(data)):
		data[i][1] = round(float(data[i][1])/factor_dict[data[i][2]], 6)

	# Sort the data based on the height and name and print the result
	data = sorted(data, key = lambda x: (-x[1], x[0]))
	for i in range(5):
		print(data[i][0])
