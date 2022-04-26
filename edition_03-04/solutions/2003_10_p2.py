# October 2003, Problem 2: Gas Bill
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_10_problem2.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = [float(i) for i in file_data.read().split("\n")]
	for case in data:

		# Initialize with the monthly rate
		res = 10

		# Add up the rates per unit volume
		rates = [0.275635, 0.045293, 0.008811, .103994]
		for i in rates:
			res += round(case * i, 2)
		
		# Add the GST
		res += round(res * 0.07, 2)
		res = round(res, 2)
		print(f"{res:.2f}")
