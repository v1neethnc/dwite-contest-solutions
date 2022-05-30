# November 2003, Problem 4: Bin Packing
# https://github.com/v1neethnc/dwite-contest-solutions


def first_bin(lst: list) -> list:

	"""
	Implement the First Bin method on the given list.

	Parameters:
		lst:	(list) a given list of numbers indicating candy box weights
	
	Returns:
		(list): weights of non-empty candy bins
	"""


	# Initialize 50 bins with amount of empty space available
	bucket_list = [10] * 50

	# Iterate through the list
	for element in lst:
		
		# Update the first bucket that can hold the box
		for j in range(len(bucket_list)):
			if bucket_list[j] >= element:
				bucket_list[j] -= element
				break
	
	# Return the weights of the non-empty bins
	return [10-i for i in bucket_list if i != 10]
				
				
def best_bin(lst: list) -> list:

	"""
	Implement the Best Bin method on the given list.

	Parameters:
		lst:	(list) a given list of numbers indicating candy box weights
	
	Returns:
		(list): weights of non-empty candy bins
	"""


	# Initialize 50 bins with amount of empty space available
	bucket_list = [10] * 50

	# Iterate through the list
	for i in lst:
		
		# Find the best bucket and update the bin
		if i in bucket_list:
			ind = bucket_list.index(i) 
			bucket_list[ind] -= i
		else:
			for k in range(len(bucket_list)):
				if bucket_list[k] > i:
					bucket_list[k] -= i
					break

	# Return the weights of the non-empty bins
	return [10-i for i in bucket_list if i != 10]


def worst_bin(lst: list) -> list:

	"""
	Implement the Worst Bin method on the given list.

	Parameters:
		lst:	(list) a given list of numbers indicating candy box weights
	
	Returns:
		(list): weights of non-empty candy bins
	"""


	# Initialize 50 bins with amount of empty space available
	bucket_list = [10] * 50

	# Iterate through the list
	for i in data:

		# Initialize the first bucket
		if bucket_list.count(10) == 50:
			bucket_list[0] -= i
		else:
			# Find the lightest bin and place the new box in it
			min_bucket = 0
			ind = 0
			for k in range(len(bucket_list)):
				if bucket_list[k] > min_bucket and bucket_list[k] != 10:
					min_bucket, ind = bucket_list[k], k
			if bucket_list[ind] < i:
				ind = bucket_list.index(10)
			bucket_list[ind] -= i

	# Return the weights of the non-empty bins
	return [10-i for i in bucket_list if i != 10]


with open("2003_11_problem4.txt") as file_data:

	# Create list from file and initialize the index to read from data
	data = list(map(int, file_data.read().split('\n')))

	print(f"FB {first_bin(data)}")
	print(f"BB {best_bin(data)}")
	print(f"WB {worst_bin(data)}")
	data.sort()
	print(f"FBA {first_bin(data)}")
	data.sort(reverse = True)
	print(f"FBD {first_bin(data)}")
