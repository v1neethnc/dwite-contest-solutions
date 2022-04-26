# December 2002, Problem 2: DECEMBER 25
# https://github.com/v1neethnc/dwite-contest-solutions


from math import floor
with open("../inputs/2002_12_problem2.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a game
	data = [int(i) for i in file_data.read().split("\n")]
	day_map = {0: 'SUNDAY', 1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY", 4: "THURSDAY", 5: "FRIDAY", 6: "SATURDAY"}
	
	# Create month map in accordance to the disparate version of the Gauss algorithm
	month_map = {}
	val = 3
	for i in range(1, 13):
		month_map[val] = i
		val += 1
	m, k = month_map[12], 25

	for year in data:
		# Plug in the values in the formula
		c = year // 100
		y = year % 100
		res = (k + floor(2.6*m - 0.2) - (2*c) + y + (y//4) + (c//4)) % 7
		print(day_map[res])
