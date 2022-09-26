# January 2004, Problem 3: Elapsed Time in Seconds
# https://github.com/v1neethnc/dwite-contest-solutions


import datetime

with open("2004_01_problem3.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	for line in data:
		dt = line.split(' ')
		# Get the different parts of the timestamp
		day, month, year = map(int, dt[0].split('/'))
		hour, minute, sec = map(int, dt[1].split(':'))
		# Calculate the difference in days
		date_diff = datetime.date(year, month, day) - datetime.date(2004, 1, 1)
		# Calculate the number of seconds
		sec_ctr = (date_diff.days * 86400) + (hour * 3600) + (minute * 60) + sec
		print(sec_ctr)
