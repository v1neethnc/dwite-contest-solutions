# December 2003, Problem 2: Lottery Ticket Checker
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_12_problem2.txt") as file_data:

	# Create list from file
	data = [list(map(int, line.split(' '))) for line in file_data.read().split('\n')]
	
	# Create set of winning tickets and bonus number
	winning_tickets = set(data[0][:-1])
	bonus_num = data[0][-1]

	# Iterate through the tickets
	for line in data[1:]:

		# Find the set of common numbers
		intersect = winning_tickets.intersection(set(line))
		
		# Check for prize conditions using the common tickets
		if len(intersect) == 6:
			print("First prize")
		elif len(intersect) == 5:
			if bonus_num in set(line):
				print("Second prize")
			else:
				print("Third prize")
		elif len(intersect) == 4:
			print("Fourth prize")
		elif len(intersect) == 3:
			print("Fifth prize")
		else:
			print("No prize")
