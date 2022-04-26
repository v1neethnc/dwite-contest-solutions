# February 2003, Problem 2: HOW MANY SUMS
# https://github.com/v1neethnc/dwite-contest-solutions


# Function to count number of subsets whose sum is equal to a specified number
def subset_sum_counter(lst: list, i: int, curr_sum: int, lst_len: int, sum_to_check: int) -> int:

	"""
	Calculate the total count of subsets of a list whose sum is equal to a given value

	Parameters:
		lst: 			(list) the list of elements to check
		i: 				(int) the index of the element in the list to check
		curr_sum: 		(int) the current running sum
		lst_len: 		(int) the length of the list
		sum_to_check: 	(int) the given sum to check against

	Returns:
		(int) the number of subsets whose sum is equal to sum_to_check
	"""

	# Return 1 if the current sum is equal to the sum to check for
	if curr_sum == sum_to_check:
		return 1

	# If index crosses the list or current sum crosses the required
	if curr_sum > sum_to_check or i == lst_len:
		return 0

	# Check for counter with and without including the current element
	v1 = subset_sum_counter(lst, i + 1, curr_sum + lst[i], lst_len, sum_to_check)
	v2 = subset_sum_counter(lst, i + 1, curr_sum, lst_len, sum_to_check)
	return v1 + v2


with open("../inputs/2003_02_problem2.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]
	
	# Iterate through the cases
	for case in data:

		# Get the values and call the function
		sm, ls_len = case[0], case[1]
		lst = [i for i in case[2:]]
		lst.sort()
		print(subset_sum_counter(lst, 0, 0, ls_len, sm))
