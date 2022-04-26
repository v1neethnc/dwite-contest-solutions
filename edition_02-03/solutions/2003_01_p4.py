# January 2003, Problem 4: NUMBER THEORY
# https://github.com/v1neethnc/dwite-contest-solutions


# Function to calculate the partition
def partition_calc(n: int, k: int) -> int:

	"""
	Function based on the partition formula to calculate the number
	of ways a given number n can be partitioned into k parts

	Parameters:
		n: (int) the number to partition
		k: (int) the number of partitions
	
	Returns:
		(int) the total number of possible partitions
	"""

	if n < k:
		return 0
	if k == 1:
		return 1

	# The calculation can be done using the following formula:
	# p(n, k) = p(n-1, k-1) + p(n-k, k)
	return partition_calc(n-1, k-1) + partition_calc(n-k, k)

with open("../inputs/2003_01_problem4.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[int(i) for i in dt.split(' ')] for dt in file_data.read().split("\n")]
	for i in data:
		print(partition_calc(i[0], i[1]))
