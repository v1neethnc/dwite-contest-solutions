# December 2003, Problem 4: XOR Cryptology
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2003_12_problem4.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	for ind in range(0, len(data), 2):
		# Get integer equivalent of the decoded character
		decoded = ord(data[ind][0])
		chars = [int(i, 2) for i in data[ind+1].split(' ')]

		# Calculate the key and print the result
		key = decoded ^ chars[0]
		print(''.join([chr(i ^ key) for i in chars]))
