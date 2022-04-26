# December 2002, Problem 5: DUTCH SOLITAIRE
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_12_problem5.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]

	# Iterate through the cases
	for line in data:

		# Create the piles and sort to start, store the subsequent configurations
		piles = [i for i in line[2:]]
		piles.sort()
		configs = [piles]

		# Check all iterations
		for ind in range(0, 100):
			
			# Create the new piles
			new_piles = [i-1 for i in piles if i > 1]
			new_piles.append(len(piles))
			new_piles.sort()

			# Check if the current configuration has already occurred and compare the index
			if new_piles in configs:
				if configs.index(new_piles) == ind - 1:
					print(f"WIN-{ind}")
					break
				elif configs.index(new_piles) < ind - 1:
					print(f"LOSS-{ind+1}")
					break
			
			# Update the configurations and current piles
			configs.append(new_piles)
			piles = [i for i in new_piles]
