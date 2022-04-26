# December 2002, Problem 1: DICE GAME
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_12_problem1.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a game
	data = [[int(j) for j in i.split(' ')] for i in file_data.read().split("\n")]
	for line in data:

		# Save the first element and create flag to track win/loss/no result
		first = line[0]
		flag = False
		for ind in range(len(line)-1):
			val = line[ind]
			
			# Check for win/loss on first roll
			if ind == 0:
				if val in [2, 3, 10]:
					print(f"LOSS-{ind+1}")
					flag = True
				elif val in [7, 11]:
					print(f"WIN-{ind+1}")
					flag = True
			else:
				# Check for win conditions on rolls after the first one
				if val == first or val in [7, 10, 11]:
					print(f"WIN-{ind+1}")
					flag = True
			
			# Break the loop if a result is reached
			if flag:
				break
		
		# If the result is not reached, then flag remains False
		if not flag:
			print(f"NO RESULT-{len(line)-1}")
