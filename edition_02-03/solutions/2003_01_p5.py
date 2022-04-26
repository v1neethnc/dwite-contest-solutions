# January 2003, Problem 5: CRIBBAGE HAND SCORE
# https://github.com/v1neethnc/dwite-contest-solutions


def fifteen_counts(ind, sum, lst):

	# If the index has crossed the list
	if ind == len(lst):

		# Check of the sum is 15
		if sum == 15:
			return 1

		# Since there is nothing more to check, return the result
		return 0
		
	# Generate the lists consisting of the current number, and without the current number
	r1 = fifteen_counts(ind + 1, sum + lst[ind], lst)
	r2 = fifteen_counts(ind + 1, sum, lst)

	# Add the number of occurrences of 15 being the sum of subset
	return r1 + r2


with open("../inputs/2003_01_problem5.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [[j for j in i.split(' ')] for i in file_data.read().split("\n")]
	value_map = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
	cards_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

	# Iterate through the cases
	for case in data:
		values = [i[0] for i in case]
		for i in range(len(values)):
			if values[i] == '0':
				values[i] = 'T'
		suits = [i[1] for i in case]
		
		card_values = [value_map[i] for i in values]
		score = 0

		# Check for multiples
		for i in set(values):
			if values.count(i) in [2, 3, 4]:
				score += (values.count(i) - 1) * values.count(i)

		# Check for fifteens
		score += fifteen_counts(0, 0, card_values) * 2

		# Check for Jack At The Start
		for i in range(len(values) - 1):
			if values[i] == 'J' and suits[i] == suits[4]:
				score += 1
				break

		# Check for Flush
		if len(set(suits)) == 1:
			score += 5
		elif len(set(suits[:-1])) == 1:
			score += 4
		tmp_cards_val = [cards_order.index(i) for i in values]
		tmp_cards_val.sort()

		# Sliding window to check for Run
		st, end = 0, 1
		ctr = 1
		max_ctr = 0
		while end < len(tmp_cards_val):
			st_val = tmp_cards_val[st]
			end_val = tmp_cards_val[end]
			check_sum = ((end_val + st_val) * (end_val - st_val + 1)) // 2 
			if sum(tmp_cards_val[st:end + 1]) == check_sum:
				end += 1
				ctr += 1
			else:
				max_ctr = max(max_ctr, ctr)
				st += 1
				end = st + 1
				ctr = 0
		max_ctr = max(max_ctr, ctr)
		if max_ctr > 2:
			score += max_ctr

		print(score)
