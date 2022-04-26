# January 2003, Problem 3: CRYPTOLOGY
# https://github.com/v1neethnc/dwite-contest-solutions


from string import punctuation

with open("../inputs/2003_01_problem3.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = file_data.read().split("\n")
	data = [[data[i], data[i+1], data[i+2]] for i in range(0, len(data), 3)]

	# Iterate through the cases
	for case in data:

		# Generate the key string 
		key_string = ''
		for i in case[0]:
			if i not in key_string and i not in punctuation and i != ' ':
				key_string += i

		# Add the characters that are not available in the given string
		for j in 'ABCDEFGHIJLKMNOPQRSTUVWXYZ':
			if j not in key_string:
				key_string += j
		
		# Initialize the result string
		res = ''
		key_string = key_string[::-1]
		for i in case[2]:
			if i in punctuation or i == ' ':
				res += i
			else:
				# Encode or decode based on the inputs
				if case[1] == 'ENCODE':
					res += key_string[ord(i) - ord('A')]
				elif case[1] == 'DECODE':
					res += chr(key_string.index(i) + ord('A'))
		print(res)
