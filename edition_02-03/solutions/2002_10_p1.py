# October 2002, Problem 1: OVERTIME
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_10_problem1.txt") as file_data:

	# Map of hourly rates
	hours_rates_map = {20: 3, 15: 2, 0: 1}
	data = file_data.read().split('\n')

	# Lists of rates and corresponding hours
	rates = [float(data[i]) for i in range(len(data)) if i % 2 == 0]
	hours = [int(data[i]) for i in range(len(data)) if i % 2 != 0]

	for i in range(len(rates)):
		total_pay = 0

		# Calculate the total pay using the map of hourly rates
		for k in hours_rates_map.keys():
			if hours[i] > k:
				total_pay += (hours[i] - k) * (rates[i] * hours_rates_map[k])
				hours[i] = k
		
		# Printing the data on console
		print(f"{total_pay:.2f}")
