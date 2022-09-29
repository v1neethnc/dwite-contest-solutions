# January 2004, Problem 5: Waiting at the Bank
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_01_problem5.txt") as file_data:

	# Create list from file
	data = file_data.read().split('\n')
	ind = 0
	# Iterate through the input
	while ind < len(data):
		ctr = int(data[ind])
		names, durations, timestamps = [], [], []

		# Create lists of data
		for i in range(1, ctr+1):
			vals = data[ind + i].split(' ')
			timestamps.append(vals[0])
			durations.append(int(vals[1]))
			names.append(vals[2])
		outputs = [data[i] for i in range(ind + ctr + 1, len(data))]
		ind += len(data)

		# Get the starting time based on the first timestamp and first output
		curr_time = min(timestamps[0], outputs[0])
		temp_ind, temp_ctr = 0, len(durations)
		wait_list = []

		# Iterate until the maximum timestamp is reached
		max_time = max(timestamps[-1], outputs[-1])
		while curr_time != max_time:

			# Check if people come to the bank at the current timestamp
			if curr_time in timestamps:
				t_ind = timestamps.index(curr_time)

				# Add them to the queue
				while t_ind < len(timestamps) and timestamps[t_ind] == curr_time:
					wait_list.append([names[temp_ind], durations[temp_ind]])
					temp_ind += 1
					t_ind += 1
			
			# Check if the current time is in the outputs
			if curr_time in outputs:
				outputs = outputs[1:]
				name, ct = '', 0
				ct = len(wait_list) - 1 if len(wait_list) > 1 else 0
				name = wait_list[1][0] if len(wait_list) > 1 else ''
				print(f"{ct} {name}")

			# Update the wait list depending on the durations
			if len(wait_list) > 0:
				wait_list[0][1] -= 1

				if wait_list[0][1] == 0:
					wait_list = wait_list[1:]
					temp_ctr -= 1
			
			# Update the current time
			hour, minute = map(int, curr_time.split(":"))
			minute = (minute + 1) % 60
			if minute == 0:
				hour = (hour % 12) + 1
			curr_time = str(hour).zfill(2) + ":" + str(minute).zfill(2)
