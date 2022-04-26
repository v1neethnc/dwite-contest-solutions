# October 2003, Problem 4: You're "It"
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_10_problem4.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# Iterate through the cases
	ind = 0
	while ind < len(data):
		
		# Get the number of people and create a name-response hashmap
		n_val = int(data[ind])
		responses = [i.split(' ') for i in data[ind + 1: ind + n_val + 1]]
		name_response_map = {j[0]: j[1] for j in responses}
		
		# Populate the order of hands (right/left specification is unnecessary)
		hands_order = []
		for i in name_response_map.keys():
			hands_order.append(i)
			hands_order.append(i)
		ind = ind + n_val + 1

		# Start from the first position
		offset = 0

		# Number of turns
		while len(hands_order) > 1:

			# "Engine engine... money back" has 21 words, which in a list means index 20
			stop_point = 20 % len(hands_order)

			# If current response is NO, then go ahead by 9
			if name_response_map[hands_order[(offset + stop_point) % len(hands_order)]] == 'NO':
				last_stretch = 9

			# If YES, then go ahead by 10
			else:
				last_stretch = 10
			
			# Calculate who is IT and delete them, update the new start position
			final_stop = (last_stretch + offset + stop_point) % len(hands_order)
			del hands_order[final_stop]
			offset = final_stop % len(hands_order)
		
		# The list will contain only one element as everyone else is eliminated
		print(hands_order[0])
