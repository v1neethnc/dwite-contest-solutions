# November 2002, Problem 5: NOW I KNOW MY ABC'S
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_11_problem5.txt") as file_data:

	# Read the data from the lines
	data = file_data.read().split("\n")
	for i in data:

		# Normalize the sentence by converting everything to uppercase
		line = i.upper()

		# Create a hashmap of letter and corresponding counts
		dict_map = {chr(i): line.count(chr(i)) for i in range(ord('A'), ord('Z') + 1) if line.count(chr(i)) > 0}
		
		# Create the string in the specified format and print the result
		res = ''
		for i in dict_map.keys():
			res += i + '-' + str(dict_map[i]) + ':'
		print(res[:-1])
