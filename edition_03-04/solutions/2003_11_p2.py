# November 2003, Problem 2: Palindromic Numbers
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2003_11_problem2.txt") as file_data:

	# Create list, with each element corresponding to a case
	data = list(map(int, file_data.read().split('\n')))

	# Iterate through the cases
	for case in data:

		# Store the initial value and initialize a counter
		tmp = case
		ctr = 0

		# Iterate a hundred times
		while ctr < 100:

			# Calculate the sum of the number and its reverse
			val = tmp + int(str(tmp)[::-1])
			ctr += 1

			# Check if the sum is a palindrome
			if str(val) == str(val)[::-1]:
				print(f"{case} {ctr} {val}")
				# flag = True
				break
			
			# Update the new number to reverse and repeat the process
			tmp = val

		# If the palindrome is not found after 100 iterations
		if ctr == 100:
			print(f"{case} NOT POSSIBLE {tmp}")
