# February 2004, Problem 5: School Attendance
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2004_02_problem5.txt") as file_data:

	# Create list from file
	data = [list(map(int, i.split(' '))) for i in file_data.read().split('\n')]

	# Calculate total, absent students, and attendance percent
	total_students = sum([i[0] for i in data])
	absent_students = sum([i[1] for i in data])
	attendance_percent = [(i[0]-i[1])/i[0] for i in data]

	# Create a sorted list for fetching indices
	sorted_list = [i for i in attendance_percent]
	sorted_list.sort(reverse=True)

	# Printing the results
	print(f"{total_students}\n{absent_students}\n{attendance_percent.index(max(attendance_percent)) + 1}")
	print([attendance_percent.index(i)+1 for i in sorted_list])
	print(round(sum([i[2] for i in data])/len(data)))
