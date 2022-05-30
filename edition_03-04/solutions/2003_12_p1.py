# December 2003, Problem 1: Metric to Imperial Distance Converter
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2003_12_problem1.txt") as file_data:

	# Create list from file and initialize the index to read from data
	data = list(map(int, file_data.read().split('\n')))

	# Create map of units to use
	suffixes = ['mile(s)', 'yard(s)', 'f(oo)eet', 'inch(es)']
	
	# Iterate through the list
	for ind in range(len(data)):

		# Read the value and calculate the different unit values
		vl = data[ind]
		res = ''
		for index, scale in enumerate([160934.4, 91.44, 30.48, 2.54]):
			res += str(int(vl // scale)) + " " + suffixes[index] + ", "
			vl = vl % scale
		
		# Print the string by omitting the comma at the end 
		print(res[:-2])
