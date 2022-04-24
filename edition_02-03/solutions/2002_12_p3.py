# December 2002, Problem 3: SANTA'S MAGIC SACK
# https://github.com/v1neethnc/dwite-contest-solutions


# Function to generate a list of possible sums under 8000000
def generate_sum_list(ind, sum, lst):

	# If the index has crossed the list
	if ind == len(lst):
		res = []
		# Check the sum and append it to the result
		if sum <= 8000000:
			res.append(sum)

		# Since there is nothing more to check, return the result
		return res
	# Generate the lists consisting of the current number, and without the current number
	r1 = generate_sum_list(ind + 1, sum + lst[ind], lst)
	r2 = generate_sum_list(ind + 1, sum, lst)

	# Concatenate both the lists and return the result
	r1.extend(r2)
	return r1


# Using a meet-in-the-middle approach to solve this problem
with open("2002_12_problem3.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]
	
	# Iterate through the cases
	for case in data:
		
		# Get the length and the list
		ln = case[0]
		lst = case[1:]

		# Generatae the possible sums of each half of list
		lst1 = generate_sum_list(0, 0, lst[:ln//2])
		lst2 = generate_sum_list(0, 0, lst[ln//2:])

		# Sort the second list
		lst2.sort()
		result = 0

		# Iterate through the first sum list
		for i in lst1:
			# Get the maximum possible sum under 8000000
			ind = 0
			while ind < len(lst2) and i + lst2[ind] <= 8000000:
				ind += 1
			# Store the maximum in the result variable
			result = max(result, i + lst2[ind-1])
		print(result)