# January 2004, Problem 1: Clock Hands
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2004_01_problem1.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')

	# Iterate through the cases
	for line in data:
		# Get the hour and minute
		hour, minute = map(int, line.split(':'))
		# Every minute is six degrees
		min_angle = minute * 6
		# Every hour is 30 degrees + delta depending on the number of minutes
		hour_angle = ((hour % 12) * 30) + (min_angle / 12)
		# Calculate the angle and print
		res = abs(min_angle - hour_angle)
		if res > 180:
			res = 360 - res
		print(f"{res:.2f}")
